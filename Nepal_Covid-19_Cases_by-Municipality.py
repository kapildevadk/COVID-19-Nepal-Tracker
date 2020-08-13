# -*- coding: utf-8 -*-
'...............................................................................'
"""
Created on Wed Aug 12 17:31:56 2020
@author: Kapildev Adhikari
https://www.youtube.com/c/FOSSGeoNepal
https://twitter.com/kapil_adhikari_
"""
'...............................................................................'
"""
Data-centric API linked: 'https://github.com/postmanlabs/postman-code-generators'
##'https://data.nepalcorona.info/api/v1/districts'
##'https://data.nepalcorona.info/api/v1/municipals'
##'https://data.nepalcorona.info/api/v1/covid'
##'https://covid19.mohp.gov.np/covid/api/confirmedcases'
"""
'...............................................................................'

import pandas as pd
import requests, json

# fetching DF
# loading data right from the source:
# create database of 77 Districts
url_dist = requests.get("https://data.nepalcorona.info/api/v1/districts")
dist = url_dist.json()

#read through DataFrame
pd.DataFrame(dist)
df1 = pd.json_normalize(dist)

#manage json data as table view
df1.columns = df1.columns.map(lambda x: x.split(",")[-1])

df1 = df1[['id','title_en','centroid.coordinates']]

# #RENAME SPECIFIC COLUMNS
df1.rename(columns={'centroid.coordinates': 'coordinates'}, inplace=True)

#convert int to str
df1.coordinates = df1.coordinates.astype(str)

#remove square bracket from pandas dataframe
df1['coordinates'] = df1['coordinates'].str.strip('[]')

## new data frame with split value columns of 'lat'&'lon'
df1[['Latitude_dist','Longitude_dist']]=df1.coordinates.str.split(",",expand=True)

#covert str to int again
df1['Latitude_dist'] = pd.to_numeric(df1['Latitude_dist'])
df1['Longitude_dist'] = pd.to_numeric(df1['Longitude_dist'])

#Set the header for df1
df1 = df1[['id','title_en','Latitude_dist','Longitude_dist']]

# #RENAME SPECIFIC COLUMNS
df1.rename(columns={'id': 'dis_code', 'title_en': 'dis_en'}, inplace=True)

# change df values Nawalparasi East as Nawalpur and Nawalparasi West as Parasi at index
df1.at[74, "dis_en"] = "Nawalpur" #Nawalparasi East
df1.at[75, "dis_en"] = "Parasi" #Nawalparasi West

# create database of all local levels of nepal
url_mun = requests.get("https://data.nepalcorona.info/api/v1/municipals/")
mun = url_mun.json()

#read through DataFrame
pd.DataFrame(mun)
df2 = pd.json_normalize(mun)

#manage json data as table view
df2.columns = df2.columns.map(lambda x: x.split(",")[-1])

df2 = df2[['id','type','title_en','district','centroid.coordinates']]

#RENAME SPECIFIC COLUMNS
df2.rename(columns={'id':'mun_id','centroid.coordinates': 'coordinates'}, inplace=True)

#convert int to str
df2.coordinates = df2.coordinates.astype(str)

#remove square bracket from pandas dataframe
df2['coordinates'] = df2['coordinates'].str.strip('[]')

## new data frame with split value columns of 'lat'&'lon'
df2[['Latitude_mun','Longitude_mun']]=df2.coordinates.str.split(",",expand=True)

#covert str to int again
df2['Latitude_mun'] = pd.to_numeric(df2['Latitude_mun'])
df2['Longitude_mun'] = pd.to_numeric(df2['Longitude_mun'])

#Set the header for df1
df2 = df2[['mun_id','type','title_en','Latitude_mun','Longitude_mun','district']]

df2['mun_en'] = df2['title_en'] + ' ' + df2['type']
#Set the header for df1
df2 = df2[['mun_id','mun_en','Latitude_mun','Longitude_mun','district']]

#get data from api url of "COVID-19 Nepal"
api_url = requests.get('https://data.nepalcorona.info/api/v1/covid')
covid = api_url.json()

#read through DataFrame
pd.DataFrame(covid)
df3 = pd.json_normalize(covid)

#manage json data as table view
df3.columns = df3.columns.map(lambda x: x.split(".")[-1])

#assign columns
df3['cases'] = 1
df3 = df3[['province','district','municipality','reportedOn','currentState','cases','gender','age']]

#RENAME SPECIFIC COLUMNS
df3.rename(columns={'municipality':'mun_id', 'district':'dis_code'}, inplace=True)

#replace nan value to 0
df3['age'] = pd.to_numeric(df3['age'], errors='coerce')
df3['age'] = df3['age'].fillna(0)

df6 = df3[['mun_id','reportedOn','cases']]
df6.pivot_table(index='reportedOn', columns='mun_id',aggfunc=sum)

df6 = df6.groupby(['mun_id','reportedOn']).sum().sum(
    level=['mun_id','reportedOn']).fillna(0).reset_index()

# merge df2 & df6
df7 = pd.merge(df6, df2, on='mun_id')

#RENAME SPECIFIC COLUMNS
df7.rename(columns={'district':'dis_code'}, inplace=True)

# merge df2 & df6
df8 = pd.merge(df7, df1, on='dis_code')

#To create Database of Municipality wise
df9 = df8[['mun_id','cases']]

df10 = df9.groupby(["mun_id"], as_index=False)[["cases"]].sum()

# merge df2 & df10
df_mun = pd.merge(df10, df2, on='mun_id')

#assign row number
df_mun.insert(0, 'S.N.', range(1, 1 + len(df_mun)))

#fianl cols
df_mun = df_mun[['mun_id','mun_en','cases','Latitude_mun','Longitude_mun']]

#export database
df_mun.to_csv(r'Nepal_Covid-19_by-Municipality.csv', index=False, header=True)