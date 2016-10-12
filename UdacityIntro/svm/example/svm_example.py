from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[2., 2.]]))

print "\nget support vectors"
print(clf.support_vectors_)

print "\nget indices of support vectors"
print(clf.support_)

print "\nget number of support vectors for each class"
print(clf.n_support_)

