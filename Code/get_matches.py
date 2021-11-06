# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:53:36 2021

@author: hp
"""

import requests
import pandas as pd
url = "https://api.opendota.com/api/matches/6067993716"
resp = requests.get(url)

data = resp.json()
matches = pd.DataFrame(data)