# DataScience-Template

## load Data

## cleanse Data

1. Find out which values are in each column
`for col in df:
    print(df[col].unique())`
1.1. Get an overview about missing data
`df.info()`
1.3. Find out the type of data in the column: categorial, ordinal, numerical, int, float, date, mixed, string, unique
2. Mark missing values
`df.replace('something',np.NaN, inplace=True)`
3. Normalize values
e.g. 'm', 'M' and 'male' should all be 'm'
`df['Sex'].replace('m','male', inplace=True)`
Think about what todo with e.g. an age with 'nan': fill in a zero? keep a nan? put in the average? ignore this row?
`df.replace(np.NAN,df['Age'].mean(), inplace=True)`
or
`df_missing['Age'] = df_missing['Age'].fillna(df_missing['Age'].mean())`
4. create dummy variables
5. remove unneccassary columns
df.drop(['PassengerId', 'Ticket', 'Cabin'], axis=1)

## descriptive statistics

`df.describe()`
look out for extremes, unrealistic values
e.g. an Age of 300 would be unrealistic -> exclude it or mark it as nan?

## single column analytics

look at e.g. boxplots

## correlations

correlate single columns with y / the success indicator
correlate every two columns with each other
remeber to remove NAN and things like that first
`ttest_something = stats.ttest_ind( df['Age'],  df['Pclass'])`
