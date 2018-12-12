#data=pd.read_csv("data.csv")
import pandas as pd
from urllib.request import urlopen
from pgmpy.models import BayesianModel
names="A,B,C,D,E,F,G,H,I,J,K,L,M,RESULT"
names=names.split(",")
data=pd.read_csv(urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"),names=names)
data.head()
model=BayesianModel([("A","B"),("B","C"),("C","RESULT")])
model.fit(data)
from pgmpy.inference import VariableElimination
infer=VariableElimination(model)
q=infer.query(variables=["RESULT"],evidence={"A":22})
print(q["RESULT"])