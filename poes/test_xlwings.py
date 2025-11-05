#%% Import Python Libraries
import xlwings as xw
import numpy as np
import pandas as pd

#%% Create a workbook excel from Python
wb = xw.Book()

#%% Define sheet to work
sheet = wb.sheets["Sheet1"]

#%% Write a cell from Python
sheet["C3"].value = "python"

#%% Call an Excel cell to Python
value = sheet["C3"].value
print(value)

#%% Define a numpy array from Python to Excel
sheet["C4"].options(np.array).value = np.array([1, 2, 3, 4, 5])

#%% Call array from Excel to Python
array = sheet["C4:G4"].value
print(array)

#%% Define a pandas dataframe from Python to Excel:
sheet["C8"].options(pd.DataFrame, expand="table", index=False).value = pd.DataFrame({"Field": ["Sacha", "Auca"],
                                                                        "Well": ["Sacha-1", "Auc-5"],
                                                                        "Oil rate (bpd)": [1000, 300]})
#%% Call a dataframe from Excel to Python
df = sheet["C8:E10"].options(pd.DataFrame, expand="table", index=False).value
print(df)