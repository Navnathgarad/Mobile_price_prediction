import numpy as np
from PIL import Image
import streamlit as st
import pickle
import numpy

decision_tree_model = pickle.load(open('lr_dtree_2.pkl','rb'))
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

col1, col2 = st.columns(2)
with col1:
    X = st.selectbox("Has 4G Connectivity or Not?",('Yes','No'),key="2")
    trial = ["Yes","No"]
    four_g = trial.index(X)

with col2:
    Y = st.selectbox("Has 3G Connectivity or Not?", ('Yes', 'No'), key="3")
    trial_2 = ["Yes", "No"]
    three_g = trial_2.index(Y)

col1, col2 = st.columns(2)
with col1:
    Z = st.selectbox("Touch Screen", ('Yes', 'No'), key="4")
    trial_3 = ["Yes", "No"]
    touch_screen = trial_3.index(Z)

with col2:
    m_dep = st.selectbox("Mobile Depth(cm)", (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), key="5")

talk_time = st.slider("Battery Last long(Hour)", 2, 20, key="6")

col1, col2 = st.columns(2)
with col1:
    pc = st.slider("Primary Camera(MP)",0,20,key="7")
with col2:
    fc = st.slider("Front Camera(MP)",0,19,key="8")

ram = st.slider("Ram (Mhz i.e 1GB = 1000 Mhz)",256,3998,key="9")

col1, col2 = st.columns(2)
with col1:
    px_height = st.slider("Pixel Height(cm)",0,1960,key="10")
with col2:
    px_width = st.slider("Pixel width(cm)",500,1998,key="11")

col1, col2 = st.columns(2)
with col1:
    mobile_wt = st.slider("Mobile Weight",80,200,key="12")
with col2:
    sc_w = st.slider("Screen width(cm)",0,18,key="13")

def predict_mobile(battery_power,four_g,three_g,touch_screen,m_dep,talk_time,pc,fc,ram,px_height,px_width,mobile_wt,sc_w):
    input = np.array([[battery_power,four_g,three_g,touch_screen,m_dep,talk_time,pc,fc,ram,px_height,px_width,mobile_wt,sc_w]])#.astype(np.float64)
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
    output=predict_mobile(battery_power,four_g,three_g,touch_screen,m_dep,talk_time,pc,fc,ram,px_height,px_width,mobile_wt,sc_w)#.astype(np.int)
    st.success('The Price of your Mobile must range between {}'.format(output))

