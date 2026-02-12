import pandas as pd

df = pd.read_csv("netflix_titles.csv")
df.head()

df.info()
df.isnull().sum()
df.duplicated().sum()

#-------------------------------------------#
# 1.Handling Missing Values #
#-------------------------------------------#

# Fill missing director with 'Unknown'
df['director'] = df['director'].fillna('Unknown')

# Fill missing cast with 'Not Available'
df['cast'] = df['cast'].fillna('Not Available')

# Fill missing country with mode
df['country'] = df['country'].fillna(df['country'].mode()[0])

# Drop rows where date_added is missing
df.dropna(subset=['date_added'], inplace=True)

#-------------------------------------------#
# 2.Remove Duplicates #
#-------------------------------------------#

df = df.drop_duplicates()

#-------------------------------------------#
# 3.Standardize Column Names #
#-------------------------------------------#

df.columns = df.columns.str.lower().str.replace(" ", "_")

#-------------------------------------------#
# 4.Convert Date Format #
#-------------------------------------------#

df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

#-------------------------------------------#
# 5.Fix Data Types #
#-------------------------------------------#

df['release_year'] = df['release_year'].astype(int)

#-------------------------------------------#
# 6.Standardize Text Values #
#-------------------------------------------#

df['type'] = df['type'].str.lower()
df['country'] = df['country'].str.title()

#-------------------------------------------#
# 7.Save Cleaned Dataset #
#-------------------------------------------#

df.to_csv("cleaned_netflix_dataset.csv", index=False)
