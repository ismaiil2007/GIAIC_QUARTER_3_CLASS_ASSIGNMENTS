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
    elif from_unit == "Kilometers":
        if to_unit == "Meters":
            return value * 1000
        elif to_unit == "Centimeters":
            return value * 100000
        elif to_unit == "Inches":
            return value * 39370.1
        elif to_unit == "Feet":
            return value * 3280.84
    elif from_unit == "Centimeters":
        if to_unit == "Meters":
            return value / 100
        elif to_unit == "Kilometers":
            return value / 100000
        elif to_unit == "Inches":
            return value * 0.393701
        elif to_unit == "Feet":
            return value * 0.0328084
    elif from_unit == "Inches":
        if to_unit == "Meters":
            return value / 39.37
        elif to_unit == "Kilometers":
            return value / 39370.1
        elif to_unit == "Centimeters":
            return value * 2.54
        elif to_unit == "Feet":
            return value / 12
    elif from_unit == "Feet":
        if to_unit == "Meters":
            return value / 3.281
        elif to_unit == "Kilometers":
            return value / 3280.84
        elif to_unit == "Centimeters":
            return value * 30.48
        elif to_unit == "Inches":
            return value * 12
    return value  

def weight_converter(value, from_unit, to_unit):  
    if from_unit == "Kilograms":  
        if to_unit == "Grams":  
            return value * 1000  
        elif to_unit == "Pounds":  
            return value * 2.20462  
        elif to_unit == "Ounces":  
            return value * 35.274  
    elif from_unit == "Grams":
        if to_unit == "Kilograms":
            return value / 1000
        elif to_unit == "Pounds":
            return value * 0.00220462
        elif to_unit == "Ounces":
            return value * 0.035274
    elif from_unit == "Pounds":
        if to_unit == "Kilograms":
            return value / 2.20462
        elif to_unit == "Grams":
            return value * 453.592
        elif to_unit == "Ounces":
            return value * 16
    elif from_unit == "Ounces":
        if to_unit == "Kilograms":
            return value / 35.274
        elif to_unit == "Grams":
            return value * 28.3495
        elif to_unit == "Pounds":
            return value / 16
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

st.title("Unit Converter By Ismail Hussain")  

unit_type = st.selectbox("Choose unit type for conversion", ["Length", "Weight", "Temperature", "Volume"])  

if unit_type == "Length":  
    length_units = ["Meters", "Kilometers", "Centimeters", "Inches", "Feet"]  
    from_unit = st.selectbox("From Unit", length_units)  
    to_unit = st.selectbox("To Unit", length_units)  
    value = st.text_input("Enter value:")  

    if st.button("Convert"):  
        if value == "":  
            st.error("Please enter a value to convert")
        elif value:  
            converted_value = length_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")  

elif unit_type == "Weight":  
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]  
    from_unit = st.selectbox("From Unit", weight_units)  
    to_unit = st.selectbox("To Unit", weight_units)  
    value = st.text_input("Enter value:")  

    if st.button("Convert"):  
        if value == "":  
            st.error("Please enter a value to convert")
        elif value:  
            converted_value = weight_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")  

elif unit_type == "Temperature":  
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]  
    from_unit = st.selectbox("From Unit", temperature_units)  
    to_unit = st.selectbox("To Unit", temperature_units)  
    value = st.text_input("Enter value:")  

    if st.button("Convert"):  
        if value == "":  
            st.error("Please enter a value to convert")
        elif value:  
            converted_value = temperature_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")  

elif unit_type == "Volume":  
    volume_units = ["Liters", "Milliliters", "Gallons"]  
    from_unit = st.selectbox("From Unit", volume_units)  
    to_unit = st.selectbox("To Unit", volume_units)  
    value = st.text_input("Enter value:")  

    if st.button("Convert"):  
        if value == "":  
            st.error("Please enter a value to convert")
        elif value:  
            converted_value = volume_converter(float(value), from_unit, to_unit)  
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}") 

