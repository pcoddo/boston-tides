#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:Project:   boston-tides
:Created:   Tue Oct 19 16:14:49 2021
:Filename:  get_full_data.py

1) Downloads Boston sea level reconstruction from Talke et al. (2018):
    Talke, S. A., Kemp, A. C., & Woodruff, J. (2018). Relative Sea Level, Tides, 
    and Extreme Water Levels in Boston Harbor From 1825 to 2018. Journal of Geophysical Research: 
    Oceans, 123(6), 3895–3914. https://doi.org/https://doi.org/10.1029/2017JC013645

2) Concatenates recent data (2018/01/01 - 2021/09/30) from NOAA Tides and Currents
"""
__version__ = "1.0"
__author__ = "Perry Oddo <perry.oddo@nasa.gov>"


import requests
import noaa_coops as nc
import pandas as pd
from io import StringIO



#####################################################
## Download reconstruction from Talked et al. (2018)
#####################################################
url = "https://agupubs.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1029%2F2017JC013645&file=jgrc22945-sup-0002-2017JC013645-ds01.txt"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}
data = requests.get(url, headers= headers).text

# Format into data frame
left_df = pd.read_csv(StringIO(data), comment="#", delim_whitespace=True, names=["year", "sea_level"], skiprows=lambda x: x%2 == 0)
right_df = pd.read_csv(StringIO(data), comment="#", delim_whitespace=True, names=["datum_correction"], skiprows=lambda x: x%2 == 1)
df_combined = pd.concat([left_df, right_df], axis=1)


##############################################################
## Download data from 2018 onward from NOAA Tides and Currents
##############################################################
boston = nc.Station(8443970)

# Find hourly heights
df_hourly = boston.get_data(
    begin_date="20180101",
    end_date="20210930",
    product="hourly_height",
    datum="STND",
    units="metric",
    time_zone="gmt")

# Find annual means
annual_mean = df_hourly.resample("Y")["water_level"].mean()

df_annual_mean = pd.DataFrame(
    {
    "year": annual_mean.index.year,
    "sea_level": annual_mean,
    "datum_correction": 0.0
    }
)

############################
## Combine into full dataset
############################

df_full = df_combined.append(df_annual_mean, ignore_index=True)

# Save to file
df_full.to_csv("data/boston_annual_msl.csv")