import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="π",
    layout="wide",
)

st.markdown("# KOSPI 200 ESG μ§μ")
st.sidebar.markdown("# μκ°ν π")

file_names = ["data\kospi200_esg_index.csv", "data\kospi200_esg_index_zero.csv"]

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data_load_state = st.text('Loading data...')
# data_zero = load_data(file_names[0])
data = load_data(file_names[1]) # κ²°μΈ‘μΉλ₯Ό 0μΌλ‘ λμ²΄ν νμΌλ‘ μ¬μ©
data_load_state.text("Done! (using st.cache)")

st.dataframe(data)

# μ’κ°, κ±°λλ, λ±λ½λ₯  μ€ μ ν
standard = ["None", "μ’κ°", "κ±°λλ", "λ±λ½λ₯ "]
selected_standard = st.sidebar.selectbox("μκ°νν  column", standard) 

# κΈ°μ€ λ μ§ μ ν
v_list = ["None", "μ μ²΄ λ μ§μ λν μκ°ν", "μ°λλ³ μκ°ν", "μ°λ-μλ³ μκ°ν"]
selected_v = st.sidebar.selectbox("μκ°ν κΈ°μ€", v_list)

def visualize(s, v):    # selectbox λμ ν¨μ
    if v == v_list[0]:
        pass
    elif v == v_list[1]:
        st.line_chart(data.set_index("μΌμ")[s])
    elif selected_v == v_list[2]:
        fig = plt.figure(figsize=(20, 5))
        sns.lineplot(data=data, x="μ°λ", y=s, ci=None)
        st.pyplot(fig)
    else:
        fig = plt.figure(figsize=(20, 5))
        sns.lineplot(data=data, x="μ°λμ", y=s, ci=None)
        st.pyplot(fig)
        
visualize(selected_standard, selected_v)
