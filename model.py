import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

df = pd.read_excel("D:\GithubProject\HelioPredict\RTP_Data\solar_production.xlsx")
df_=df[['uv_index', 'cloud_cover', 'temp_c', 'humidity','wind_kph', 'power(kw)']]
df_.columns = ['uv_index', 'cloud_cover', 'temp_c', 'humidity','wind_kph', 'power(kw)']
df.head()