# run 'jupyter notebook' in terminal

import pandas as pd
pd.__version__

data = pd.read_csv("Food_composition_dataset.csv", encoding='latin-1', sep=';', decimal=',')
data.head()

