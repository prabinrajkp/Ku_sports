import pandas as pd
import gspread as gs

def athletics():
	gc = gs.service_account(filename='horizontal-ward-317609-7b13c9012800.json')
	sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1EWuTD-8ATgSxEcuCSVVoYGQ4WIrSpwvlU3u_-Z7qxbo/edit?usp=sharing')
	ws = sh.worksheet('Sheet1')
	df = pd.DataFrame(ws.get_all_records())
	
	return df
