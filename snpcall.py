with open("info.txt") as f:
    content = f.readlines()
    content = content[1:]
  

with open("sequences.fa", 'r') as f1:
	fasta_seqs = {}
	seq_id = []
	seqs = []
	start_pos = []	
	for lines in f1:
		fasta = lines.rstrip()		
		if ">" in fasta:
			seq_id.append(fasta)
		else:
			seqs.append(fasta)
for i in seq_id:
	start_pos.append(i.split(":")[1].split("-")[0])


fasta_seqs = dict(zip(start_pos, seqs))

#print fasta_seqs.keys(), fasta_seqs.values()

for ids, seq in fasta_seqs.items(): 
	for i in content:
        	data=i.split("\t")
		#print ids,data[3]
		if ids==data[3]:			#check if the key in dictionary matches with the column 3 in infor.txt
			#print data[5],data[7]
			#print fasta_seqs[ids]
			mod_list=list(fasta_seqs[ids])		
			mod_list[1001] = data[7].rstrip().lstrip()  ### if match found then chnage the 1001 chr of seq
			mod_str=''.join(mod_list)
			print ">",ids,"\n", mod_str
			#####other way of replacing the string####
			#print mod_str[1001],len(mod_str)
			#target_seq_u = fasta_seqs[ids][0:1001]
			#target_seq_d = fasta_seqs[ids][1002:]
			#target_seq_center = data[7].rstrip().lstrip()
			#final_mod_seq = str(target_seq_u) + str(target_seq_center) + str(target_seq_d)
			#print 
			#print final_mod_seq
		#	print
			#print type(fasta_seqs[ids])
			#fasta_seqs[ids] = final_mod_seq
		
		
		
	

			
