'''
input1: genotype matrix with biallelic SNP or indel
'''
import sys,os
inp = open(sys.argv[1],'r').readlines()
out = open(sys.argv[1].split('.txt')[0] + '_fastPHASE.txt','w')
out.write('%s\n'%(len(inp[0].split('\t')) - 4))
out.write('%s\n'%(len(inp)-1))
tem = inp[0].strip().split('\t')
for i in range(4,len(inp[0].split('\t'))):
	ind = tem[i]
	out.write('# id %s\n'%ind)
	out1 = ''
	out2 = ''
	for inl in inp[1:]:
		ref = inl.split('\t')[2]
		alt = inl.split('\t')[3]
		snp = inl.strip().split('\t')[i]
		snp = snp.replace('.','?')
		### for indel, if alt is longer than ref, then encoded as 'I', while ref was encoded as 'R'
		if len(alt) > len(ref):
			snp = snp.replace(alt,'I')
			snp = snp.replace(ref,'R')
		### for indel, if alt is longer than ref, then encoded as 'D', while ref was encoded as 'R'
		if len(alt) < len(ref):
			snp = snp.replace(ref,'R')
			snp = snp.replace(alt,'D')
		allele = snp.split('/')
		if out1 == '':
			out1 = allele[0]
			out2 = allele[1]
		else:
			out1 = out1 + ' ' + allele[0]
			out2 = out2 + ' ' + allele[1]
	out.write(out1 + '\n')
	out.write(out2 + '\n')

out.close()
				
		