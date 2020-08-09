# -*- coding: utf-8 -*-
"""
Created on Friday Aug 7 15:042:06 2020
@author: Kapildev Adhikari
https://twitter.com/kapil_adhikari_
https://www.youtube.com/c/FOSSGeoNepal
"""

"""
#Wikipedia Link for data
##wiki_url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
url = http://covidinfonepal.com/
url = https://covid-19-nepal-2019.herokuapp.com/
"""

import pandas as pd
import requests
# import csv
# import json
# from pandas.io.json import 
import logging

#Step 1 Data Collection
url = 'https://covid-19-nepal-2019.herokuapp.com/'
req = requests.get(url, timeout=50)
data_list = pd.read_html(req.text)
df1 = data_list[0]

df1 = df1[['S.N','District','Total Cases','Active Cases','Recovered','Deaths']]
#RENAME SPECIFIC COLUMNS
df1.rename(columns={'Recovered': 'Total Recovered', 'Deaths': 'Total Deaths'}, inplace=True)


#get data from api url
url2 = requests.get('https://data.nepalcorona.info/api/v1/covid')
dist = url2.json()

#read through DataFrame
pd.DataFrame(dist)
df2 = pd.json_normalize(dist)

#manage json data as table view
df2.columns = df2.columns.map(lambda x: x.split(".")[-1])
#assign columns
df2 = df2[['id','province','district','municipality','reportedOn','gender','age','coordinates','currentState','isReinfected','recoveredOn','deathOn']]

#convert int to str
df2.coordinates = df2.coordinates.astype(str)

#remove square bracket from pandas dataframe
df2['coordinates'] = df2['coordinates'].str.strip('[]')

## new data frame with split value columns of 'lat'&'lon'
df2[['Latitude','Longitude']]=df2.coordinates.str.split(",",expand=True)

#Set the header for df2
df2 = df2[['id','province','district','municipality','reportedOn','gender','age','currentState','isReinfected','recoveredOn','deathOn','Latitude','Longitude']]

#covert str to int again
df2['id'] = pd.to_numeric(df2['id'])
df2['Latitude'] = pd.to_numeric(df2['Latitude'])
df2['Longitude'] = pd.to_numeric(df2['Longitude'])

df2.to_csv(r'Nepal_covid-19_timeline.csv', index=False, header=True)

# #RENAME SPECIFIC COLUMNS
# df2.rename(columns={'title': 'District', 'province': 'Province'}, inplace=True)

# df3=pd.merge(df1, df2, on='District')
# df3=df3[['S.N','Province','District','Total Cases','Active Cases','Total Recovered','Total Deaths','lat','lon']]
# #Step 3 Export The Data
# logging.info("Saving new data to CSV.")
# df3.to_csv(r'Nepal_covid-19_dataset_simply.csv', index=False, header=True)

# def foo():
#     f = open("Nepal_covid-19_dataset_simply.csv")
#     f.close()