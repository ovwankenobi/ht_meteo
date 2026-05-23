# -*- coding: utf-8 -*-
"""
Created on Sat May 23, 2026

@author: rsderamos
"""

### This script is to download real-time the ECMWF open access data

from ecmwf.opendata import Client
from pathlib import Path


class ecmwf_ifs:
    def __init__(self, cyc_date, cyc_hour, fhour, meteo_db_path):
        self.meteo_db_path = meteo_db_path
        self.request = {
            "date": cyc_date,
            "time": cyc_hour,
            "stream": "oper",
            "type": "fc",
            "step": list(range(0, fhour, 3)), ###fhour is how many hours we will forecast
            "param": ["tp"],
        }

        self.client= Client(
            source="ecmwf",
            model="ifs",
            resol="0p25",
            preserve_request_order=False,
            infer_stream_keyword=True,
        )
    
    def download(self):
        self.grib_file = Path(self.meteo_db_path)/ "ecmwf_ifs" / "_tmp_grib.grib2"
        self.grib_file.parent.mkdir(parents=True, exist_ok=True)
        self.client.retrieve(self.request, self.grib_file)

if __name__ == "__main__":
    

    meteo_db_path = r"D:\projects\Flood_Model\earth_sight\meteo_db"
    cyc_date = "20260523"
    cyc_hour = "00"
    fhour = 24
    ecmwf_ifs(cyc_date, cyc_hour, fhour, meteo_db_path).download()



"""
class ecmwf_aifs_single:
    def __init__(self):
        request = {
            "time": 0,
            "type": "fc",
            "step": 24,
            "param": ["tp"], ## u10, v10, and msl can be added here when transitioning to storm surge
        }

        client_aifs-single = Client(
            source="ecmwf",
            model="aifs-single",
            resol="0p25",
            preserve_request_order=False,
            infer_stream_keyword=True,
        )
    def ecmwf_deterministic_client(self):
        client.retrieve(request, "data.grib2")
        pass
"""


