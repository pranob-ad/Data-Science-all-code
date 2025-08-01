import pandas as pd

df = pd.read_csv('light_spotify_dataset.csv')
#print(df.head())
value_missing = df.isnull().sum()
#print(value_missing)
df_c = df.dropna(subset=['song'])
#print(df_c.isnull().sum())
df_c['Release Date']=pd.to_datetime(df_c['Release Date'],format='%Y')
#print(df_c.dtypes)
#print(df_c['Release Date'])
count = df_c.duplicated().sum()
#print(count)
#print(df_c.drop_duplicates())

'''Avg popularity by Emotion
Find which emotion are associated with the popular song'''

avg_emotion = df_c.groupby('emotion')['Popularity'].mean().sort_values
#print(avg_emotion(ascending=False))

'''Avg Energy and Danceability by Genre
Find out the most energetic and danceable genre'''

avg_genre = df_c.groupby('Genre')[['Energy', 'Danceability']].mean().sort_values(by=['Energy', 'Danceability'], ascending=[False, False])
#print(avg_genre)

#top Artist by songs count
top_artist = df_c.groupby('artist')['Popularity'].count().sort_values
#print(top_artist(ascending=False))

songs = df_c[df_c['artist']== 'Andy Williams']
#print(songs)

loud_song = df_c[['song', 'Loudness']].sort_values(by='Loudness', ascending=False).head(10)
#print(loud_song)

#how many songs released by an artist in a year
song_year = df_c.groupby(['artist', 'Release Date'])['song'].count().sort_values(ascending=False)
#print(song_year)

#hit song of the year
hit_song = df_c.groupby(df_c['Release Date'].dt.year)['song'].sum().sort_values(ascending=False)
#print(hit_song)

#top 10 song and there relation between release date and popularity :
top_10_songs = df_c.sort_values(by=['Release Date', 'Popularity'], ascending=False).head(10)
#print(top_10_songs[['song', 'Release Date', 'Popularity']])

# Most Acoustic vs. Instrumental Songs
most_acoustic = df_c[df_c['Acousticness'] > 70].sort_values(by='Acousticness', ascending=False)[['artist', 'song', 'Acousticness']].head(5)
most_instrumental = df_c[df_c['Instrumentalness'] > 70].sort_values(by='Instrumentalness', ascending=False)[['artist', 'song', 'Instrumentalness']].head(5)

print("Most Acoustic Songs:\n", most_acoustic)
print("Most Instrumental Songs:\n", most_instrumental)