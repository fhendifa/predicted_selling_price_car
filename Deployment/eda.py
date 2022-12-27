import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title='Sell Price Car - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # Membuat Title
    st.title('Selling Price Car Prediction')

    # Membuat Sub Header
    st.subheader('EDA')

    # Menambahkan Gambar
    #image = Image.open('soccer.jpg')
    #st.image(image, caption='FIFA 2022')

    # Membuat Garis Lurus
    st.markdown('---')

    # Magic Syntax
    '''
    Pada page kali ini, saya akan melakukan eskplorasi data sederhana.
    Dataset yang digunakan adalah dataset 'CAR DETAILS FROM CAR DEKHO'.
    Dataset ini berasal dari web Kaggle.com.
    '''

    # Show DataFrame
    data = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')
    st.dataframe(data)

    # Membuat BarPlot
    st.write('#### Owner')
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(x='owner', data=data)
    st.pyplot(fig)

    # Membuat Plotly Pie
    st.write('#### 10 Kendaraan Yang Banyak Dijual')
    fig=px.pie(data_frame = data ,names = data.name.value_counts().head(10).index,values = data.name.value_counts().values[0:10],hole = 0.7)
    st.plotly_chart(fig)

    # Membuat Plotly Pie
    st.write('#### Jenis Bahan Bakar')
    fig=px.pie(data_frame = data ,names = data.fuel.value_counts().index,values = data.fuel.value_counts().values,hole = 0.7)
    st.plotly_chart(fig)

    # Membuat BarPlot
    st.write('#### Owner')
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(x='seller_type', data=data)
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('#### Mobil dengan Harga Jual')
    fig = px.scatter(data, x='name', y='selling_price', hover_data=['year', 'transmission'] )
    st.plotly_chart(fig)

    

if __name__ == '__main__':
    run()