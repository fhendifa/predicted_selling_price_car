import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

def run():
# Load Model
    with open('model.pkl', 'rb') as file_1:
        model = joblib.load(file_1)
  # Membuat form
    with st.form("my_form"):
        name = st.text_input('Car', value='')
        year = st.number_input('Year', min_value=1992, max_value=2020, value=2000, step=1)
        km_driven = st.number_input('Kilometers', min_value=0, max_value=1000000, value=0)
        fuel = st.selectbox('Fuel', ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'), index=1)
        seller_type = st.selectbox('Seller', ('Individual', 'Dealer', 'Trustmark Dealer'), index=1)
        transmission = st.selectbox('Transmission', ('Manual', 'Automatic'), index=1)
        owner = st.selectbox('Owner', ('First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'), index=1)
        st.markdown('---')

        submitted = st.form_submit_button("Submit")

    data_inf = {
          'name': name,
          'year': year,
          'km_driven': km_driven,
          'fuel': fuel,
          'seller_type': seller_type,
          'transmission': transmission,
          'owner' : owner
      }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        y_pred_inf_df = model.predict(data_inf)
        
        st.write('# Selling Price : ', str(int(y_pred_inf_df)))

if __name__ == '__main__':
    run()
