import pandas as pd 
import matplotlib.pyplot as plt 

csv_file =	pd.read_csv('.csv')
csv_file = csv_file.ix[0:,['name','chart name']]
csv_file = csv_file.set_index([''])
csv_file.plot(color ='')
plt.show()
