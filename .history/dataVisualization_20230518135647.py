import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


breast_cancer_data = pd.read_csv("data.csv")
head = breast_cancer_data.columns.values

print(head)
