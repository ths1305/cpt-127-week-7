import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.pyplot import pie, axis, show, title
#Converted it into a dictionary
data = pd.read_csv('sales_data.csv')
df = pd.DataFrame(data)
print(df) 

#Question 1
sum = df['sales'].sum()
print('Total Sales: ', sum, '\n')

#Question 2
top3 = df.groupby('region')['sales'].sum().sort_values(ascending=True)
print('Sales by Region: ', top3)
print('The order is Europe, North America, Asia', '\n')

#Question 3
most_sold = df.groupby('product')['sales'].sum()
print(most_sold)
print('Bobbles sold the most', '\n')

#Question 4
bobble = df[df['product'] == 'bobbles']['sales'].sum()
widget = df[df['product'] == 'widgets']['sales'].sum()
bobblerev = bobble * 10.99
widgetrev = widget * 15.99
print(f"Bobbles Revenue: {bobblerev}" )
print(f"Widgets Revenue: {widgetrev}" )
print('Widgets brought in more revenue, at $51,887.85', '\n')

#Question 5
top3 = df.groupby('region')['sales'].sum().sort_values(ascending=True)
print('Sales by Region: ', top3)
print('Europe sold the least', '\n')
least_sold = df.groupby('product')['sales'].sum()
print(least_sold)
print('Widgets sold the least', '\n')

#Question 6
bar_chart = df.groupby('region')['sales'].sum()
bar_chart.plot(kind='bar')
plt.title("Sales by Region") 
plt.xlabel("Region") 
plt.ylabel("Sales") 
plt.show()

#Question 7
sum = df.groupby('product')['sales'].sum()
title("Sales by Product")
axis('equal')
pie(sum, labels=sum.index)
show()
