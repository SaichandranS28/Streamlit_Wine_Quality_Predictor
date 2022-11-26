# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:39:25 2022

@author: home
"""

import numpy as np
import pickle
import streamlit as st
import base64

#loading the saved model
loaded_model = pickle.load(open('trained_model_final.sav','rb'))


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
   
def Wine_quality_prediction(input_data):
    
    # changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the data as we are predicting the label for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==3):
        return 'Very Bad Quality Wine'
    elif(prediction[0]==4):
        return 'Bad Quality Wine'
    elif(prediction[0]==5):
        return 'Average Quality wine'
    elif(prediction[0]==6):
        return 'Normal Quality Wine'
    elif(prediction[0]==7):
        return 'Good Quality Wine'
    else:
        return 'Very Good Quality Wine' 
  
def main():
    
    #Adding title to the web app
    #add_bg_from_local('D:/5th sem/miniproject/Wine Quality Prediction/requirements/wine10.jpg') 
    new_title = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">Wine Quality Prediction</p>'
    st.markdown(new_title, unsafe_allow_html=True)
   

    #Getting input from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        
        fixedacidity = st.text_input("FIXED ACIDITY :")
        volatile = st.text_input('VOLATILE ACIDITY:')
        citricacid = st.text_input('CITRIC ACID :')
        residualsugar = st.text_input('RESIDUAL SUGAR:')
        
    with col2:
        
        chlorides = st.text_input('CHLORIDES :')
        free_sulfur_dioxide = st.text_input('FREE SULFUR DIOXIDE :')
        total_sulfur_dioxide = st.text_input('TOTAL SULFUR DIOXIDE :')
        density = st.text_input('DENSITY :')
              
    with col3:  

        pH = st.text_input('pH :')
        sulphates = st.text_input('SULPHATES :')
        alcohol = st.text_input('ALCOHOL :')

    
    #code for prediction
    result = ' '
    
    #Creating button for prediction
    if st.button('Click here to predict'):
        result = Wine_quality_prediction([fixedacidity,volatile,citricacid,residualsugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol])
    
        st.balloons()
        st.success(result)
    
    text_contents = (result+"\nThanks for using WINE QUALITY PREDICTOR WEB APP \n S Saichandran")
    st.download_button('Download', text_contents)
    
if __name__=='__main__':
    main()    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
