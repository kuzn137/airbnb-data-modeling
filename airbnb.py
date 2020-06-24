# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:44:34 2020

@author: kuzn137
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
dfb=pd.read_csv("listings_seattle.csv")
print(dfb.head())
most_missing_cols = set(dfb.columns[abs(~dfb.isnull().sum())>0.75*len(dfb)])
print(most_missing_cols)
nulls = set(dfb.columns[dfb.isnull().any()])#Provide a set of columns with 0 missing values.
print(nulls)
most_missing_cols = set(dfb.columns[abs(~dfb.isnull().sum())>0.75*len(dfb)])
print(most_missing_cols)
df=dfb[['id', 'cancellation_policy']].groupby(['cancellation_policy']).count()
(df/dfb.shape[0]).plot(kind="bar");
plt.title("instant bookable");
dfb=dfb.loc[~dfb['monthly_price'].isnull()]
dfb['monthly_price']=dfb['monthly_price'].apply(lambda x: float(x[1:].replace(',','')))
#dfb['monthly_price']=dfb['monthly_price'].apply(lambda x: float(x))
print(dfb['monthly_price'])

colf=np.array(dfb.select_dtypes('float').columns)
print(colf)
corr = dfb[colf].corr()
print(dfb.loc[dfb['monthly_price'].isnull(), ['monthly_price']])
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


#col
#corr = df[col[1:]].corr()
# Generate a mask for the upper triangle
#mask = np.zeros_like(corr, dtype=np.bool)
#mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
#f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
#cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
#sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
#            square=True, linewidths=.5, cbar_kws={"shrink": .5})