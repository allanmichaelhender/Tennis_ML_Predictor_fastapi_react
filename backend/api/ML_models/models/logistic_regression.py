from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform

dataframe = pd.read_csv("../data/new_data/ML_ready_data.csv", index_col=0)

                        
X = dataframe.drop(columns=["player1_win"])
y = dataframe['player1_win']
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

logistic_regr_pipeline = Pipeline([
    ("scalar", StandardScaler()), 
    ("regr", LogisticRegression(solver='saga', max_iter=1000))
])

parameters = {    
    'regr__C': loguniform(0.001, 1000),
    'regr__l1_ratio': [0, 1] 
}

clf = RandomizedSearchCV(logistic_regr_pipeline, parameters, n_iter=50, cv=5)
clf.fit(x_train, y_train)

best_pipeline = clf.best_estimator_
print("Best pipeline configuration: ", best_pipeline)
print("Best parameters found: ", clf.best_params_)

best_pipeline_score = best_pipeline.score(x_test, y_test)
print(f"Pipeline score on test data: {best_pipeline_score:.4f}")

joblib.dump(best_pipeline, 'logistic_regr_pipeline.joblib')