## COVID-19-Nepal-Tracker
COVID-19-Nepal-Tracker: This repository contains the script to scrap Nepal's data of COVID19 from the Data-centric API of Nepal.
The data is collected from MOHP, publicly available information and data API sources. The dataset are updated only based on official government announcements and extracts data related to Nepal from the daily reports. 

1. Nepal_Covid-19_Time-Series_API.py : For Covid-19 cases by Local levels/Districts of Nepal (Time series database) with Lat & Lon of districts and local levels.
2. COVID-19-Nepal_fromWiki.py : For Covid-19 Updates of Nepal, contains total identified cases, dealths and recovery district wise with Lat & Lon from wikipedia.
3. Nepal_Covid-19_Cases_by-District.py : For Covid-19 cases by Districts of Nepal with Lat & Lon.
4. Nepal_Covid-19_Cases_by-Municipality.py : For Covid-19 cases by Local levels (mun) of Nepal with Lat & Lon.

The data in csv/xlsx can be visualized by [Geopandas](https://geopandas.org/), [Qgis](https://qgis.org/en/site/), [ArcGIS](https://desktop.arcgis.com/en/), [R](https://www.r-project.org/), [Power BI](https://powerbi.microsoft.com/en-us/), [Tableau](https://www.tableau.com/products/desktop), [Matplotlib](https://matplotlib.org/)... 
Every attempt is done in making data accurate. If you find any inconsistency, please report.

## Requirements
1. Download and install [Anaconda packages](https://www.anaconda.com/) or 
2. Download and install [Python](https://www.python.org), 
   and install packages through [pip install](https://phoenixnap.com/kb/install-pip-windows) : 
   "[pip install pandas](https://pypi.org/project/pandas/)" &
   "[pip install spyder](https://pypi.org/project/spyder/)" In Windows command prompt.

## Maintainer
[Kapildev Adhikari](https://github.com/kapildevadk)

### API & links
[Nepal Corona Open Data API](https://documenter.getpostman.com/view/9992373/SzS7PkXr?version=latest#intro)

[API: District link](https://data.nepalcorona.info/api/v1/districts)

[API: Municipals link](https://data.nepalcorona.info/api/v1/municipals)

[API: COVID-19 Nepal](https://data.nepalcorona.info/api/v1/covid)

[API: MOHP](https://covid19.mohp.gov.np/covid/api/confirmedcases)

[Wikipedia: COVID-19 pandemic in Nepal](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal)

[Public API Contribution](https://github.com/postmanlabs/postman-code-generators)


### Contribution
If you're new to contributing to Open Source on Github, [this guide](https://opensource.guide/how-to-contribute/) can help you get started. Please check out the contribution guide for more details on how issues and pull requests work.

