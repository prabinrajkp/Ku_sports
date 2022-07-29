import streamlit as st
import pandas as pd
from data import athletics
import dataframe_image as dfi
#import gspread as gs
import json

st.markdown('# Campus olympics')

st.markdown('## By Departmets Union sports clib')


col1,col2=st.columns(2)
with col1:
	st.write( '[Registration- Athletics](https://docs.google.com/forms/d/e/1FAIpQLSe8I1zuALlXKmxGu7gIRmH6DQ9LAOTEwfQ1jLgkZPFMitSJQg/viewform?usp=sf_link)')
	
with col2:
	st.write( '[Registration- Games](https://docs.google.com/forms/d/e/1FAIpQLSe8I1zuALlXKmxGu7gIRmH6DQ9LAOTEwfQ1jLgkZPFMitSJQg/viewform?usp=sf_link)')



st.write('---')

tab1, tab2,tab3 = st.tabs(["Event Wise Result","Leader Board","Point Table - Department_wise"])

df=athletics()
ev=df['Event'].unique()

with tab1:

	c1,c2=st.columns(2)
	#with c1:
	option = st.selectbox('Event result',ev)

	st.write('Results For ', option)

	ev=df[df['Event']==option]
	ev=ev[['Name','Faculty','Department','Position']]
		
		
	bd=ev.style.set_properties(**{'background-color': 'black',
		                       'color': 'white',
		                       'border-color': 'Red'}).hide_index().set_caption(str(option)+' result')
		
	st.dataframe(ev)
	dfi.export(ev, 'Result.png')
		
	with open("Result.png", "rb") as file: btn = st.download_button(
		         label="Download Result",
		         data=file,
		         file_name="result.png",
		         mime="image/png"
		       )
		       
	#with c2:
	st.markdown('###### Leaderboard - Individual')
	dpt=df[df['Department']!='']
	dpt=dpt.groupby(['Name']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False).head(10)
	st.dataframe(dpt)
		

	
with tab2:
	c1,c2=st.columns(2)
	
	with c1:
	
		
		st.markdown('###### Leaderboard - Faculty wise')
		st.dataframe(df.groupby(['Faculty']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False))
	
	with c2:
		st.markdown('###### Leaderboard - Department wise')
		dpt=df.groupby(['Department']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False)
		dpt=dpt.head(10)
		st.dataframe(dpt[dpt['Department']!=''])

	
	


with tab3:
	
	
	
	st.write('ssbsbbs')

#st.dataframe(df)
	
	

