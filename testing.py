import joblib
import streamlit as st
import numpy as np

model = joblib.load('housing.joblib')

def prediction(longitude=0,latitude=0,age=0,t_rooms=0,t_beds=0,pops=0,household=0,med_income=0,ocean_proximity=0):
    test = [float(longitude),float(latitude),float(age),float(t_rooms),float(t_beds),float(pops),float(household),float(med_income),float(ocean_proximity)]
    bedroom_ratio = 0 if test[3] == 0 else test[4]/test[3]
    income_per_person = 0 if test[5] == 0 else test[7] / test[5]
    household_rooms = 0 if test[6] == 0 else test[3]/test[6]
    romms_per_person = 0 if test[5] == 0 else test[3]/test[5]

    test.append(bedroom_ratio)
    test.append(income_per_person)
    test.append(household_rooms)
    test.append(romms_per_person)
    predicted_value = model.predict(np.array([test]))
    return predicted_value[0]

st.title("Housing Price Prediction")

longitude = st.text_input("Longitude",key="Longitude")
latitude = st.text_input("Latitude",key="Latitude")
house_age = st.text_input("House Age",key="House Age")
t_rooms = st.text_input("Total Number of Rooms",key="t_rooms")
t_bedrooms = st.text_input("Total Number of Bedrooms",key="t_bedrooms")
population = st.text_input("Number of people",key="population")
household = st.text_input("Households",key="household")
med_income = st.text_input("Median Income",key="med_income")
ocean_proximity = st.selectbox("Ocean Proximity", ["Close", "Inland", "Island", "Near Bay", "Near Ocean"])
if ocean_proximity == "Close":
    ocean_proximity = 0
elif ocean_proximity == "Inland":
    ocean_proximity = 1
elif ocean_proximity == "Island":
    ocean_proximity = 2
elif ocean_proximity == "Near Bay":
    ocean_proximity = 3
elif ocean_proximity == "Near Ocean":
    ocean_proximity = 4

press = st.button("Predict")
if press:
    predicted = round(prediction(longitude,latitude,house_age,t_rooms,t_bedrooms,population,household,med_income,ocean_proximity),2)

    st.markdown(f"<h4>The Predicted Price is {predicted}<h4>", unsafe_allow_html=True)