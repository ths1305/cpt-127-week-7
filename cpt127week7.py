import pandas as pd
#Imported matplotlib for the graphs on questions 6 and 7
import matplotlib.pyplot as plt 
from matplotlib.pyplot import pie, axis, show, title
#Converted csv file into a dictionary
data = pd.read_csv('sales_data.csv')
df = pd.DataFrame(data)
print(df) 

#Question 1
#Calculated sum of sales
sum = df['sales'].sum()
print('Total Sales: ', sum, '\n')

#Question 2
#Calculated number of sales by region
top3 = df.groupby('region')['sales'].sum().sort_values(ascending=True)
print('Sales by Region: ', top3)
print('The order is Europe, North America, Asia', '\n')

#Question 3
#Calculated number of sales by product
most_sold = df.groupby('product')['sales'].sum()
print(most_sold)
print('Bobbles sold the most', '\n')

#Question 4
#Separated the products which divides the sales among them individually
bobble = df[df['product'] == 'bobbles']['sales'].sum()
widget = df[df['product'] == 'widgets']['sales'].sum()
#Calculate revenue
bobblerev = bobble * 10.99
widgetrev = widget * 15.99
print(f"Bobbles Revenue: {bobblerev}" )
print(f"Widgets Revenue: {widgetrev}" )
print('Widgets brought in more revenue, at $51,887.85', '\n')

#Question 5
#Repeats of questions 2 and 3 respectively, any information needed here can be gauged from those
top3 = df.groupby('region')['sales'].sum().sort_values(ascending=True)
print('Sales by Region: ', top3)
print('Europe sold the least', '\n')
least_sold = df.groupby('product')['sales'].sum()
print(least_sold)
print('Widgets sold the least', '\n')

#Question 6
#Created the chart with region as x axis and sales as y axis, categorized it as a bar chart
bar_chart = df.groupby('region')['sales'].sum()
bar_chart.plot(kind='bar')
#Created title, axis labels, and a command to display the graph externally
plt.title("Sales by Region") 
plt.xlabel("Region") 
plt.ylabel("Sales") 
plt.show()

#Question 7
#Inserted the product axis and sales axis
sum = df.groupby('product')['sales'].sum()
#Created title, equal axes, categorized it as a pie chart, and inserted command to display it externally
title("Sales by Product")
axis('equal')
pie(sum, labels=sum.index)
show()
