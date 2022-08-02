import streamlit as st
import streamlit as st
import pandas as pd
from data import athletics
import dataframe_image as dfi
#import gspread as gs
from PIL import Image
import json
import datetime
from data import registration
from data import reg

def admin():

	tab1, tab2,tab3,tab4 = st.tabs(["Event Wise Result","Leader Board","Registration",'Admin Access'])

	df=athletics()
	ev=df['Event'].unique()

	with tab1:

		c1,c2=st.columns(2)
		#with c1:
		st.markdown('###### Event result')
		option = st.selectbox('',ev)

		st.write('Results For ', option)

		ev=df[df['Event']==option]
		ev=ev[['Name','Faculty','Department','Position']]
			
			
		bd=ev.style.set_properties(**{'background-color': 'black',
				                   'color': 'white',
				                   'border-color': 'Red'}).hide_index().set_caption(str(option)+' result')
			
		st.dataframe(ev)
		#dfi.export(ev, 'Result.png')
			
		#with open("Result.png", "rb") as file: btn = st.download_button(
				     #label="Download Result",
				     #data=file,
				     #file_name="result.png",
				     #mime="image/png"
				   #)
		st.write('---')	       
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

		#name,mob,mail= None
		with st.form("reg2", clear_on_submit=True):
			tb1,tb2=st.columns(2)
		
			#st.write('name')
			with tb1:
				name=st.text_input(label='Name')
				mob=st.text_input(label='Phone')
				mail=st.text_input(label='E-mail')
			with tb2:
				gen=st.selectbox('Gender',('Male','Female','Transgender'))
				d = st.date_input( "Date of birt",datetime.date(1999, 1, 1))
				
				fac=st.selectbox('Faculty',
				('Applied Science and Technology','Arts, Education & Music','IMk, Commerce & Law','OrientalStudies','Science','Social Science'))
			
			items = st.multiselect(
		 'Events (Maximum 3 events)',
		 ['100 meter','200 meter','400 meter','1500 meter','Walking (3000 meter)','Shot put','Discus Throw','Javelin throw','Cricket Ball Throw'])
			
			
			submit_button = st.form_submit_button(label='Submit')
		#st.write(len(name),len(mob),len(mail))
		
		
			
		if len(items)>3 and submit_button==True:
			st.error('Error: items cannot be more than 3')
		#st.write(name,mob,mail,fac)
		elif submit_button==True and ((len(name) and len(mob) and len(mail))<1)  :
			st.error("Error: all fields must be filled")
			
		elif submit_button==True:
			st.success(str(name)+' Successfully registered for ' + str(items))
			
			for event in items:
				
				lst=[name,mob,mail,gen,fac,str(d),event]
				registration(lst)
				
				
	with tab4:
		
		
		with st.form('ew',clear_on_submit=True):
			st.markdown('#### Event Wise Participants')
		
			Event=st.selectbox(
		 'Event)',
		 ['100 meter','200 meter','400 meter','1500 meter','Walking (3000 meter)','Shot put','Discus Throw','Javelin throw','Cricket Ball Throw'])
			gen1=st.selectbox('Gender',('Male','Female','Transgender'))
			submit = st.form_submit_button(label='Submit')
			
			d=reg()
			
			if submit==True:
				
				st.write('Participants for ' + str(Event)+'-'+str(gen1))
				elist=d[(d['event']==Event) & (d['gender']==gen1)]
				st.dataframe(elist[['name','mobile','email','faculty','age']])
				
		with st.form('fac'):
			st.markdown('#### Faculty Wise Participants')
			fac=st.selectbox('Faculty',
				('Applied Science and Technology','Arts, Education & Music','IMk, Commerce & Law','OrientalStudies','Science','Social Science'))
			submit2 = st.form_submit_button(label='Submit')
			
			if submit2==True:	
				fc=d[d['faculty']==fac]
				st.dataframe(fc[['name','mobile','email','event','gender']])
			
			
			
			
			#st.dataframe(d)
		
		
		
		
