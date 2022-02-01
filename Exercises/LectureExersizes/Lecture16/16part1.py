countries = dict()
countries = {'Algeria': 37.1, 'Canada':34.9, 'Uganda': 32.9, 'Morocco': 32.7, 'Sudan': 30.9}
print(len(countries))

countrynames = []
for i in countries:
    countrynames.append(i)
countrynames.sort()
print(countrynames)

countryvalues = []
for i in countries:
    countryvalues.append(countries[i])
countryvalues.sort()
print(countryvalues)