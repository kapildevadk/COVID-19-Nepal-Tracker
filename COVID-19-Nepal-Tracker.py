# -*- coding: utf-8 -*-
"""
Created on Friday Aug 7 15:042:06 2020
@author: Kapildev Adhikari
https://twitter.com/kapil_adhikari_
https://www.youtube.com/c/FOSSGeoNepal
"""

"""
##wiki_url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
##url = https://covid-19-nepal-2019.herokuapp.com/
##open_api = 'https://data.nepalcorona.info/api/v1/districts'
##url_api = 'https://covid19.mohp.gov.np/covid/api/confirmedcases'
"""

import pandas as pd
import requests
import logging

#Data Collection
url = 'https://covid-19-nepal-2019.herokuapp.com/'
req = requests.get(url, timeout=50)
data_list = pd.read_html(req.text)
df1 = data_list[0]

#cols
df1 = df1[['S.N','District','Total Cases','Active Cases','Recovered','Deaths']]

#RENAME SPECIFIC COLUMNS
df1.rename(columns={'Recovered': 'Total Recovered', 'Deaths': 'Total Deaths'}, inplace=True)

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
df3=df3[['S.N','Province','District','Total Cases','Active Cases','Total Recovered','Total Deaths','Latitude','Longitude']]

#Export The Data
logging.info("Saving new data to CSV.")
df3.to_csv(r'Nepal_covid-19_dataset.csv', index=False, header=True)