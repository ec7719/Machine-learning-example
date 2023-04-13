import sklearn
from sklearn.tree import DecisionTreeClassifier 
import pandas as pd
boo=pd.read_csv("music.csv")
x=boo
x=boo.drop(columns=['genre'])
y=boo['genre']
model=DecisionTreeClassifier()
model.fit(x,y)
predictions=model.predict([[22,0]])
print(predictions)