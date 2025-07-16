import pandas as pd
import matplotlib.pyplot as plt
data= {
    'name':['A','B','C','D'],
    'score':['10','9','8','7'] 
}
df=pd.DataFrame(data)
print("data summery")
print(df)
plt.bar(df['name'],df['score'])
plt.title('student score')
plt.xlabel('name')
plt.ylabel('score')
plt.show
