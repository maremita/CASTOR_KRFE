#!/usr/bin/env python

###############
### Imports ###
############### 

from castor_krfe import data
from castor_krfe import extraction
from castor_krfe import evaluation
from castor_krfe import __version__

import argparse

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='CASTOR KRFE')

    parser.add_argument('-t', '--train',
                        action='store_true',
                        help="Train a model with a dataset of labeled"
                        "genomic sequences")
 
    parser.add_argument('-v', '--validate',
                        action='store_true',
                        help="Validate dataset")
 
    parser.add_argument('-p', '--predict',
                        action='store_true',
                        help="Predict classes of genomic sequences")

    parser.add_argument('-m', '--model',
                        nargs='?',
                        help="File of the model")

    parser.add_argument('-k', '--kmers',
                        nargs='?',
                        help="File of the extracted k-mers list")

    parser.add_argument('--threshold',
                        type=float,
                        nargs='?',
                        default=1,
                        help="Percentage of performance loss in terms of"
                        "F-measure to reduce the number of attributes")
 
    parser.add_argument('--kmin',
                        type=int,
                        nargs='?',
                        default=5,
                        help="Minimum length of k-mer(s)")

    parser.add_argument('--kmax',
                        type=int,
                        nargs='?',
                        default=5,
                        help="Maximum length of k-mer(s)")
    
    parser.add_argument('--fmin',
                        type=int,
                        nargs='?',
                        default=1,
                        help="Minimum number of features to identify")
    
    parser.add_argument('--fmax',
                        type=int,
                        nargs='?',
                        default=50,
                        help="Maximum number of features to identify")
    
    parser.add_argument('-d', '--data',
                        nargs='?',
                        default='Data/',
                        help="Data directory. If it is not specified, "
                        "the program uses Data/ folder")

    parser.add_argument('-o', '--output',
                        nargs='?',
                        default='Output/',
                        help="Output directory. If it is not specified, "
                        "the program uses Output/ folder")

    parser.add_argument('--version',
                        action='version',
                        version=__version__)

    args = parser.parse_args()

    return args


def main():
    #################
    ### Arguments ###
    #################

    args = parse_arguments()

    # Threshold (percentage of performance loss in terms of 
    # F-measure to reduce the number of attributes)
    T = args.threshold
    # Minimum length of k-mer(s)
    k_min = args.kmin
    # Maximum length of k-mer(s)
    k_max = args.kmax
    # Minimum number of features to identify
    features_min = args.fmin
    # Maximum number of features to identify
    features_max = args.fmax
    # Training dataset
    training_dataset = "HIVGRPCG"
    # Testing dataset
    testing_dataset = "HIVGRPCG"

    mode_training = args.train
    mode_validation = args.validate
    mode_prediction = args.predict

    kmers_file = args.kmers
    model_file = args.model
    ##################
    ### LOAD DATA  ###
    ##################

    dataset = training_dataset

    class_file = "Data/" + dataset + "/class.csv"
    fasta_file = "Data/" + dataset + "/data.fa"


    ####################
    ## Training mode ###
    ####################
    if mode_training:
    # Get training dataset
        print("Loading of the training dataset...")
        training_data = data.generateData(class_file, fasta_file)

        ############################
        ### FEATURES EXTRACTION  ###
        ############################
        best_k_mers, best_k_length = extraction.extractKmers(T, training_data,
                k_min, k_max, features_min, features_max)
        print("Identified k =", best_k_length)
        print("Identified k-mers  =", best_k_mers)

        ##################
        ### EVALUATION ###
        ##################
        evaluation.cross_validation(training_data, best_k_mers, training_data)
    
    
    ######################
    ## Validation mode ###
    ######################
    if mode_validation:
        # Get testing dataset
        print("Loading of the testing dataset...")
        testing_data = data.generateData(class_file, fasta_file)

        print("\nPrediction")
        # the value of best_k_mers will be fetched from a file
        best_k_mers = []
        evaluation.prediction(training_data, testing_data, best_k_mers)
 
    ######################
    ## Prediction mode ###
    ######################
    if mode_prediction:
        pass

if __name__ == "__main__":
    main()
