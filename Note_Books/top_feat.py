import json
import pandas as pd 
df=pd.read_csv("Note_Books/Feature_Importance_Score.csv")

top_features = df[df['Importance'] > 0.01]['Feature'].tolist()

with open('Note_Books/top_features.json', 'w') as f:
    json.dump(top_features, f)

print(top_features)