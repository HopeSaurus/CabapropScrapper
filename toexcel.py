import pandas as pd

def toExcel(dict):
  df = pd.DataFrame(dict)
  df.to_excel("output.xlsx", index=False)