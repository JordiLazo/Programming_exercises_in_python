import matplotlib
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
data = pd.read_csv('train.csv')
data.head()
print(data.head())
a = data.iloc[3,1:].values
a = a.reshape(28,28).astype('uint8')
plt.imshow(a)
df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]
x_train, y_train, x_test, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state = 4)
x_train.head()



