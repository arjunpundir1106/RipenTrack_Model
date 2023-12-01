# -*- coding: utf-8 -*-
"""Capstone (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NupCWJz50ctEzur6mg3TrxF4QILdwSQV
"""

!pip install pycaret &> /dev/null
print ("Pycaret installed sucessfully!!")

from pycaret.utils import version
version()

import pandas as pd

dataset = pd.read_csv("/content/training_dataset.csv")

pip install markupsafe==2.0.1

dataset.head()

from pycaret.classification import *
s = setup(data=dataset, target='Class')

# Other Parameters:
# train_size = 0.7
# data_split_shuffle = False

cm = compare_models()

""" Model performance using "Normalization"
"""

s = setup(data=dataset, target='Class',
      normalize = True, normalize_method = 'minmax')
cm = compare_models()
regression_results = pull()
print(regression_results)

#normalize_method = {zscore, minmax, maxabs, robust}

"""Model performance using "Outlier Removal"
"""

setup(data=dataset, target='Class',
      remove_outliers = True, outliers_threshold = 0.05)
cm = compare_models()

"""Model performance using "Transformation"
"""

setup(data=dataset, target='Class',
      transformation = True, transformation_method = 'yeo-johnson')
cm = compare_models()

setup(data=dataset, target='Class',
      remove_outliers = True, outliers_threshold = 0.05,
      transformation = True, transformation_method = 'yeo-johnson')

cm = compare_models()

""" Model performance using "PCA" and normalisation showed maximum accuracy"""

setup(data=dataset, target='Class',
      pca = True, pca_method = 'linear',normalize = True, normalize_method = 'minmax')
cm = compare_models()

"""#EXTRA TREES"""

setup(data=dataset, target='Class',
      pca = True, pca_method = 'linear',normalize = True, normalize_method = 'minmax')

etModel = create_model('et')
# Explore more parameters

"""SVM Model

"""

setup(data=dataset, target='Class',
      pca = True, pca_method = 'linear',normalize = True, normalize_method = 'minmax')

SVMmodel = create_model('svm')
# Explore more parameters

"""# Naive Bayes

"""

setup(data=dataset, target='Class',
      pca = True, pca_method = 'linear',normalize = True, normalize_method = 'minmax')

nbModel = create_model('nb')

"""#Decision Tree

"""

setup(data=dataset, target='Class',
      pca = True, pca_method = 'linear',normalize = True, normalize_method = 'minmax')

dtModel = create_model('dt')

"""#stack 3 models"""

# Ensemble models
ensemble_model = stack_models(estimator_list=[dtModel, nbModel,SVMmodel])

# Evaluate ensemble model
evaluate_model(ensemble_model)

"""Blend Models"""



"""Stacked Models"""

sm = save_model(ensemble_model, 'Ensemble_Model_Final')

newdataset = pd.read_csv("/content/testing_dataset.csv")

newPredictions = predict_model(ensemble_model, data = newdataset)
newPredictions

newPredictions.to_csv("NewPredictions.csv", index=False)

from google.colab import files
files.download('NewPredictions.csv')

from sklearn.metrics import accuracy_score

# Load the PyCaret trained ensemble model
ensemble_model = load_model('Ensemble_Model_Final')  # Replace 'your_ensemble_model_name' with the actual name

# Make predictions on the testing dataset
newPredictions = predict_model(ensemble_model, data=newdataset)

# Evaluate the model on the testing dataset
accuracy = accuracy_score(newPredictions['Class'], newPredictions['Class'])  # Replace 'target_column' with the actual target column name

# Print the accuracy
print(f"Accuracy on the testing dataset: {accuracy}")

# Save predictions to a CSV file
newPredictions.to_csv("NewPredictions.csv", index=False)

# Download the CSV file
from google.colab import files
files.download('NewPredictions.csv')

"""Plots"""

plot_model(ensemble_model, plot='confusion_matrix')

"""Plot the "learning curve"
"""

plot_model(ensemble_model, plot='learning')

"""Plot the "AUC Curve" (Area Under the Curve)"""

plot_model(ensemble_model, plot='auc')

"""Plot the "Decision Boundary"
"""

plot_model(ensemble_model, plot='boundary')

