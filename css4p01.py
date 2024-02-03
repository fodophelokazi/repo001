# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:06:19 2024

@author: chiya
"""

import pandas as pd
import seaborn as sns
import numpy
import matplotlib.pyplot as plt

#creating a dataframe 
df = pd.read_csv("movie_dataset.csv")
df.head()

#drop all the null values
df = df.dropna(axis=0)
print(df)


#check duplicated dataset
dup_df = df.duplicated().any()
print(dup_df)

#check the statistics of all 
print(df.describe(include='all'))
print(df.info)

print(df.columns)

#check datset having the rate of atleast 8.0
print(df[df['Rating']>=8.0]['Rating'])

#the highest avarage rating year
print(df.groupby('Year')['Rating'].mean().sort_values(ascending=False))

sns.barplot(x='Year' ,y='Rating' ,data=df)
plt.title("AVERAGE RATE BY YEAR")
plt.show()


print(df.columns)

#movies realesed in 2016
print(df['Year'].value_counts())

#print(df['Genre'].value_counts())

#highest rated movie
print(df.groupby('Title')['Rating'].mean().sort_values(ascending=False))

sns.barplot(x='Rating' ,y='Title' ,data=df)
plt.title("RATED MOVIE BY YEAR")
plt.show()

print(df.columns)

#movies directed by Christopher
print(df[df['Director']=='Christopher Nolan']['Rating'])


#revevenues
#print(df.groupby('Metascore')['].mean().sort_values(ascending=False))

#print(df[df['Revenue (Millions)']>=2015:2017]['Revenue (Millions)']).mean.sort_values(ascending=False)

#number 11
print(df['Genre'].value_counts())

list1=[]
for value in df['Genre']:
      list1.append(value.split(';'))
      print(list1)
one_list=[]
for item in list1:
    for item1 in item:
       one_list.append(item1)
print(one_list)    

unique_list=[]
for item in one_list:
     if item not in unique_list:
         unique_list.append(item)
         
print(len(unique_list)) 
      
#revevenues
#print(df.groupby('Metascore')['].mean().sort_values(ascending=False))

#print(df[df['Revenue (Millions)']>=2015:]['Revenue (Millions)']).mean.sort_values(ascending=False)

print(df['Actors'])
list2=[]
for value in df['Actors']:
      list2.append(value.split(';'))
      print(list2)
second_list=[]
for item in list2:
    for item2 in item:
       one_list.append(item2)
print(second_list)    

common_list=[]
for item in second_list:
     if item not in common_list:
         common_list.append(item)
print(common_list)         
      
"""
sns.barplot(x='Year' ,y='Runtime (Minutes)' ,data=df)
plt.title("percentage increase--")
plt.show()
"""
