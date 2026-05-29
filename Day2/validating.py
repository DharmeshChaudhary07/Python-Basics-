######## Validating ##########

country = "australia"
print(country.isalpha())
country = "australia04"
print(country.isalpha())

phone = "+4923933176"
print(phone.isnumeric())
phone = "004923933176"
print(phone.isnumeric())
phone = "492393317c6"
print(phone.isnumeric())

# # doesnt work with bool
phone = "492393317.6"
print(phone.isnumeric())