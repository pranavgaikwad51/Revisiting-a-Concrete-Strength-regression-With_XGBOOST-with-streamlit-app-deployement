import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Trained XGBoost Model
# -------------------------------
model = pickle.load(open('best_model_xgboost.pkl', 'rb'))

# -------------------------------
# Sidebar – Your Information
# -------------------------------
st.sidebar.title("👤 Developer Info")

st.sidebar.markdown("""
### **Pranav Gaikwad**
- 📧 **Email:** gaikwadpranav988@gmail.com  
- 📱 **Phone:** 7028719844  
- 🔗 **LinkedIn:**  
  [linkedin.com/in/pranav-gaikwad-0b94032a](https://www.linkedin.com/in/pranav-gaikwad-0b94032a)  
- 🐙 **GitHub:**  
  [github.com/pranavgaikwad51](https://github.com/pranavgaikwad51)  


---

### 🎯 **Career Goals**
- Becoming **Data Scientist → AI/ML Engineer → Chief AI Scientist**
- Mastering **Machine Learning, XGBoost, Deep Learning, App Deployment**
- Building real-world ML apps for business problems

---

### 📚 Current Learning
- Data Science & AI (6-month program)
- Python, ML, XGBoost, EDA, Deployment  
- Developing Import-Export App (Confidentiality + Middleman Control)

""")

# -------------------------------
# Main App Title
# -------------------------------
st.title("🧱 Concrete Compressive Strength Prediction (XGBoost Model)")

st.write("""
This app predicts the **compressive strength of concrete**  
using the Yeh Concrete Dataset and XGBoost regression model.
""")

# -------------------------------
# Input Fields
# -------------------------------
st.header("🔢 Enter Input Features")

cement = st.number_input('Cement (kg/m³)', min_value=0.0, value=300.0)
slag = st.number_input('Blast Furnace Slag (kg/m³)', min_value=0.0, value=100.0)
flyash = st.number_input('Fly Ash (kg/m³)', min_value=0.0, value=50.0)
water = st.number_input('Water (kg/m³)', min_value=0.0, value=180.0)
superplasticizer = st.number_input('Superplasticizer (kg/m³)', min_value=0.0, value=10.0)
coarseagg = st.number_input('Coarse Aggregate (kg/m³)', min_value=0.0, value=900.0)
fineagg = st.number_input('Fine Aggregate (kg/m³)', min_value=0.0, value=800.0)
age = st.number_input('Age (days)', min_value=1, value=28)

# -------------------------------
# Prepare Input For Prediction
# -------------------------------
input_data = pd.DataFrame([{
    'cement': cement,
    'slag': slag,
    'flyash': flyash,
    'water': water,
    'superplasticizer': superplasticizer,
    'coarseaggregate': coarseagg,
    'fineaggregate': fineagg,
    'age': age
}])

# -------------------------------
# Predict Button
# -------------------------------
if st.button('Predict Compressive Strength'):
    prediction = model.predict(input_data)
    st.success(f"### 🔮 Predicted Compressive Strength: **{prediction[0]:.2f} MPa**")
