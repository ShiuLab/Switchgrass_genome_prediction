'''
convert the genotype g.vcf file into genotype matrix
input1: genotype g.vcf file, which has been filtered using 'QD < 2.0 || MQ < 40.0 || FS > 60.0 || MQRankSum < –12.5 || ReadPosRankSum < –8.0 –clusterSize 3 –clusterWindowSize 10' for SNPs, 'QD < 2.0 || FS > 200.0 || ReadPosRankSum < –20.0'  for indels
'''
import sys,os
inp = open(sys.argv[1],'r')
inl = inp.readline()
D = {}
out = open(sys.argv[1] + '_genotype_matrix','w')
while inl:
	if inl.startswith('#CHROM'):
		tem = inl.split('\t')[9:]
		out.write('Chr\tPos\tRef\tAlt\t%s'%'\t'.join(tem))
		out.flush()
	if not inl.startswith('#') and 'PASS' in inl:
		tem = inl.strip().split('\t')
		chr = tem[0]
		pos = tem[1]
		ref = tem[3]
		alt = tem[4].split(',')
		geno = tem[9:]
		res = '%s\t%s\t%s\t%s'%(chr,pos,ref,tem[4])
		for g in geno:
			type = g.split(':')[0]
			type = type.replace('0',ref)
			if '1' in type:
				type = type.replace('1',alt[0])
			if '2' in type:
				type = type.replace('2',alt[1])
			if '3' in type:
				type = type.replace('3',alt[2])
			if '4' in type:
				type = type.replace('4',alt[3])
			if '5' in type:
				type = type.replace('5',alt[4])
			if '6' in type:
				type = type.replace('6',alt[5])
			if '7' in type:
				type = type.replace('7',alt[6])
			res = res + '\t%s'%type	
		out.write(res + '\n')
		out.flush()
	inl = inp.readline()
	
out.close()
