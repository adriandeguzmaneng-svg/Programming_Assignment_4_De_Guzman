# %%
import pandas as pd

# %%
df = pd.read_csv('board2.csv')
df

# %% [markdown]
# Vis = [“Name”, “Gender”, “Track”, “Math<70”]; hometown is constant as Visayas

# %%
Vis = df.loc[(df['Hometown'] == 'Visayas') & (df['Math'] < 70)]
Vis = pd.DataFrame(Vis, columns = ("Name", "Gender", "Track", "Math"))
Vis.to_csv('Vis.csv')
Vis

# %% [markdown]
# Instru = [“Name”, “GEAS”, “Electronics >70”]; where track is constant as
# Instrumentation and hometown Luzon

# %%
Instru = df.loc[(df['Hometown'] == 'Luzon') & (df['Track'] == 'Instrumentation') & (df['Electronics'] > 70)]
Instru = pd.DataFrame(Instru, columns = ("Name", "GEAS", "Electronics"))
Instru.to_csv('Instru.csv')
Instru

# %% [markdown]
# Mindy = [ “Name”, “Track”, “Electronics”, “Average >=55”]; where hometown is
# constant as Mindanao and gender Female

# %%
mindy = df.copy()
mindy["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)
Mindy = mindy.loc[(mindy['Hometown'] == 'Mindanao') & (mindy['Gender'] == 'Female') & (mindy['Average'] >= 55)]
Mindy = pd.DataFrame(Mindy, columns = ("Name", "Track", "Electronics", "Average"))
Mindy.to_csv('Mindy.csv')
Mindy

# %%
df["Average"] = df[["Math", "Electronics", "GEAS", "Communication"]].mean(axis=1)
Average = df[["Track", "Gender", "Hometown", "Average"]]
import matplotlib.pyplot as plt

# %% [markdown]
# Does chosen track in college contribute to higher average

# %%
TrackAve = Average.groupby("Track")["Average"].mean().reset_index()
plt.figure(figsize=(5, 6))
plt.bar(TrackAve['Track'], TrackAve['Average'])
plt.title("Average by Track")

# %% [markdown]
# Does gender contribute to higher average

# %%
GenderAve = Average.groupby("Gender")["Average"].mean().reset_index()
plt.figure(figsize=(5, 6))
plt.bar(GenderAve['Gender'], GenderAve['Average'])
plt.title("Average by Gender")

# %% [markdown]
# Does hometown contribute to higher average

# %%

HomeAve = Average.groupby("Hometown")["Average"].mean().reset_index()
plt.figure(figsize=(5, 6))
plt.bar(HomeAve['Hometown'], HomeAve['Average'])
plt.title("Average by Hometown")


