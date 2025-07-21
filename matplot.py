#pip install matplotlib

import matplotlib.pyplot as plt

#Basic Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

#Barchart
categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

#Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Pie chart
labels = ['Python', 'Java', 'C++']
sizes = [45, 30, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Language Popularity")
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.
plt.show()

#Histogram
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='green')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()


#box plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data)
plt.title("Boxplot Example")
plt.show()

