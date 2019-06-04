#!/usr/bin/env python

# Script to determine the average fragment length of reads
# mapped against a reference. As input give a sam file, where the 
# top three lines are replaced with the following line:
#name	flag	rname	position	mapq	cigar	rnext	pnext	tlen	sequence	qual	filename

import numpy as np
import pandas as pd

import argparse

parser = argparse.ArgumentParser(
    description='Determine the fragmentsize of mapped read origins',
    epilog=('xxx'))

parser.add_argument(
	'-i', '--infile',
	help=('The modified samfile to be analysed. Give modifies samfile as renamed to .csv'))

parser.add_argument(
	'-o', '--outfile',
	help=('The outfile, containing name and fragmentsize. For visualisation use sum.py'))

args = parser.parse_args()

out = args.outfile

file = args.infile

samfile = pd.read_csv(file, sep='	')

sortedsam = samfile.sort_values(by=['name'])

fragmentsizes = {}

previousname = None
previouspair = None
previousposition = None
previoussequence = None

for index, row in sortedsam.iterrows():
	rowname = row['name'].split()
	name = rowname[0]
	pair = rowname[1]
	rowposition = row['position']
	
	if previousname == name:
		# Calculate the fragment lenght.
		if rowposition >=  previousposition:
			length2 = len(row['sequence'])
		elif previousposition > rowposition:
			length2 = len(previoussequence)
		length1 = abs(previousposition-rowposition)
		fragmentsize = length1 + length2
		fragmentsizes[name] = fragmentsize

	previousname = name
	previouspair = pair
	previousposition = row['position']
	previoussequence = row['sequence']

with open(out, 'a') as outfile:
	for name in fragmentsizes:
		outfile.write('%s %s\n' %(name, fragmentsizes[name]))
