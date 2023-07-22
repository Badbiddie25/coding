# 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the 
# default country

def describe_city(name_city, name_country="Europe"):
    print(name_city + " is in "+ name_country)
    print(f"{name_city} is in {name_country}")
describe_city('London', 'UK')
describe_city('Amsterdam',"Netherlands")
describe_city('Vienna', 'Austria')
