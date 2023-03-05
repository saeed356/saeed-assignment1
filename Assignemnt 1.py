import matplotlib.pyplot as plt

# Sample data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
india_pop = [1230.98, 1249.28, 1267.4, 1285.39, 1303.17, 1319.97, 1339.18, 1353.96, 1369.59, 1380.05, 1393.28]
china_pop = [1339.72, 1347.35, 1354.04, 1360.76, 1367.48, 1371.22, 1377.15, 1383.17, 1390.08, 1397.17, 1404.68]
us_pop = [309.35, 311.56, 313.87, 316.06, 318.43, 320.74, 323.03, 325.15, 327.17, 329.48, 331.58]
brazil_pop = [194.95, 197.5, 200.05, 202.66, 205.25, 207.84, 210.41, 212.93, 215.43, 217.79, 220.12]
japan_pop = [128.06, 127.83, 127.63, 127.44, 127.27, 127.14, 126.96, 126.79, 126.49, 126.15, 125.71]

# Line plot
plt.plot(years, india_pop, label='India')
plt.plot(years, china_pop, label='China')
plt.plot(years, us_pop, label='United States')
plt.plot(years, brazil_pop, label='Brazil')
plt.plot(years, japan_pop, label='Japan')

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.title('Population of Countries over Time')
plt.legend()

# Display plot
plt.show()

import matplotlib.pyplot as plt

# Sample data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
india_pop = [1230.98, 1249.28, 1267.4, 1285.39, 1303.17, 1319.97, 1339.18, 1353.96, 1369.59, 1380.05, 1393.28]
china_pop = [1339.72, 1347.35, 1354.04, 1360.76, 1367.48, 1371.22, 1377.15, 1383.17, 1390.08, 1397.17, 1404.68]
us_pop = [309.35, 311.56, 313.87, 316.06, 318.43, 320.74, 323.03, 325.15, 327.17, 329.48, 331.58]
brazil_pop = [194.95, 197.5, 200.05, 202.66, 205.25, 207.84, 210.41, 212.93, 215.43, 217.79, 220.12]
japan_pop = [128.06, 127.83, 127.63, 127.44, 127.27, 127.14, 126.96, 126.79, 126.49, 126.15, 125.71]

# Stacked Bar Graph
plt.bar(years, india_pop, label='India')
plt.bar(years, china_pop, bottom=india_pop, label='China')
plt.bar(years, us_pop, bottom=[india_pop[j] + china_pop[j] for j in range(len(years))], label='United States')
plt.bar(years, brazil_pop, bottom=[india_pop[j] + china_pop[j] + us_pop[j] for j in range(len(years))], label='Brazil')
plt.bar(years, japan_pop, bottom=[india_pop[j] + china_pop[j] + us_pop[j] + brazil_pop[j] for j in range(len(years))], label='Japan')

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.title('Population of Countries over Time')
plt.legend()

# Display plot
plt.show()


import matplotlib.pyplot as plt

# Sample data
countries = ['India', 'China', 'United States', 'Brazil', 'Japan']
populations = [1393.28, 1404.68, 331.58, 220.12, 125.71] # in millions
areas = [3287, 9596, 9834, 8515, 377.97] # in thousand sq. km

# Scatter plot
plt.scatter(areas, populations)

# Add labels and legend
plt.xlabel('Geographical Area (in thousand sq. km)')
plt.ylabel('Population (in millions)')
plt.title('Population and Geographical Area of Countries')
for i in range(len(countries)):
    plt.annotate(countries[i], xy=(areas[i], populations[i]), xytext=(5,5), textcoords='offset points')

# Display plot
plt.show()