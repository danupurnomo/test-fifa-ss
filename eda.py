import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import plotly.express as px

def run():
    # Membuat Title
    st.title('Aplikasi Prediksi Rating Pemain FIFA 2022')

    # Membuat Sub Header
    st.subheader('Page ini berisi Exploratory Data Analysis (EDA) mengenai dataset FIFA 2022')

    # Menampilkan Teks
    st.write('Page ini dibuat oleh *Danu P.*')
    st.write('# Teks 1')
    st.write('## Teks 2 \n Teks 3')

    # Menambahkan Gambar
    data = mpimg.imread('./src/soccer.jpg')
    st.image(data, caption='EDA FIFA 2022')

    # Menampilkan DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # Menampilkan Histogram of Rating
    st.write('### Plot Histogram of Rating')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df['Overall'], bins=30, kde=True)
    st.pyplot(fig)

    # Menampilkan Histogram berdasarkan Input User
    st.write('### Histogram berdasarkan Input User')
    opsi = st.selectbox('Pilih column : ', ('Age', 'Height', 'Weight', 'PaceTotal'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df[opsi], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Plot menggunakan Plotly
    st.write('Plotly Plot - ValueEUR vs Overall')
    fig = px.scatter(df, x='ValueEUR', y='Overall', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)



if __name__ == '__main__':
    run()