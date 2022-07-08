'''
question5_solution.py

Corresponding solution file for question5.py.

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


# Write a Python script that generates an image with the following listed 
# characteristics. Write your script in the file `question5.py` in the folder 
# `question5`. 
#
# Read the jpg file `walkie-talkie.jpg` within the `img` folder in the `question5` 
# folder into a numpy array. In order to achieve full marks, ensure your code 
# will run on another computer (even another operating system) without needing 
# to be edited.
# 
# Write a Python script that will generate a new image based on `walkie-talkie.jpg` 
# with columns 450 to 700 for all rows displaying only the blue channel and all 
# other colums left unchanged.

import numpy as np
import os
from skimage import io
import matplotlib.pyplot as plt

# open file
original = io.imread(os.path.join('img', 'walkie_talkie.jpg'))

# divide up image
cut_left = original[::, :450, ::]
cut_stripe = original[::, 450:700, ::]
cut_right = original[::, 700::, ::]

# tint stripe blue
blue_multiplier = [0, 0, 1]
cut_stripe = cut_stripe * blue_multiplier

# put stripes into single array
striped_image = np.concatenate([cut_left, cut_stripe, cut_right], axis=1)

# create window
plt.figure(figsize=(4, 4))

# show striped image
plt.imshow(striped_image)
# turn off axis and show image
plt.axis('off')
plt.show()