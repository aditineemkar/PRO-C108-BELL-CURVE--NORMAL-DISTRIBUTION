import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv("mobile_data.csv")
data = df["Avg Rating"].tolist()

a = ff.create_distplot([data], ["Avg Rating for smartphones"], show_hist= True)
a.show()

#fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height Distribution"], show_hist=False) 
#fig.show()
