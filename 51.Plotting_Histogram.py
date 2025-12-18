import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv(r"C:\Users\jspm\Downloads\iris.csv")
values = iris["sepal_length"]
plt.hist(values,bins=30,color='lime',edgecolor='black')
plt.xlabel("Sepal length in cm")
plt.ylabel("FREQUENCY")
plt.title("Histogram")
plt.show()