# Imports
import csv
import numpy as np
from Bio import SeqIO

def generateData(cls_file, fa_file):
	# Variable data 
	data = []

    # Open the class file
	with open(cls_file) as f:
		reader = list(csv.reader(f))

	# Open the sequences file
	for record in SeqIO.parse(fa_file, "fasta"):
		for i, read in enumerate (reader):
			if read[0] == record.id:
				# Generate table [Id, Sequences, Class]
				data.append([record.id, record.seq.upper(), read[1]])

	# Return data
	return data
