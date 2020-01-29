import pandas as pd
import numpy as np
import os, sys
import subprocess

input_dir = "/home/tanashree/Downloads/code_gff"

os.chdir(input_dir)

#for x in open('try.gff').readlines():
#@	print x.split('\t')

chr_Ca=[]
pos=[]
fh_gff=open('try.gff','r+')
for pos_id in open("list.txt",'r+'):
	splits1 = pos_id.split("_")
	chr_Ca=splits1[0]
	pos=int(splits1[1])
	fh_gff.seek(0)
	print chr_Ca,pos
	for gff_data in fh_gff:
		gff_data_split = gff_data.split('\t')
		#print gff_data_split
		if gff_data_split[0]==chr_Ca:
			#print 'match found'
			if int(gff_data_split[3])<=pos and int(gff_data_split[4])>=pos:
				print 'match found',gff_data




#res = dict(zip(chr_Ca, pos)) 

#print res

'''
for i in range(len(chr_Ca)):
	#print chr_Ca[i],pos[i]
	COMMAND = """awk '{if($1 == "chr_Ca[i]" && $4 <="pos[i]"  && $5 >="pos[i]" ) {print $0}}' try.gff"""
	subprocess.call(COMMAND, shell=True)

'''

