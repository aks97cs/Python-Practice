import pandas as pd
path = '../annual-enterprise-survey-2017-financial-year-provisional-csv.csv'
data = pd.read_csv(path)
print(data.describe())