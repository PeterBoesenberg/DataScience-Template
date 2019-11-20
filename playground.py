# text1 = "Ethics are built built right into the ideals and objectives of the United Nations"
# words = text1.split(' ')
# long_words = [w for w in words if len(w) > 3]
# unique_words = set(words)
# print([w for w in words if w.startswith('i')])


import nltk
#from nltk.book import *
# porter = nltk.PorterStemmer()
# testsentence = 'Das ist ein echt cooler Satz, der geht. Und jeder ging nach Hause.' 
# words = nltk.word_tokenize(testsentence)
# result = [porter.stem(t) for t in words]
# print(result)
# print(nltk.help.upenn_tagset('MD'))
#text15 = nltk.word_tokenize('Alice loves Bob')
import numpy as np 
import pandas as pd
from scipy import stats
df = pd.read_csv('./train.csv')
#print(df.columns)

df.replace(np.NAN,df['Age'].mean(), inplace=True)
df.drop(['PassengerId', 'Ticket', 'Cabin'], axis=1, inplace=True)
# for col in df:
#     print(df[col].unique())
print(df['Age'].unique())
#print(df)
correlation_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df_corr = pd.DataFrame()
# ttest_something = stats.ttest_ind( df['Age'],  df['Fare'])
# print(ttest_something)
for col in correlation_cols:
    df_corr[col]=[]
for col in correlation_cols:
    row = []
    for col2 in correlation_cols:
        col_pos = df_corr.columns.get_loc(col2)
        ttest_something = stats.ttest_ind( df[col],  df[col2])
        row.append(ttest_something.pvalue < 0.01)
    df_corr[col] = row
df_corr.index = df_corr.columns
print(df_corr)
