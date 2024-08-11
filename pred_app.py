import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load model
try:
    with open('Fmodel.pkl', 'rb') as f:
        mod = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Define encoders
try:
    le_car_name = LabelEncoder()
    le_car_name.fit(['ritz', 'sx4', 'ciaz', 'wagon r', 'swift', 'vitara brezza', 's cross', 'alto 800', 'ertiga', 'dzire', 'alto k10', 'ignis', '800', 'baleno', 'omni', 'fortuner', 'innova', 'corolla altis', 'etios cross', 'etios g', 'etios liva', 'corolla', 'etios gd', 'camry', 'land cruiser', 'Royal Enfield Thunder 500', 'UM Renegade Mojave', 'KTM RC200', 'Bajaj Dominar 400', 'Royal Enfield Classic 350', 'KTM RC390', 'Hyosung GT250R', 'Royal Enfield Thunder 350', 'KTM 390 Duke ', 'Mahindra Mojo XT300', 'Bajaj Pulsar RS200', 'Royal Enfield Bullet 350', 'Royal Enfield Classic 500', 'Bajaj Avenger 220', 'Bajaj Avenger 150', 'Honda CB Hornet 160R', 'Yamaha FZ S V 2.0', 'Yamaha FZ 16', 'TVS Apache RTR 160', 'Bajaj Pulsar 150', 'Honda CBR 150', 'Hero Extreme', 'Bajaj Avenger 220 dtsi', 'Bajaj Avenger 150 street', 'Yamaha FZ  v 2.0', 'Bajaj Pulsar  NS 200', 'Bajaj Pulsar 220 F', 'TVS Apache RTR 180', 'Hero Passion X pro', 'Bajaj Pulsar NS 200', 'Yamaha Fazer ', 'Honda Activa 4G', 'TVS Sport ', 'Honda Dream Yuga ', 'Bajaj Avenger Street 220', 'Hero Splender iSmart', 'Activa 3g', 'Hero Passion Pro', 'Honda CB Trigger', 'Yamaha FZ S ', 'Bajaj Pulsar 135 LS', 'Activa 4g', 'Honda CB Unicorn', 'Hero Honda CBZ extreme', 'Honda Karizma', 'Honda Activa 125', 'TVS Jupyter', 'Hero Honda Passion Pro', 'Hero Splender Plus', 'Honda CB Shine', 'Bajaj Discover 100', 'Suzuki Access 125', 'TVS Wego', 'Honda CB twister', 'Hero Glamour', 'Hero Super Splendor', 'Bajaj Discover 125', 'Hero Hunk', 'Hero  Ignitor Disc', 'Hero  CBZ Xtreme', 'Bajaj  ct 100', 'i20', 'grand i10', 'i10', 'eon', 'xcent', 'elantra', 'creta', 'verna', 'city', 'brio', 'amaze', 'jazz'])
    
    le_fuel_type = LabelEncoder()
    le_fuel_type.fit(['Petrol', 'Diesel', 'CNG'])
    
    le_selling_type = LabelEncoder()
    le_selling_type.fit(['Dealer', 'Individual'])
    
    le_transmission = LabelEncoder()
    le_transmission.fit(['Manual', 'Automatic'])
except Exception as e:
    st.error(f"Error setting up label encoders: {e}")

# Streamlit app
st.title("Car Price Prediction")

# Define input fields
car_name = st.selectbox("Car Name", options=['ritz', 'sx4', 'ciaz', 'wagon r', 'swift', 'vitara brezza', 's cross', 'alto 800', 'ertiga', 'dzire', 'alto k10', 'ignis', '800', 'baleno', 'omni', 'fortuner', 'innova', 'corolla altis', 'etios cross', 'etios g', 'etios liva', 'corolla', 'etios gd', 'camry', 'land cruiser', 'Royal Enfield Thunder 500', 'UM Renegade Mojave', 'KTM RC200', 'Bajaj Dominar 400', 'Royal Enfield Classic 350', 'KTM RC390', 'Hyosung GT250R', 'Royal Enfield Thunder 350', 'KTM 390 Duke ', 'Mahindra Mojo XT300', 'Bajaj Pulsar RS200', 'Royal Enfield Bullet 350', 'Royal Enfield Classic 500', 'Bajaj Avenger 220', 'Bajaj Avenger 150', 'Honda CB Hornet 160R', 'Yamaha FZ S V 2.0', 'Yamaha FZ 16', 'TVS Apache RTR 160', 'Bajaj Pulsar 150', 'Honda CBR 150', 'Hero Extreme', 'Bajaj Avenger 220 dtsi', 'Bajaj Avenger 150 street', 'Yamaha FZ  v 2.0', 'Bajaj Pulsar  NS 200', 'Bajaj Pulsar 220 F', 'TVS Apache RTR 180', 'Hero Passion X pro', 'Bajaj Pulsar NS 200', 'Yamaha Fazer ', 'Honda Activa 4G', 'TVS Sport ', 'Honda Dream Yuga ', 'Bajaj Avenger Street 220', 'Hero Splender iSmart', 'Activa 3g', 'Hero Passion Pro', 'Honda CB Trigger', 'Yamaha FZ S ', 'Bajaj Pulsar 135 LS', 'Activa 4g', 'Honda CB Unicorn', 'Hero Honda CBZ extreme', 'Honda Karizma', 'Honda Activa 125', 'TVS Jupyter', 'Hero Honda Passion Pro', 'Hero Splender Plus', 'Honda CB Shine', 'Bajaj Discover 100', 'Suzuki Access 125', 'TVS Wego', 'Honda CB twister', 'Hero Glamour', 'Hero Super Splendor', 'Bajaj Discover 125', 'Hero Hunk', 'Hero  Ignitor Disc', 'Hero  CBZ Xtreme', 'Bajaj  ct 100', 'i20', 'grand i10', 'i10', 'eon', 'xcent', 'elantra', 'creta', 'verna', 'city', 'brio', 'amaze', 'jazz'])
fuel_type = st.selectbox("Fuel Type", options=['Petrol', 'Diesel', 'CNG'])
selling_type = st.selectbox("Selling Type", options=['Dealer', 'Individual'])
transmission = st.selectbox("Transmission", options=['Manual', 'Automatic'])
year = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, step=1)
present_price = st.number_input("Present Price", min_value=0.0, step=0.01)
driven_kms = st.number_input("Driven Kms", min_value=0, step=1)
owner = st.number_input("Owner", min_value=0, step=1)

# Transform input values
try:
    car_name = le_car_name.transform([car_name])[0]
    fuel_type = le_fuel_type.transform([fuel_type])[0]
    selling_type = le_selling_type.transform([selling_type])[0]
    transmission = le_transmission.transform([transmission])[0]
except Exception as e:
    st.error(f"Error transforming input data: {e}")

# Create DataFrame from inputs
input_data = pd.DataFrame({
    'Car_Name': [car_name],
    'Year': [year],
    'Present_Price': [present_price],
    'Driven_kms': [driven_kms],
    'Fuel_Type': [fuel_type],
    'Selling_type': [selling_type],
    'Transmission': [transmission],
    'Owner': [owner]
})

if st.button('Predict Price'):
    try:
        predicted_price = mod.predict(input_data)[0]
        
        # Determine if the price should be shown in lakhs or rupees
        if predicted_price >= 1:
            # Display in lakhs
            st.title(f"The predicted price of this configuration is ₹{predicted_price:.2f} lakhs")
        else:
            # Convert to rupees
            predicted_price_rupees = predicted_price * 100000
            st.title(f"The predicted price of this configuration is ₹{predicted_price_rupees:,.2f} rupees")
        
        st.write(f"Debug: Model output (INR) = {predicted_price}")  # Debugging line
        
    except Exception as e:
        st.error(f"Error during prediction: {e}")