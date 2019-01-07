from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)


from sklearn.model_selection import KFold
kf = KFold(n_splits=2) 
kf.get_n_splits(X)


from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
loo.get_n_splits(X)


from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics
scores = cross_val_score(model, df, y, cv=6)



from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
hyperparameters = dict()
clf = GridSearchCV(model, hyperparameters, cv=5, verbose=0)
clf = RandomizedSearchCV(model, hyperparameters, cv=5, verbose=0)
best_model = clf.fit(X, Y)
print('Best Parameters',clf.best_params_)


from hyperopt import hp, tpe, fmin
