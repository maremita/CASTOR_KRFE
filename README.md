# CASTOR_KRFE

* CASTOR-KRFE v1.0 Help file
* Feature extractor for viral genomic classification                               
* Copyright (C) 2018  Dylan Lebatteux, Amine M. Remita, Abdoulaye Banire Diallo    
* Author : Dylan Lebatteux, Amine M. Remita
* Contact : lebatteux.dylan@courrier.uqam.ca


## Description 

CASTOR-KRFE contains three modes:								      
- **Training** : Extract best kmer features and train a model with a dataset of labeled genomic sequences  
- **Evaluation** : Evaluate a prediction model with a dataset of labeled genomic sequences                 
- **Prediction** : Predict classes of unknown genomic sequences                                             


## Required Software

- numpy (https://docs.scipy.org/doc/numpy-1.13.0/user/install.html) 
- scipy (https://www.scipy.org/install.html)                        
- scikit-learn  (https://scikit-learn.org/stable/install.html)      
- biopython (https://biopython.org/wiki/Download)   
- matplotlib (optional, https://matplotlib.org/)


## Options
```
-h : Show the help
-t, --train : Extract best kmer features and train a model with a dataset of labeled genomic sequences
-e, --evaluate : Evaluate a model prediction with a dataset of labeled genomic sequences
-p, --predict : Predict classes of unknown genomic sequences
-f FASTA, --fasta FASTA : Fasta file containing the sequences (the file is used in the three modes)
-c [CSV], --csv [CSV] : CSV file containing the labels of the sequences with the format : ID,label
> The file could be used in the training/evaluation modes.

-m [MODEL], --model [MODEL] : File of the model <br/>
-k [KMERS], --kmers [KMERS] : Name of the file of the extracted k-mers list (Défault : Kmers.txt)
-o [OUTPUT], --output [OUTPUT] : Output directory. If it is not specified, the program uses Output/ folder 
--threshold [THRESHOLD] : Percentage of performance loss in terms of F-measure to reduce the number of attributes
>Default : T = 1
To reduce the number of features T = 0,99 showed great performance

--kmin [KMIN] : Minimum length of k-mer(s)
--kmax [KMAX] : Maximum length of k-mer(s)
--fmin [FMIN] : Minimum number of features to identify
--fmax [FMAX]: Maximum number of features to identify
--version : Show program's version number and exit
```

## Examples

### Training mode example :

#### Command :

```Bash
python -W ignore Main.py -t -f Data/HIVGRPCG/data.fa -c Data/HIVGRPCG/class.csv --kmin 5 --kmax 10 --fmin 10 --fmax 25 --threshold 1 -k ListOfIdentifiedKmers.txt
```

#### Description :

This command will allow to extract at least 10 features (--fmin 10) and at most 25 features (--fmax 25) based on k-mers with a minimum and maximum length of respectively 5 and 10 (--kmin 5, --kmax 10). <br/>
These features will be extracted from the sequences of the fasta file (-f Data/HIVGRPCG/data.fa) whose labels are specified in the CSV file (-c Data/HIVGRPCG/class.csv). <br/>
The threshold (--threshold 1) to reduce the number of attributes is 1 (default value). <br/>
A prediction model will be generated (-t) and the extracted features saved in the file (-k ListOfIdentifiedKmers.txt).

### Evaluation mode example :

#### Command :

```Bash
python -W ignore Main.py -e -f Data/HIVGRPCG/data.fa -c Data/HIVGRPCG/class.csv -m Output/model.pkl
```

#### Description :

This command will allow to evaluate (-e) the model (-m Output/model.pkl) with the prediction of the sequences of the fasta file (-f Data/HIVGRPCG/data.fa) whose labels are specified in the CSV file (-c Data/HIVGRPCG/class.csv). <br/>
The results will be given in the Evaluation.txt file of folder Ouput.

### Prediction  mode example :

#### Command :

```Bash
python -W ignore Main.py -p -f Data/HIVGRPCG/data.fa -m Output/model.pkl
```

#### Description :

This command will allow to predict (-p) the classes of the unknown sequences of the file (-f Data/HIVGRPCG/data.fa) based on the model (-m Output/model.pkl). <br/>
The results will be given in the Prediction.txt file of folder Ouput.


## Input Files

### FASTA : Contains the sequences in fasta format

```
>Id Description <br/>
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC <br/>
>Id Description <br/>
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC <br/>
>Id Description <br/>
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC <br/>
>Id Description <br/>
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC <br/>
>Id Description <br/>
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC <br/>
```

### CSV :  Contains the classes associated with each sequence
```
>Id,Class <br/>
>Id,Class <br/>
>Id,Class <br/>
>Id,Class <br/>
>Id,Class <br/>
```
### MODEL : Contains a prediction model in pkl format

For more detailed examples see the data sets in the Data folder        


## Output Files

- Analysis.png : Show the decision graph of the optimal set of k-mers by CASTOR algorithm (Training mode) <br/>
- model.pkl : Prediction model generated by CASTOR-KRFE (Training mode) <br/>
- Kmers.txt : File of the extracted k-mers list (Name can be change in parameter) <br/>
- Evaluation.txt : Results file of the evaluation a model with a dataset of labeled sequences (Evaluation mode) <br/>
- Prediction.txt : Results file of the prediction of unknown genomic sequences (Prediction mode) <br/>


## Cite CASTOR-KRFE

* Dylan Lebatteux, Amine M. Remita and Abdoulaye Banire Diallo (2018) *Toward an Alignment-Free Method for Feature Extraction and Accurate Classification of Viral Sequences*. Joint ICML and IJCAI Workshop on Computational Biology (WCB'18)


## References

* Scikit-learn
Pedregosa, Fabian, et al. "Scikit-learn: Machine learning in Python."
Journal of machine learning research 12.Oct (2011): 2825-2830.
Website : https://scikit-learn.org/

* Biopython
Cock, Peter JA, et al. "Biopython: freely available Python tools for computational molecular biology and bioinformatics."
Bioinformatics 25.11 (2009): 1422-1423.
Website : https://biopython.org/

