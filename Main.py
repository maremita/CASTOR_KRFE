###############
### Imports ###
############### 
import Data
import Extraction
import Evaluation

#################
### VARIABLES ###
#################

# Threshold (percentage of performance loss in terms of F-measure to reduce the number of attributes)
T = 1
# Minimum length of k-mer(s)
k_min = 3
# Maximum length of k-mer(s)
k_max = 10
# Minimum number of features to identify
features_min = 1
# Maximum number of features to identify
features_max = 50
# Training dataset
training_dataset = "HIVGRPCG"
# Testing dataset
testing_dataset = ""


##################
### LOAD DATA  ###
##################


# Get training dataset
print("Loading of the training dataset...")
if training_dataset: training_data = Data.generateData(training_dataset)

# Get testing dataset
print("Loading of the testing dataset...")
if testing_dataset: testing_data = Data.generateData(testing_dataset)

############################
### FEATURES EXTRACTION  ###
############################
best_k_mers, best_k_length = Extraction.extractKmers(T, training_data, k_min, k_max, features_min, features_max)
print("Identified k =", best_k_length)
print("Identified k-mers  =",best_k_mers)

##################
### EVALUATION ###
##################
Evaluation.cross_validation(training_data, best_k_mers, best_k_length, training_data)
if testing_dataset:
	print("\nPrediction")
	Evaluation.prediction(training_data, testing_data, best_k_mers, best_k_length)

