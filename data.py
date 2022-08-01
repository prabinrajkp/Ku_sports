import pandas as pd
import gspread as gs
import json
import streamlit as st
import os



    
print('json file created')


def athletics():
	j=st.secrets['js']
	res = json.loads(j)
	with open('data.json', 'w') as f:
		json.dump(res, f)

	gc = gs.service_account(filename='data.json')
	os.remove('data.json')
	sh = gc.open_by_url(st.secrets['result'])
	ws = sh.worksheet('Sheet1')
	df = pd.DataFrame(ws.get_all_records())
	
	return df
	
def registration(lst):

	j=st.secrets['js']
	res = json.loads(j)
	with open('data.json', 'w') as f:
		json.dump(res, f)

	gc = gs.service_account(filename='data.json')
	os.remove('data.json')
	
	sh = gc.open_by_url(st.secrets['reg'])
	ws = sh.worksheet('Sheet1')
	ws.insert_row(lst,2)
	
	#return None

	
	
