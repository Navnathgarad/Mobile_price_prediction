import numpy as np
from PIL import Image
import streamlit as st
import pickle
import numpy

decision_tree_model = pickle.load(open('lr_dtree.pkl','rb'))
#st.title(" Mobile_Price_Range_Prediction ")
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Mobile Price Range Prediction</h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
image = Image.open('mobile.jpg')
st.image(image,'mobile')

battery_power= st.slider("Battery Backup(mAH)",501,1998,key="1")

col1, col2 ,col3= st.columns(3)
with col1:
    X = st.selectbox("Has 4G Connectivity or Not?",('Yes','No'),key="2")
    trial = ["Yes","No"]
    four_g = trial.index(X)

with col2:
    Y = st.selectbox("Bluetooth", ('Yes', 'No'), key="3")
    trial_1 = ["Yes", "No"]
    blue = trial_1.index(Y)

with col3:
    Z = st.selectbox("Dual sim", ('Yes', 'No'), key="4")
    trial_2 = ["Yes", "No"]
    dual_sim = trial_2.index(Z)

col1, col2 = st.columns(2)
with col1:
    P = st.selectbox("Has 3G Connectivity or Not?", ('Yes', 'No'), key="5")
    trial_4 = ["Yes", "No"]
    three_g = trial_4.index(P)

with col2:
    Q = st.selectbox("Wifi Connectivity", ('Yes', 'No'), key="6")
    trial_5 = ["Yes", "No"]
    wifi = trial_5.index(X)

int_memory= st.slider("Internal Memory (GB)",2,64,key="7")

col1, col2 = st.columns(2)
with col1:
    pc = st.slider("Primary Camera(MP)",0,20,key="8")
with col2:
    fc = st.slider("Front Camera(MP)",0,19,key="9")

ram = st.slider("Ram (Mhz i.e 1GB = 1000 Mhz)",256,3998,key="10")

col1, col2 = st.columns(2)
with col1:
    px_height = st.slider("Pixel Height(cm)",0,1960,key="11")
with col2:
    px_width = st.slider("Pixel width(cm)",500,1998,key="12")

col1, col2 = st.columns(2)
with col1:
    sc_h = st.slider("Screen Height(cm)",5,19,key="13")
with col2:
    sc_w = st.slider("Screen width(cm)",5,18,key="14")

def predict_mobile(battery_power,four_g,blue,dual_sim,three_g,wifi,int_memory,pc,fc,ram,px_height,px_width,sc_h,sc_w):
    input = np.array([[battery_power,four_g,blue,dual_sim,three_g,wifi,int_memory,pc,fc,ram,px_height,px_width,sc_h,sc_w]])#.astype(np.float64)
    prediction = decision_tree_model.predict(input)
    if prediction == 0:
        prediction = "5,000 to 10,000"
    elif prediction == 1:
        prediction = "10,000 to 15,000"
    elif prediction == 2:
        prediction = "15,000 to 20,000"
    elif prediction == 3:
        prediction = "20,000 and Above "

    return prediction
    #return prediction[0]
if st.button("Predict"):
    output=predict_mobile(battery_power,four_g,blue,dual_sim,three_g,wifi,int_memory,pc,fc,ram,px_height,px_width,sc_h,sc_w)#.astype(np.int)
    st.success('The Price of your Mobile must range between {}'.format(output))


