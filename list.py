countries = ["United States", "United Kingdom", "Germany", "France", "Italy", "Kenya", "Uganda", "Mali"]
long_countries = [country for country in countries if len(country) > 5]
print(f"The countries with names longer than 5 characters are: {long_countries}")
