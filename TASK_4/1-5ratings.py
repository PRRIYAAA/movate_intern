import pandas as pd
import matplotlib.pyplot as plt


file_path = "rating_Analysis.xlsx"  
sheet_name = "Sheet1"   
df = pd.read_excel(file_path, sheet_name=sheet_name)


x = df['Ratings'] 
y = df['Count'] 

plt.figure(figsize=(8, 5))
plt.bar(x, y)
plt.title("1-5 Ratings")
plt.xlabel("ratings")  
plt.ylabel("count") 
plt.grid()
plt.show()




