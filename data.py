import pandas as pd
import gspread as gs
import json
import streamlit as st
import os


j=st.secrets['js']
res = json.loads(j)

with open('data.json', 'w') as f:
    json.dump(res, f)
    
print('json file created')


def athletics():
	gc = gs.service_account(filename='data.json')
	os.remove('data.json')
	sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1EWuTD-8ATgSxEcuCSVVoYGQ4WIrSpwvlU3u_-Z7qxbo/edit?usp=sharing')
	ws = sh.worksheet('Sheet1')
	df = pd.DataFrame(ws.get_all_records())
	
	return df
