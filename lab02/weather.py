# Lab02 | Nachiket Dani
#############################################################################################################################
# Q1. What is the difference between the highest and the lowest temperature values predicted for the 10 day forecast?
high_temp = 77
low_temp = 53
temp_diff = high_temp - low_temp
print("The difference between the highest and the lowest temperatures for the 10 day forecast is:", temp_diff)

#############################################################################################################################
# Q2. What is the average temperature at noon predicted for the 10 day forecast
noon_templist = [66, 69, 66, 64, 60, 60, 59, 60, 62, 63]

average_noontemp = sum(noon_templist) / len(noon_templist)
print("The average temperature at noon predicted for the next 10 days is:", average_noontemp)

#############################################################################################################################
# Q3. What is the highest temperature predicted for the 10 day forecast, converted from Fahrenheit to Celsius?
high_tempCelsius = (5/9)*(high_temp - 32)
print("The highest temperature for the next 10 days converted to Celcius is:", high_tempCelsius)