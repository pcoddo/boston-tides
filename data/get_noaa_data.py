#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:Project:   boston-tides
:Created:   Tue Oct 19 16:14:49 2021
:Filename:  get_noaa_data.py

Downloads hourly data for Boston tide gauge from NOAA Tides and Currents
"""
__version__ = "1.0"
__author__ = "Perry Oddo <perry.oddo@nasa.gov>"

import noaa_coops as nc


# Find Boston station 
boston = nc.Station(8443970)

# Find hourly heights
gauge_raw = boston.get_data(
    begin_date="19210504",
    end_date="20210930",
    product="hourly_height",
    datum="STND",
    units="metric",
    time_zone="gmt")

# Remove duplicate indices
gauge_raw = gauge_raw[~gauge_raw.index.duplicated(keep="first")]
gauge_raw.to_csv("data/boston_hourly_msl.csv")