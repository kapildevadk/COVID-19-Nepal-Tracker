# COVID-19-Nepal-Tracker
COVID-19-Nepal-Tracker: This repository contains the script to scrap Nepal's data of COVID19 from the Data-centric API of Nepal.
The data is collected from MOHP, publicly available information and data API sources. The dataset are updated only based on official government announcements and extracts data related to Nepal from the daily reports. 

1. Nepal_Covid-19_Time-Series_API.py : For Covid-19 cases by Local levels/Districts of Nepal (Time series database) with Lat & Lon of districts and local levels.
2. COVID-19-Nepal_fromWiki.py : For Covid-19 Updates of Nepal, contains total identified cases, dealths and recovery district wise with Lat & Lon from wikipedia.
3. Nepal_Covid-19_Cases_by-District.py : For Covid-19 cases by Districts of Nepal with Lat & Lon.
4. Nepal_Covid-19_Cases_by-Municipality.py : For Covid-19 cases by Local levels (mun) of Nepal with Lat & Lon.

The data in csv/xlsx can be visualized by geopandas, Qgis, ArcGIS, R,...
Every attempt is done in making data accurate. If you find any inconsistency, please report.

Created on Wed Aug 12 17:31:56 2020
@author: Kapildev Adhikari

[Data-centric API linked: 'https://github.com/postmanlabs/postman-code-generators']
##'https://data.nepalcorona.info/api/v1/districts'
##'https://data.nepalcorona.info/api/v1/municipals'
##'https://data.nepalcorona.info/api/v1/covid'
##'https://covid19.mohp.gov.np/covid/api/confirmedcases'
##'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'
