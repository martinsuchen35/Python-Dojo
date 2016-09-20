import numpy as np

features_train = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
labels_train = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)
print(clf.predict([[-0.8, -1]]))
print(clf.predict([[3, 4]]))

clf_pf = GaussianNB()
clf_pf.partial_fit(features_train, labels_train, np.unique(labels_train))
print(clf_pf.predict([[-0.8, -1]]))
print(clf.predict([[3, 4]]))
