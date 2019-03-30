import pandas as pd

x = [1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4 ]
y = pd.qcut(x, 3, duplicates='drop')
print(y)