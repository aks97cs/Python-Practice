from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
# print(digits)
# print(digits.data)
print(digits.target)
clf = svm.SVC(gamma=0.001, C=100.)
print(clf)
clf.fit(digits.data[:-1], digits.target[:-1])  
# SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
#   decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
#   max_iter=-1, probability=False, random_state=None, shrinking=True,
#   tol=0.001, verbose=False)
print(clf.predict(digits.data[-1:]))
# print(array[8])