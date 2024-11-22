import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading data
merged_df = pd.read_csv("merged_data.csv")

# Basic pivot table - Average IMDb Rating by Genre and Type
pivot_genre_type = merged_df.pivot_table(index='Genres', columns='Type', values='IMDb Average Rating', aggfunc='mean').head(10)
print("Average IMDb Rating by Genre and Type:\n", pivot_genre_type)

# Visualization
# Heatmap for Average IMDb Rating by Genre and Type
plt.figure(figsize=(10,6))
sns.heatmap(pivot_genre_type, annot=True, cmap='coolwarm', fmt=".1f")
plt.title("Average IMDb Rating by Genre and Type")
plt.show()