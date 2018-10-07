#import needed libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen   #to extract data from html files
from bs4 import BeautifulSoup   #bs4 = Beautiful Soup v4

url = "https://www.classiccarratings.com/auction-results?field_makecar_tid=All&field_yearcar_value%5Bmin%5D%5Byear%5D=1880&field_yearcar_value%5Bmax%5D%5Byear%5D=2001&field_modelcar_value=&field_date%5Bvalue%5D%5Bdate%5D=&sort_by=field_date_value"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

# next step is to access results table, which is not in a HTML table...