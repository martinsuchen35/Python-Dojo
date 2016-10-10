def classify(features_train, labels_train):

    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)

    return clf

def NBAccuracy1(features_train, labels_train, features_test, labels_test):
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    accuracy = clf.score(features_test, labels_test)

    return accuracy

def NBAccuracy2(features_train, labels_train, features_test, labels_test):
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)

    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)

    return accuracy