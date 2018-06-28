# @author: Judith Vlaar
# @date: June 2018
# @description: Merge sam files RNA seq runs of the same sample and same library prep  

import re
import os

data_folder = "hpc/"
sample_to_merge = "Desktop/testRnaMerge.txt"  #colum 1 sample name colum 2 run first colunmn 3 run second 

output_folder = "hpc/" 

with open(sample_to_merge) as filelist:
	for line in filelist:
		line = line.rstrip()
		columns = line.split("\t")
		sample = columns[0]
		run_1 = columns[1]
		run_2 = columns[2]
		print run_1		
		
		#GET INPUT PATHWAYS OF SEPARTE RUNS 
		input_1 = "{0}/{1}".format(data_folder, run_1)
		input_2 = "{0}/{1}".format(data_folder, run_2)
		merged_files = "{0}/{1}/{1}_merged_files".format(output_folder, sample)
		
		#MERGE THE SAM FILES
		os.system(java -jar $PICARD MergeSamFiles I=input_1 I=input_2 O=merged_files)
		
		#SORT THE SAM FILES 	
		sort_merged_files = "{0}_{1}".format(merged_files, "sort")
		os.system(/hpc/local/CentOS7/cog_bioinf/sambamba_v0.5.8/sambamba sort merged_files) 
		
		#INDEX THE SAM FILES	
		os.system(samtools index sort_merged_files) 
		
		#REMOVE NOT SORTED SAM FILE	
		os.system(rm merged_files)
		
		print "Merge {0} is done, {1} is created".format(sample, sort_merged_files) 
			
	