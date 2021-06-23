import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict():
    st.title("software salary predict")

    st.write("""###need some information""")
    countries = (
        "United States",
        "India",
        "United Kingdom",        
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
    )
    country = st.selectbox("Country",countries)
    education =(
        'Bachelor’s degree', 
        'Master’s degree', 
        'Less than a Bachelors',
        'Post grad',
    )
    education=st.selectbox("EDUCATION LEVEL",education)

    experience = st.slider("YEARS OF EXPERIENCE",0,50,3)

    ok=st.button("COLCULATE SALARY")

    if ok:
        X = np.array([[country, education,experience ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary=regressor.predict(X)
        st.subheader(f"THE ESTIMATE SALARY IS ${salary[0]:.2f}")        
    