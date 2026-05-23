# -*- coding: utf-8 -*-
"""
Created on Sat May 23, 2026

@author: rsderamos
"""

from datetime import datetime
from ecmwf_meteo import ecmwf_ifs

class Prep_meteo:
    def __init__(self, meteo_type, cycle, fhour, meteo_db_path, range_lon, range_lat):
        self.meteo_type = meteo_type
        self.fhour = fhour
        self.meteo_db_path = meteo_db_path
        ## Converting the cycle to date and hour for retrieving
        dt = datetime.strptime(cycle, "%Y%m%d_%Hz")
        self.cyc_date = dt.strftime("%Y%m%d")
        self.cyc_hour = dt.strftime("%H")
        self.range_lat = range_lat
        self.range_lon = range_lon
        print (self.range_lat)
    def download_meteo(self):
        if self.meteo_type == "ecmwf_ifs":     
                   
            ecmwf_ifs(self.cyc_date, self.cyc_hour, self.fhour, self.meteo_db_path, self.range_lat, self.range_lon).run()

if __name__ == "__main__":
    meteo_db_path = r"D:\projects\Flood_Model\earth_sight\meteo_db"
    fhour = 24
    cycle = "20260523_12z"
    meteo_type = "ecmwf_ifs"
    range_lon = (115, 130)  
    range_lat = (25, 5) 
    Prep_meteo(meteo_type, cycle, fhour, meteo_db_path, range_lon, range_lat).download_meteo()