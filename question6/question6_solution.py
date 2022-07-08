'''
question6_solution.py

Corresponding solution file for question6.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

See the README for a full description of the desired plot.


TOTAL POINTS AVAILABLE: 10 


Code Functionality (7)
7 points - desired plot is generated and code is efficient and Pythonic

5-6 points - desired plot is generated, but code could be significantly 
improved to be more Pythonic

3-4 points - plot has some errors

1-2 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question



Code Readability (3)
3 points - Well commented, clear code 

1-2 points - Some issues related to comments or issues such as variable 
names could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand

'''

# Write a Python script that reads in the csv file `data.csv` and generates 
# a boxplot as shown in the image in ./img. *[10 points]*
# 
# Read the CSV file `data.csv` into a numpy array (hint: the delimiter in the 
# file is `','`). In order to achieve full marks, ensure your code will run on 
# another computer (even another operating system) without needing to be edited.
# 
# Create a boxplot using matplotlib using the data in the 5th column of the csv 
# file in ./csv. Set the notch to be `True` and change the symbols of the outliers 
# to be blue diamonds, `'bD'`. Set the plot title and labels to match the image 
# (Question 6 Plot, Input Data, Values).


import matplotlib.pyplot as plt
import numpy as np
import os

# read csv file into numpy array
csv_data = np.genfromtxt(os.path.join('csv', 'data.csv'), delimiter=',')


# create boxplot of column 4 (the fifth column)
plt.boxplot(csv_data[:, 4], notch=True, sym='bD')

# add a title
plt.title('Question 6 Plot')
# x and y axis labels
plt.xlabel('Input Data')
plt.ylabel('Values')
# show the plot
plt.show()