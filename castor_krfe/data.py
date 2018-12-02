# Imports
import csv
import numpy as np
from Bio import SeqIO

def generateData(dataset):
	# Variable data 
	data = []

	# Open the class file
	with open("Data/" + dataset + "/class.csv") as f:
		reader = list(csv.reader(f))

	# Open the sequences file
	for record in SeqIO.parse("Data/" + dataset + "/data.fa", "fasta"):
		for i, read in enumerate (reader):
			if read[0] == record.id:
				# Generate table [Id, Sequences, Class]
				data.append([record.id, record.seq.upper(), read[1]])

	# Return data
	return data
