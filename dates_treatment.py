import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
cd Desktop/parkinsons_project/full_run/

dates =pd.read_csv('dates.csv')
dates= np.array(dates, dtype = str)
dates =dates.reshape(dates.shape[0])
dates = pd.to_datetime(dates, format = '%m/%d/%Y')

d = np.unique(dates)
e= np.array(range(d.shape[0]))
f = [e[j] for j in range(len(d)) for i in range(len(dates)) if dates[i]==d[j]]
