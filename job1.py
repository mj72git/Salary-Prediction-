import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('job1.joblib')
st.title('Salary Prediction in 2022')
st.write("""### We need some information to predict the salary""")

countries = (
    "United States of America",
    "Iran, Islamic Republic of...",
    "India",
    "United Kingdom of Great Britain and Northern Ireland",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden",
    "Switzerland",
    "Israel",
    "Austria",
    "Portugal",
    "Denmark",
    "Turkey",
    "Belgium",
    "Norway",
    "Finland",
    "Greece",
    "Czech Republic",
    "New Zealand",
    "Mexico",
    "South Africa",
    "Pakistan"

)

education = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree",
    "Post grad"
)

Gender = ("Man","Woman")

Age = ("under 18 years old","18-24 years old","25-34 years old",
    "35-44 years old","45-54 years old","55-64 years old",
    "65 years or older")



country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)
expericence = st.slider("Years of Experience", 0, 50, 3)
gender = st.radio("Choose gender",['Man','Woman'])
age=st.selectbox("Age",Age)

columns = ['Country', 'EdLevel', 'YearsCodePro', 'Age', 'Gender']

ok = st.button("Calculate Salary")
if ok:
    X_new = np.array([countries,education,expericence,gender,age])
    X_new_df = pd.DataFrame([X_new], columns = columns)
    salary = model.predict(X_new_df)
    
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")\

