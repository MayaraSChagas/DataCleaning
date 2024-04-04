# -*- coding: utf-8 -*-
"""DataCleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3lVuF7GMBf3ZJlN-vvQSh-7L3vRv-K7
"""

import pandas as pd

titanic = pd.read_csv("/content/drive/MyDrive/10-31 - Limpeza de Dados em um Dataset Real-20240404T002847Z-001/10-31 - Limpeza de Dados em um Dataset Real/train.csv")
display(tabela)

titanic.shape

titanic.info()

titanic.describe()

titanic.nunique()

titanic.isnull().sum()

titanic[titanic.Embarked.isnull()]

titanic.loc[titanic.Embarked.isnull(),'Embarked'] = 'S'

titanic[titanic.Age.isnull()]

titanic.Age.describe()

titanic.Age.plot.box();

titanic.Age.plot.hist(bins=20);

titanic.groupby('Pclass')['Age'].median()

titanic.groupby(['Pclass','Sex'])['Age'].median()

titanic['Age_Check1'] = titanic.groupby(['Pclass','Sex'])['Age'].transform('median')

titanic.head(3)

titanic['Age_Check1'] =titanic.Age.fillna(titanic.groupby(['Pclass','Sex'])['Age'].transform('median'))

titanic.Cabin.value_counts()

#Eliminamos a coluna cabine pois ela não faz sentido
titanic = titanic.drop('Cabin',axis=1)

titanic.nunique()

titanic = titanic.drop(['PassengerId','Ticket'],axis=1)

titanic.head(5)

titanic = titanic.drop('Age',axis=1)

titanic.info()