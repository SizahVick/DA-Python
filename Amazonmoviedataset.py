import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
amazon_df = pd.read_csv(r"C:\Users\sizah\Downloads\RGN\DA\Python\Data Visualization\data.csv")

imdb_df = pd.read_csv(r"C:\Users\sizah\Downloads\RGN\DA\Python\Data Visualization\imdb_movie_dataset.csv")

imdb_df
amazon_df

# Renaming column to match imdb dataset
amazon_df = amazon_df.rename(columns={
    'title': 'Title',
    'type': 'Type',
    'genres': 'Genres',
    'releaseYear': 'Release Year',
    'imdbId': 'IMDb ID',
    'imdbAverageRating': 'IMDb Average Rating',
    'imdbNumVotes': 'IMDb Number of Votes',
    'availableCountries': 'Available Countries'
})

# Renaming columns in IMDb dataset to ensure consistency
imdb_df = imdb_df.rename(columns={
    'Rank': 'Rank',
    'Title': 'Title',
    'Genre': 'Genres',
    'Description': 'Description',
    'Director': 'Director',
    'Actors': 'Actors',
    'Year': 'Release Year',
    'Runtime (Minutes)': 'Runtime (Minutes)',
    'Rating': 'IMDb Average Rating',
    'Votes': 'IMDb Number of Votes'
})
print(amazon_df.dtypes)
print(imdb_df.dtypes)

# Coverting datatype to numeric
amazon_df['Release Year'] = pd.to_numeric(amazon_df['Release Year'], errors='coerce')
amazon_df['IMDb Average Rating'] = pd.to_numeric(amazon_df['IMDb Average Rating'], errors='coerce')
imdb_df['Release Year'] = pd.to_numeric(imdb_df['Release Year'], errors='coerce')
imdb_df['IMDb Average Rating'] = pd.to_numeric(imdb_df['IMDb Average Rating'], errors='coerce')

# Handling missing values
# Dropping rows  with missing vaules
amazon_df.dropna(subset=["Title"], inplace=True)
imdb_df.dropna(subset=["Title"], inplace=True)

# Joins (merging dataset)
merged_df = pd.merge(amazon_df, imdb_df, on="Title", how= "inner")
print(merged_df.dtypes)

# Filling NaN values in relevant columns with zeros to simplify analysis
merged_df.fillna({'IMDb Average Rating':0, 'IMDb Number of Votes':0, 'Runtime (Minutes)':0}, inplace=True)

# Dropping "_y" columns and renaming "_x" columns
merged_df = merged_df.drop(columns=['Genres_y', 'Release Year_y', 'IMDb Average Rating_y', 'IMDb Number of Votes_y'])
merged_df = merged_df.rename(columns={
    'Genres_x': 'Genres',
    'Release Year_x': 'Release Year',
    'IMDb Average Rating_x': 'IMDb Average Rating',
    'IMDb Number of Votes_x': 'IMDb Number of Votes'
})

# Calculating average IMDb rating for each genre
genre_ratings = merged_df.groupby('Genres')['IMDb Average Rating'].mean().sort_values(ascending=False)
print("Top Genres by Average IMDb Rating: \n", genre_ratings.head(10))


# Visualization

# Visualize top genres by average rating using a bar plot
top_genres = genre_ratings.head(10)
top_genres.plot(kind='bar', color='blue', title='Top 10 Genres by Average IMDb Rating')
plt.xlabel('Genres')
plt.ylabel('Average IMDb Rating')
plt.show()

# Calculating average runtime by genre
genre_runtime = merged_df.groupby('Genres')['Runtime (Minutes)'].mean().sort_values(ascending=False)
print("\nTop Genres by Average Runtime:\n", genre_runtime.head(10))

# plotting average runtime by genre
top_runtimes = genre_runtime.head(10)
top_runtimes.plot(kind='bar', color='orange', title='Top 10 Genres by Average Runtime')
plt.xlabel('Genres')
plt.ylabel('Average Runtime (Minutes)')
plt.show()

# Save merged_df to a CSV file
merged_df.to_csv("merged_data.csv", index=False)
print("DataFrame saved to 'merged_data.csv'")

# Calculating average IMDb rating per genre and type
pivot_top_10_genres = merged_df.pivot_table(
    index='Genres',
    columns='Type',
    values='IMDb Average Rating',
    aggfunc='mean'
)

# Sort the genres by average IMDb rating and select the top 10
top_10_genres = pivot_top_10_genres.mean(axis=1).sort_values(ascending=False).head(10).index
pivot_top_10_filtered = pivot_top_10_genres.loc[top_10_genres]

# Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(pivot_top_10_filtered,annot=True, cmap="YlGnBu", fmt=".1f")
plt.title("Average IMDb Rating by Genre (Top 10)")
plt.xlabel("Type")
plt.ylabel("Genre")
plt.show()