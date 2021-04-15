import pandas as pd
df=pd.read_table("songs.tsv")
for i in df.index:
    print(f"<tr><td>{df['Title'][i]}</td><td>{df['Length'][i]}</td><td>{df['Artist'][i]}</td><td>{df['Album'][i]}</td><td>{df['Genre'][i]}</td><td>{df['Plays'][i]}</td></tr>")