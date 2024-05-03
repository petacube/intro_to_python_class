# todo: replace this with an actual task
"""
1. in USA zip code is a string of 5 numbers
eg 02110
write code to validate a string is a zip code

Solution
import re
check_if_zip_code="\d{5}"
zip_code="02120"
if len(zip_code) == 5:
    result=re.findall(check_if_zip_code,zip_code)
else:
    print("invalid zip")
if len(result) >0:
    print("valid zip")
else:
    print("invalid zip")
"""
import re

"""
2. latitude and longitude are numbers with two numbers before floating point and 
up to 4 numbers after with space and letters E or N
eg 9.3077° N, 2.3158° E
"""
#solution:
validation_expression=r"(\d\.\d+° (N|E))"
latitude="9.3077° N"
longtitude="2.3158° E"
matches = re.findall(validation_expression,latitude)
if len(matches) >0:
    print("valid latitude or langitude")

"""
3. a license plate is 4 numbers and 2 letters eg
2025FE
write code to validate 6 letter string is a license plate
"""
#solution:
validation_expression = "\d{4}[A-Z]{2}"
plate_number = "2025FE"
matches = re.findall(validation_expression,latitude)
if len(matches) >0:
    print("valid plate!")
else:
    print("invalid plate")
"""
4. American education system recognizes the following degrees:
    sceince: MA, MS, MSW), 
    professional degrees (e.g. MBA, JD, MD) or 
    doctorate degrees (e.g. PhD).
write code to validate degree is an american one 
"""

#solution:
validation_expression=r"(MA|MS|MSW|MBA|JD|MD|PhD)"
test_degree="PHD"
matches = re.findall(validation_expression,test_degree,re.IGNORECASE)
if len(matches) >0:
    print("valid degree!")
else:
    print("invalid degree")