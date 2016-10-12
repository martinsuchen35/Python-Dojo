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

#########################################################
# USE SVM
# from sklearn.svm import SVC
# clf = SVC(kernel="linear")
#
# t2 = time()
# clf.fit(features_train, labels_train)
# print "SVC training time:", round(time() - t2, 3), "s"
#
# t3 = time()
# pred = clf.predict(features_test)
# print "SVC prediction time:", round(time() - t3, 3), "s"
#
# accuracy = accuracy_score(pred, labels_test)
# print(accuracy)
