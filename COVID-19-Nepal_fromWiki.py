# -*- coding: utf-8 -*-
"""
Created on Friday Aug 7 15:042:06 2020
@author: Kapildev Adhikari
https://twitter.com/kapil_adhikari_
https://www.youtube.com/c/FOSSGeoNepal
"""

"""
##url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic'
##wiki_url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
##open_api = 'https://data.nepalcorona.info/api/v1/districts'
##url_api = 'https://covid19.mohp.gov.np/covid/api/confirmedcases'
"""

import pandas as pd
import requests
import logging

#Step 1 Data Collection
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
req = requests.get(url, timeout=10)
data_list = pd.read_html(req.text)
df1 = data_list[3]

#Step 2 Data Cleaning
#Issue 1: Column Names
df1.columns = ['District','col1','Total Cases','Total Recoveries','Total Deaths']

#Issue 2: exclude extra cols and set cols.
df1 = df1[['District','Total Cases','Total Recoveries','Total Deaths']]

#Issue 3: Extra Rows
last_idx = df1.index[-1]
df1 = df1.drop([0, 15, 24, 38, 50, 63, 74, last_idx, last_idx-1])

#Issue 4: Extra Value ("No Data") in Column 4
df1['Total Cases'] = df1['Total Cases'].str.replace('No data','0')
df1['Total Recoveries'] = df1['Total Recoveries'].str.replace('No data','0')
df1['Total Deaths'] = df1['Total Deaths'].str.replace('No data','0')

#Issue 5: Wrong Data Type
df1['Total Cases'] = pd.to_numeric(df1['Total Cases'])
df1['Total Recoveries'] = pd.to_numeric(df1['Total Recoveries'])
df1['Total Deaths'] = pd.to_numeric(df1['Total Deaths'])

#Issue 6: assign row number
df1.insert(0, 'S.N.', range(1, 1 + len(df1)))

#get district database from github repo
raw_url='https://raw.githubusercontent.com/kapildevadk/COVID-19-Nepal-Tracker/master/Centroids_districts_lat-lon.csv'
df2 = pd.read_csv(raw_url, index_col=0)

#Set the header for df2
df2 = df2[['District','Province','Latitude','Longitude']]

#if need, convert string to number
df2['Latitude'] = pd.to_numeric(df2['Latitude'])
df2['Longitude'] = pd.to_numeric(df2['Longitude'])

#merge dataframes by attribute 
df3=pd.merge(df1, df2, on='District')

#set the final dataframe with headers
df3=df3[['S.N.','Province','District','Total Cases','Total Recoveries','Total Deaths','Latitude','Longitude']]

#Step 3 Export The Data
logging.info("Saving new data to CSV.") 
df3.to_csv(r'Nepal_covid-19_dataset_wiki.csv', index=False, header=True) 