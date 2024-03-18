# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("Titanic-Dataset.csv")
df['Age'] = df['Age'].fillna(23.8)

df['Sex'] = df['Sex'].replace({'male': 0 ,'female':1})
df.drop(columns=['Embarked','Cabin','Fare','Ticket','PassengerId'],inplace=True)

df.drop(columns=['Name'],inplace=True)


correlation = df.corr()
correlation['Survived'].sort_values(ascending=False)
X = df.drop(['Survived'],axis=1)
y = df['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.3)


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

algo = DecisionTreeClassifier(criterion='gini',random_state=100,max_depth=5,min_samples_leaf=5)
a = algo.fit(X_train,y_train)

pickle.dump(a,open('model.pkl','wb')) 




