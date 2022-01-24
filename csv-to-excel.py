import pandas as pd
import sys

read_file = pd.read_csv (sys.argv[1])
name = sys.argv[1] + '.xlsx'
read_file.to_excel (name, index=True, header=True)
