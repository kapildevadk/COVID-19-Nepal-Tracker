# -*- coding: utf-8 -*-
"""
Created on Friday Aug 7 15:042:06 2020
@author: Kapildev Adhikari
https://twitter.com/kapil_adhikari_
www.youtube.com/c/FOSS%20Geo-Nepal
"""

"""
#Wikipedia Link for data
##wiki_url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
##open_api = 'https://data.nepalcorona.info/api/v1/districts'
# url__ = requests.get('https://covid19.mohp.gov.np/covid/api/confirmedcases')
# url__ = requests.get('https://covidapi.naxa.com.np/api/v1/stats/')
# url_api = requests.get("https://covid19.mohp.gov.np/covid/api/confirmedcases")
# dist_api = url_api.json()
# pd.DataFrame(dist_api)
# df_api = pd.json_normalize(dist_api)
# df_api.columns = df_api.columns.map(lambda x: x.split(".")[-1])
timeline_url = https://covid-dataset-by-bikram.herokuapp.com/CoronaNepal.csv
http://covidinfonepal.com/
"""

import pandas as pd
import requests
# import csv
# import json
# from pandas.io.json import 
import logging

#Step 1 Data Collection
#url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic'
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
req = requests.get(url, timeout=10)
data_list = pd.read_html(req.text)
df1 = data_list[3]

#Step 2 Data Cleaning
#Issue 1 Column Names
df1.columns = ['District','col1','Total Cases','Total Recoveries','Total Deaths']

#Issue 2 Extra Columns
df1 = df1[['District','Total Cases','Total Recoveries','Total Deaths']]

#Issue 3 Extra Rows
last_idx = df1.index[-1]
df1 = df1.drop([0, 15, 24, 38, 50, 63, 74, last_idx, last_idx-1])
#Issue 4 Inconsistent District Name

# df1['District'] = df1['District'].str.replace('\[.*\]','')
# #Issue 5 Extra Value ("No Data") in Column 4
df1['Total Cases'] = df1['Total Cases'].str.replace('No data','0')
df1['Total Recoveries'] = df1['Total Recoveries'].str.replace('No data','0')
df1['Total Deaths'] = df1['Total Deaths'].str.replace('No data','0')

#Issue 6 Wrong Data Type
df1['Total Cases'] = pd.to_numeric(df1['Total Cases'])
df1['Total Recoveries'] = pd.to_numeric(df1['Total Recoveries'])
df1['Total Deaths'] = pd.to_numeric(df1['Total Deaths'])
df1.insert(0, 'S.N.', range(1, 1 + len(df1)))

#get data from api url
url2 = requests.get('https://data.nepalcorona.info/api/v1/districts')
dist = url2.json()

#read through DataFrame
pd.DataFrame(dist)
df2 = pd.json_normalize(dist)

#manage json data as table view
df2.columns = df2.columns.map(lambda x: x.split(".")[-1])
#assign columns
df2 = df2[['title','province','coordinates']]

#convert int to str
df2.coordinates = df2.coordinates.astype(str)

#remove square bracket from pandas dataframe
df2['coordinates'] = df2['coordinates'].str.strip('[]')

## new data frame with split value columns of 'lat'&'lon'
df2[['lat','lon']]=df2.coordinates.str.split(",",expand=True)

#Set the header for df2
df2 = df2[['title','province','lat','lon']]

#covert str to int again
df2['lat'] = pd.to_numeric(df2['lat'])
df2['lon'] = pd.to_numeric(df2['lon'])

#RENAME SPECIFIC COLUMNS
df2.rename(columns={'title': 'District', 'province': 'Province'}, inplace=True)


df3=pd.merge(df1, df2, on='District')
df3=df3[['S.N.','Province','District','Total Cases','Total Recoveries','Total Deaths','lat','lon']]
#Step 3 Export The Data
logging.info("Saving new data to CSV.")
df3.to_csv(r'Nepal_covid-19_dataset_wiki.csv', index=False, header=True)