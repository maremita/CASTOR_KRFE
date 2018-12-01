def cross_validation(training_data, best_k_mers, best_k_length, data):
	# Imports
	import Matrices
	import Classifiers
	from sklearn.metrics import accuracy_score
	from sklearn.metrics import confusion_matrix
	from sklearn.metrics import classification_report
	from sklearn.model_selection import StratifiedKFold
	from sklearn.model_selection import cross_val_predict

	# Generate  matrices
	X, y = Matrices.generateMatrice(training_data, best_k_mers, best_k_length)

	# Realize evaluation with CV + Classifier + Metrics
	clf = Classifiers.svm()
	skf = StratifiedKFold(n_splits = 10, shuffle = False, random_state = None)
	y_pred = cross_val_predict(clf, X, y, cv = skf, n_jobs = 4)
	
	# Print results
	print("\nClassification report of model evaluation\n")
	print(classification_report(y, y_pred, digits = 3))
	print("Accuracy :", accuracy_score(y, y_pred) * 100, "%\n")
	print("Confusion matrix \n", confusion_matrix(y, y_pred))


def prediction(training_data, testing_data, best_k_mers, best_k_length):
	# Imports
	import Matrices
	import Classifiers
	from sklearn.externals import joblib
	from sklearn.metrics import accuracy_score
	from sklearn.metrics import confusion_matrix
	from sklearn.metrics import classification_report
	from sklearn.model_selection import StratifiedKFold

	# Generate matrices
	X_train, y_train = Matrices.generateMatrice(training_data, best_k_mers, best_k_length)
	X_test, y_test = Matrices.generateMatrice(testing_data, best_k_mers, best_k_length)

	# Implement and fit classifier
	clf = Classifiers.svm()
	clf.fit(X_train, y_train)

	# Save model
	joblib.dump(clf, 'Output/model.pkl') 
	
	# Load model
	clf = joblib.load('Output/model.pkl')

	# Realize prediction
	y_pred = clf.predict(X_test)

	# Print results
	print("\nClassification report of prediction\n")
	print(classification_report(y_test, y_pred, digits = 3))
	print("Accuracy :", accuracy_score(y_test, y_pred) * 100, "%\n")
	print("Confusion matrix \n", confusion_matrix(y_test, y_pred))


	f = open("Output/Prediction.txt", "w")
	f.write("Sequence id, Predicted class \n");
	for i, d in enumerate(testing_data): f.write(d[0] + ", " + y_pred[i] + "\n");
	f.close()



