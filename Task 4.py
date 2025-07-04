import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\LENOVO\Documents\Project SkillCraft\archive\US_Accidents_March23.csv")
print("Dataset loaded. Shape:", df.shape)
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Hour'] = df['Start_Time'].dt.hour
df = df.dropna(subset=['Weather_Condition', 'Start_Lat', 'Start_Lng', 'Severity'])
df_sample = df.sample(10000, random_state=1)

plt.figure(figsize=(12, 6))
sns.countplot(
    data=df_sample,
    x='Hour',
    color='skyblue'
)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(
    data=df_sample,
    x='Severity',
    order=sorted(df_sample['Severity'].unique()),
    hue='Severity',
    palette='rocket',
    legend=False
)
plt.title("Accidents by Severity Level")
plt.xlabel("Severity Level")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
top_weather = df_sample['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(
    data=df_sample[df_sample['Weather_Condition'].isin(top_weather)],
    y='Weather_Condition',
    order=top_weather,
    hue='Weather_Condition',
    palette='magma',
    legend=False
)
plt.title("Top 10 Weather Conditions in Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df_sample,
    x='Start_Lng',
    y='Start_Lat',
    alpha=0.3,
    s=10
)
plt.title("Accident Hotspots in the US (Sample of 10k)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
