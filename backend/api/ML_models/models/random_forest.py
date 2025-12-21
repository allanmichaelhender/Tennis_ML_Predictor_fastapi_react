import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
import  joblib


dataframe = pd.read_csv("ML_ready_data.csv", index_col=0)
                        
X = dataframe.drop(columns=["player1_win"])
y = dataframe['player1_win']
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

rf = RandomForestClassifier(n_estimators=250, max_depth=5)
print('Random Forest parameters:')
rf_params = rf.get_params()
print(rf_params)

rf.fit(x_train,y_train)
y_pred = rf.predict(x_test)
rf_accuracy = rf.score(x_test,y_test)
print('Test set accuracy:')

print(rf_accuracy)

joblib.dump(rf, 'random_forest_model.joblib')