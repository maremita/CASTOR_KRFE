==================================CASTOR-KRFE=======================================
= CASTOR-KRFE v1.0 Help file																		  =
= Feature extractor for viral genomic classification                               =
= Copyright (C) 2018  Dylan Lebatteux, Amine M. Remita, Abdoulaye Banire Diallo    =
= Author : Dylan Lebatteux, Amine M. Remita													  =
= Contact : lebatteux.dylan@courrier.uqam.ca												     =
====================================================================================



==========================================DESCRIPTION=================================================
= CASTOR-KRFE contains three modes: 																					  =
= - Train : Extract best kmer features and train a model with a dataset of labeled genomic sequences =
= - Evaluation : Evaluate a prediction model with a dataset of labeled genomic sequences             =
= - Prediction : Predict classes of unknown genomic sequences                                        =
======================================================================================================


===========================REQUIRED SOFTWARES=========================
= - numpy (https://docs.scipy.org/doc/numpy-1.13.0/user/install.html)=
= - scipy (https://www.scipy.org/install.html)                       =
= - scikit-learn  (https://scikit-learn.org/stable/install.html)     =
= - biopython (https://biopython.org/wiki/Download)                  =
======================================================================


================================================CASTOR-KRFE OPTIONS==================================================
= -h : Show the help																																  =
= -t, --train : Extract best kmer features andtrain a model with a dataset of labeled genomic sequences		   	  =
= -e, --evaluate : Evaluate a model prediction with a dataset of labeled genomic sequences								  =
= -p, --predict : Predict classes of unknown genomic sequences                                                      =
= -f FASTA, --fasta FASTA : Fasta file containing the sequences (the file is used in the three modes)               =
= -c [CSV], --csv [CSV] : CSV file containing the labels of the sequences with the format : ID,label                =
=					      The file could be used in the training/evaluation modes.                                       =
= -m [MODEL], --model [MODEL] : File of the model                                                                   =
= -k [KMERS], --kmers [KMERS] : Name of the file of the extracted k-mers list (Défault : Kmers.txt)                 =
= -o [OUTPUT], --output [OUTPUT] : Output directory. If it is not specified, the program uses Output/ folder        =
= --threshold [THRESHOLD] : Percentage of performance loss in terms of F-measure to reduce the number of attributes =
=								    Default : T = 1                                                                         =
=						          To reduce the number of features T = 0,99 showed great performance                      =
= --kmin [KMIN] : Minimum length of k-mer(s)                                                                        =
= --kmax [KMAX] : Maximum length of k-mer(s)                                                                        =
= --fmin [FMIN] : Minimum number of features to identify                                                            =
= --fmax [FMAX]: Maximum number of features to identify                                                             =
= --version : Show program's version number and exit                                                                =
=====================================================================================================================

=====EXAMPLES=====

Extract features and train a model: 
python -W ignore Main.py -t -f Data/HIVGRPCG/data.fa -c Data/HIVGRPCG/class.csv --kmin 5 --kmax 8 --fmin 1 --fmax 5 --threshold 1

Evaluate a model: 
python -W ignore Main.py -e -f Data/HIVGRPCG/data.fa -c Data/HIVGRPCG/class.csv -m Output/model.pkl

Precict sequences: 
python -W ignore Main.py -p -f Data/HIVGRPCG/data.fa -m Output/model.pkl

=====INPUT FILES======

======================

=====OUTPUT FILES=====

======================
	

============================================================REFERENCES==============================================
= Scikit-learn
= Pedregosa, Fabian, et al. "Scikit-learn: Machine learning in Python." 
= Journal of machine learning research 12.Oct (2011): 2825-2830.
= Website : https://scikit-learn.org/
=
= Biopython
= Cock, Peter JA, et al. "Biopython: freely available Python tools for computational molecular biology and bioinformatics." 
= Bioinformatics 25.11 (2009): 1422-1423.
= Website : https://biopython.org/
===========================================================================================================================
