import numpy as np
import pandas as pd
from scipy import stats

## load Data
df = pd.read_csv('./train.csv')
## cleanse Data
for col in df:
    print(df[col].unique())
df.replace('something',np.NaN, inplace=True)


## combine Data

## descriptive Analysis

## single column Analysis

## correlations
correlation_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df_corr = pd.DataFrame()
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
## machine learning

## 