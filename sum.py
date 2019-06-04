#!/usr/bin/env python

# Script to plot the distribution of fragment sizes
# for the combined output.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

import argparse

parser = argparse.ArgumentParser(
    description='Determine the fragmentsize of mapped read origins',
    epilog=('xxx'))

parser.add_argument(
	'-i', '--infile',
	help=('The outputfile of fragsize.py to be analysed.'))

args = parser.parse_args()

file = args.infile

with open(file) as fragmentlengths:
	numberoffrag = 0
	fraglengthsum = 0
	alllengths = []
	for line in fragmentlengths:
		line = line.split()[1]
		alllengths.append(int(line))
		numberoffrag += 1
		fraglengthsum += int(line)
	averagefraglength = int(fraglengthsum/numberoffrag)

	# Calculate standard deviation
	sd = []
	for number in alllengths:
		sd.append((number - averagefraglength)**2)
	variance = sum(sd)/len(sd)
	standarddev = round(math.sqrt(variance), 2)

fraglengths = pd.read_csv(file, sep=' ', header=0)

maxfraglength = max(fraglengths[fraglengths.columns[1]])
minfraglength = min(fraglengths[fraglengths.columns[1]])

# Histogram
plt.hist(fraglengths[fraglengths.columns[1]], color = 'blue', edgecolor = 'black',
		 bins = int(400/5))

# Add labels
plt.title('Histogram of Fragment Lengths')
plt.xlabel('Fragment length in bp')
plt.ylabel('Number of fragments')
#plt.yscale('log')
plt.text(135, 28,
	'Average fragment size: %s\nStandard deviation: %s\nMax fragment size: %s\nMin '
	'fragment size: %s' %(averagefraglength, standarddev, maxfraglength, minfraglength),
	 style='italic',
     bbox={'facecolor':'blue', 'alpha':0.5, 'pad':10})

plt.show()