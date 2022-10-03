import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image

pipe = pickle.load(open("result.pkl",'rb'))


teams = ['Australia', 'New Zealand', 'Sri Lanka', 'India', 'England',
       'West Indies', 'Pakistan', 'South Africa', 'Ireland', 'Bangladesh',
       'Thailand', 'Uganda', 'Netherlands', 'Papua New Guinea',
       'Scotland', 'United Arab Emirates', 'Malaysia', 'Botswana',
       'Malawi', 'Sierra Leone', 'Mozambique', 'Namibia', 'Lesotho',
       'China', 'Nepal', 'Hong Kong', 'Kuwait', 'Zimbabwe', 'Nigeria',
       'Tanzania', 'Japan', 'Indonesia', 'Fiji', 'Vanuatu', 'Samoa',
       'United States of America', 'Mali', 'Singapore', 'Maldives',
       'Germany', 'Oman', 'Austria', 'Rwanda', 'Kenya', 'France',
       'Norway', 'Eswatini', 'Cameroon', 'Argentina', 'Canada', 'Bhutan',
       'Barbados', 'Qatar', 'Saudi Arabia', 'Bahrain', 'Brazil', 'Jersey']

cities = ['Melbourne', 'Victoria', 'Adelaide', 'Colombo', 'Nelson',
       'Bangkok', 'Sydney', 'Canberra', 'Antigua', 'Sharjah',
       'Potchefstroom', 'East London', 'Johannesburg', 'Centurion',
       'Cape Town', 'Taunton', 'Bristol', 'Chelmsford', 'Mumbai',
       'Mount Maunganui', 'New Plymouth', 'Hamilton', 'Bloemfontein',
       'Brisbane', 'Dublin', 'Utrecht', 'Amstelveen', 'Kuala Lumpur',
       'Guyana', 'St Lucia', 'Wellington', 'Auckland', 'Trinidad',
       'FTZ Sports Complex', 'Gaborone', 'Northampton', 'Brighton',
       'Guwahati', 'Karachi', 'Perth', 'Pretoria', 'Pietermaritzburg',
       'Benoni', 'Windhoek', 'Harare', 'Port Vila', 'Lauderhill',
       'Kigali City', 'Murcia', 'Deventer', 'Dundee', 'Arbroath',
       'Incheon', 'Singapore', 'Bridgetown', 'Surat', 'Gros Islet',
       'Providence', 'Lahore', 'Pokhara', 'Al Amarat', 'Lower Austria',
       'Derby', 'Durban', 'Napier', 'Lucknow', 'Belfast', 'Carrara',
       'North Sound', 'Coolidge', 'Krefeld', 'Kolsva', 'Naucalpan',
       'Dubai', 'Queenstown', 'Birmingham', 'Doha', 'Worcester',
       'Chester-le-Street', 'Ajman', 'Kirtipur', 'Bready', 'Dambulla',
       'Bangi', 'St Saviour', 'Schiedam', 'The Hague', 'Edinburgh',
       'Abu Dhabi', 'Nottingham', 'London', 'Barbados', 'Paarl', 'Galle',
       'Canterbury', 'Manchester', 'Hove', 'Arundel', 'Loughborough',
       'Guanggong', 'Southampton', 'Sylhet', 'Mirpur', 'Gold Coast',
       'Cardiff', 'Grenada', 'Bangalore', 'Delhi', 'Chennai',
       'Chandigarh', 'Nagpur', 'Mohali', 'Dharamsala', 'Kolkata',
       'Londonderry']

img= Image.open("Asia Cup.png")
st.title("Women T20 World Cup Score.")

st.image(img,caption="Asia Cup")
col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team",sorted(teams))

with col2:
    bowling_team = st.selectbox("Select Bowling Team",sorted(teams))

city = st.selectbox("Select City",sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input("Current Score")
with col4:
    overs = st.number_input("Overs Bowled( >5 Overs)")
with col5:
    wickets = st.number_input("Wickets Out")

last_five = st.number_input("Runs Scored in last 5 Overs")

if st.button("Predict Score"):
    
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    input_df = pd.DataFrame(
        {
            'batting_team':[batting_team],
            'bowling_team':[bowling_team],
            'city':[city],
            'Current_Score':[current_score],
            'balls left':[balls_left],
            'wickets left':[wickets_left],
            'crr':[crr],
            'last_five':[last_five]
        }
    )

    result = pipe.predict(input_df)
    st.header("Predicted Score: " + str(int(result[0])))