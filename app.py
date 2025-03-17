import streamlit as st


st.set_page_config(layout='wide', page_title="Unit Converter")

st.title("Unit Converter App🌍🧭")

st.markdown("\n")


st.markdown("### ***Convert Lenght , Weight , Time , Temperature and Speed Instantly*** 😉")

st.markdown("\n")

st.write("##### **Welcome To the  ***Unit Converter App*** 🧬📲  !!!**  \n ###### **Select the Category , enter a value and get the converted result in real-life**")

category = st.selectbox(" **Choose category**", ["Length", "Weight","Time" ,"Temperature", "Speed"])

# Conversion of Units:
def convert_units (category,value,unit):
    if category == "Length":
        if unit == "Kilometers to miles":
           return (value * 0.621371, "miles")
        elif unit == "Miles to kilometers":
            return (value / 0.621371, "km")
        elif unit == "Meters to Feet":
            return (value * 3.28084,"feet")
        elif unit == "Feet to Meters":
            return (value / 3.28084, "m")
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return (value * 2.20462,"lbs")
        elif unit =="Pounds to kilograms":
            return (value / 2.20462, "kg")
    elif category == "Time":
        if unit == "Seconds to minutes":
            return (value / 60, "minutes")
        elif unit == "Minutes to seconds":
            return( value * 60, "seconds")
        elif unit == "Minutes to hours":
            return (value / 60, "hours")
        elif unit == "Hours to minutes":
            return (value * 60, "minutes")
        elif unit == "Hours to days":
            return (value / 24, "days")
        elif unit == "Days to hours":
            return (value * 24,"hours" )
    elif category == "Temperature":
        if unit ==  "Celsius to Fahrenheit":
            return  ((value * 9/5) + 32, "°F")
        elif unit == "Fahrenheit to Celsius":
            return  ((value - 32) * 5/9, "°C")
    elif category == "Speed": 
        if unit == "Kilometers per Hour to Miles per Hour":
            return (value * 0.621371, "m/h") 
        elif unit == "Miles per Hour to Kilometers per Hour":
            return (value / 0.621371, "km/h")   
    return "Invalid Conversion"
 
if category == "Length":
    unit = st.selectbox("**Select Conversation:**",["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight": 
    unit = st.selectbox("**Selecct Conversation:**", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("**Select Conversation:**", ["Seconds to minutes","Minutes to seconds","Minutes to hours","Hours to minutes","Hours to days","Days to hours"])
elif category == "Temperature":
    unit = st.selectbox("**Select Conversion:**", ["Celsius to Fahrenheit","Fahrenheit to Celsius" ]) 
elif category == "Speed" :
    unit = st.selectbox("**Select Conversion:**", ["Kilometers per Hour to Miles per Hour", "Miles per Hour to Kilometers per Hour"])      

value = st.number_input("**Enter the value to convert:**")


if st.button("Convert"):
    result, unit_name = convert_units(category,value,unit)
    if isinstance(result,(int , float)):
        st.success(f"The Result is {result:.2f} {unit_name}  ") 
    else:
        st.error("Invalid Conversion selected")
