import streamlit as st


st.set_page_config(layout='wide', page_title="Unit Converter")

st.title("Unit Converter App🌍🧭")

st.markdown("### Convert Lenght , Weight , and Time instantly 😉")

st.write("###### Welcome To the  ''Unit Converter App '' !!!  \n ###### Select the Category , enter a value and get the converted result in real-life")

category = st.selectbox(" Choose category", ["Length", "Weight","Time"])

# Conversion of Units:
def convert_units (category,value,unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit =="Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24 
    return "Invalid Conversion"
 
if category == "Length":
    unit = st.selectbox("Select Conversation:",["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight": 
    unit = st.selectbox("Selecct Conversation:", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversation:", ["Seconds to minutes","Minutes to seconds","Minutes to hours","Hours to minutes","Hours to days","Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category,value,unit)
    if isinstance(result,(int , float)):
        st.success(f"The Result is {result:.2f}") 
    else:
        st.error("Invalid Conversion selected")
