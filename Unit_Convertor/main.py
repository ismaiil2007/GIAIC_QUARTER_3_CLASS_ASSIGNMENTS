import streamlit as st

def length_converter(value, from_unit, to_unit):  
    if from_unit == "Meters":  
        if to_unit == "Kilometers":  
            return value / 1000  
        elif to_unit == "Centimeters":  
            return value * 100  
        elif to_unit == "Inches":  
            return value * 39.37  
        elif to_unit == "Feet":  
            return value * 3.281  
    return value  # If no conversion matches, return the same value  

def weight_converter(value, from_unit, to_unit):  
    if from_unit == "Kilograms":  
        if to_unit == "Grams":  
            return value * 1000  
        elif to_unit == "Pounds":  
            return value * 2.20462  
        elif to_unit == "Ounces":  
            return value * 35.274  
    elif from_unit == "Pounds":  
        if to_unit == "Kilograms":  
            return value / 2.20462  
        elif to_unit == "Grams":  
            return value * 453.592  
        elif to_unit == "Ounces":  
            return value * 16  
    return value  

def temperature_converter(value, from_unit, to_unit):  
    if from_unit == "Celsius":  
        if to_unit == "Fahrenheit":  
            return (value * 9/5) + 32  
        elif to_unit == "Kelvin":  
            return value + 273.15  
    elif from_unit == "Fahrenheit":  
        if to_unit == "Celsius":  
            return (value - 32) * 5/9  
        elif to_unit == "Kelvin":  
            return (value - 32) * 5/9 + 273.15  
    elif from_unit == "Kelvin":  
        if to_unit == "Celsius":  
            return value - 273.15  
        elif to_unit == "Fahrenheit":  
            return (value - 273.15) * 9/5 + 32  
    return value  

def volume_converter(value, from_unit, to_unit):  
    if from_unit == "Liters":  
        if to_unit == "Milliliters":  
            return value * 1000  
        elif to_unit == "Gallons":  
            return value * 0.264172  
    elif from_unit == "Milliliters":  
        if to_unit == "Liters":  
            return value / 1000  
        elif to_unit == "Gallons":  
            return value / 3785.41  
    elif from_unit == "Gallons":  
        if to_unit == "Liters":  
            return value * 3.78541  
        elif to_unit == "Milliliters":  
            return value * 3785.41  
    return value  

# Title of the app  
st.title("Unit Converter By Ismail Hussain")  

# Unit selection  
unit_type = st.selectbox("Choose unit type for conversion", ["Length", "Weight", "Temperature", "Volume"])  

if unit_type == "Length":  
    length_units = ["Select Unit","Meters", "Kilometers", "Centimeters", "Inches", "Feet"]  
    from_unit = st.selectbox("From Unit", length_units)  
    to_unit = st.selectbox("To Unit", length_units)  
    value = st.text_input("Enter value:")  # Allow any input without restrictions  

    if st.button("Convert"):  
        if value:  
            converted_value = length_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")
        elif value == "" :
            st.error("Please enter a value to convert")        

elif unit_type == "Weight":  
    weight_units = ["Select Unit","Kilograms", "Grams", "Pounds", "Ounces"]  
    from_unit = st.selectbox("From Unit", weight_units)  
    to_unit = st.selectbox("To Unit", weight_units)  
    value = st.text_input("Enter value:")  # Allow any input without restrictions  

    if st.button("Convert"):  
        if value:  
            converted_value = weight_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")  
        elif value == "" :
            st.error("Please enter a value to convert")      

elif unit_type == "Temperature":  
    temperature_units = ["Select Unit","Celsius", "Fahrenheit", "Kelvin"]  
    from_unit = st.selectbox("From Unit", temperature_units)  
    to_unit = st.selectbox("To Unit", temperature_units)  
    value = st.text_input("Enter value:")  # Allow any input without restrictions  

    if st.button("Convert"):  
        if value:  
            converted_value = temperature_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")  
        elif value == "" :
            st.error("Please enter a value to convert")      

elif unit_type == "Volume":  
    volume_units = ["Select Unit","Liters", "Milliliters", "Gallons"]  
    from_unit = st.selectbox("From Unit", volume_units)  
    to_unit = st.selectbox("To Unit", volume_units)  
    value = st.text_input("Enter value:")  # Allow any input without restrictions  

    if st.button("Convert"):  
        if value:  
            converted_value = volume_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}") 
        elif value == "" :
            st.error("Please enter a value to convert")    
