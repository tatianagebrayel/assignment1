# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I_xve1a_IJ4VdhoY42HQrZAmwxSydo2-

**Importing From FAO STAT Lebanese Population from 1987 till 2021  **
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

import io
df2 = pd.read_csv(io.BytesIO(uploaded['FAOSTAT_data_en_12-5-2022.csv']))
# Dataset is now stored in a Pandas Dataframe

df2.rename(columns = {'Element Code':'gender'}, inplace = True)

df2.drop('Domain Code', axis=1, inplace=True)

df2.drop("Domain", axis=1, inplace=True)

df2.drop('Area Code (M49)', axis=1, inplace=True)

df2.drop("Element", axis=1, inplace=True)

df2.drop("Item Code", axis=1, inplace=True)

df2.drop("Item",axis=1, inplace=True)

df2.drop("Year Code",axis=1, inplace=True)

df2.drop('Note', axis=1, inplace=True)

df2.head()

len(df2)

def prepossessing(df2):
  for index in range(0,len(df2)): 
      if(df2.at[index,'Element Code'] == 512):
        df2.at[index,'gender']= "Male"
      else :  df2.at[index,'gender']="female"

  return df2

df2.head()

df2.at[1,'gender']

df2.loc[df2["gender"] == 512, "gender"] = "Male"

df2.loc[df2["gender"] == 513, "gender"] = "female"

df2.head()

df2

"""**Gender Comparing demographics**"""

# splitting dataframe by groups
# grouping by particular dataframe column
grouped = df2.groupby(df2.gender)
df_male = grouped.get_group("Male")
df_male

df_female = grouped.get_group("female")

df_female

import matplotlib.pyplot as plt

df_male.plot(x='Year', y='Value', kind='bar')
plt.show()

df_female.plot(x='Year', y='Value', kind='bar')
plt.show()

import seaborn as sns

sns.lineplot(x='Year', y='Value', hue='gender', data=df2)

"""** as we see that:
1- populatin density is decreasing in last years due to many factors : COVID-Economic Crises- migration...
2- correlation between genders , both decreased as we can conclude that boys and girls are leaving lebanon...
3-  that nb of girls is always greater then boys even when population density is increasing or decreasing**
"""

male2021=df_male['Value'].values[-1:]
male2021

female2021=df_female['Value'].values[-1:]
female2021

population2021= male2021+female2021
population2021

percentagemale2021=(male2021/population2021)*100
percentagemale2021

percentagefemale2021=(female2021/population2021)*100
percentagefemale2021

"""%female > % male"""

df_male["Value"].describe()

df_female["Value"].describe()

df_male.boxplot( column =['Value'], grid = False)

df_female.boxplot( column =['Value'], grid = False)

df2.boxplot(by ='gender', column =['Value'], grid = False)

import seaborn as sns

corelation = df_male.corr()

sns.heatmap(corelation, xticklabels=corelation.columns,yticklabels=corelation.columns,annot=True)

sns.pairplot(df_male)

sns.pairplot(df_female)