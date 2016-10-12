#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
#sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#########################################################
# USE SVM
from sklearn.svm import SVC
clf = SVC(kernel="linear")

t2 = time()
clf.fit(features_train, labels_train)
print "SVC training time:", round(time() - t2, 3), "s"

t3 = time()
pred = clf.predict(features_test)
print "SVC prediction time:", round(time() - t3, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print(accuracy)

# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# SVC training time: 156.289 s
# SVC prediction time: 16.326 s
# 0.984072810011
#########################################################

#########################################################
# One way to speed up an algorithm is to train it on a smaller training dataset.
# The tradeoff is that the accuracy almost always goes down when you do this.
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
# These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data.

t4 = time()
clf.fit(features_train, labels_train)
print "SVC training time:", round(time() - t4, 3), "s"

t5 = time()
pred = clf.predict(features_test)
print "SVC prediction time:", round(time() - t5, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print(accuracy)

# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# SVC training time: 0.092 s
# SVC prediction time: 0.951 s
# 0.884527872582
#########################################################
