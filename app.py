from flask import Flask,render_template,redirect, url_for           # import flask
import pandas as pd
import random

debug=True

app = Flask(__name__)             # create an app instance
recent=dict()
like=dict()
df=pd.read_table("songs.tsv")
df=df.sort_values('Album')
if debug:
    for j in range(1000):
        sng=random.randint(0,800)
        if j%10 in like and sng not in like[j%10]:
            like[j%10].append(sng)
        else:
            like[j%10]=[sng]
        if j%10 in recent:
            recent[j%10].append(sng)
        else:
            recent[j%10]=[sng]

@app.route('/profile/<user>')
@app.route('/profile/<user>/<song>')
def main_page(user, song=None):
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
        if int(user) in recent:
            recent[int(user)].append(song_id)
        else:
            recent[int(user)]=[song_id]
            like[int(user)]=[]
    if song and int(song) in like[int(user)]:
        button_text="Unlike"
    else:
        button_text="Like"
    for i in df.index:
        if song:
            table_data=table_data+f"""<tr>
                <td>
                    <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                </td>
                <td>
                    {df['Length'][i]}
                </td>
                <td>
                    <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                </td>
                <td>
                    <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                </td>
                <td>
                    <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                </td>
            </tr>"""
        else:
            table_data=table_data+f"""<tr>
                <td>
                    <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                </td>
                <td>
                    {df['Length'][i]}
                </td>
                <td>
                    <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                </td>
                <td>
                    <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                </td>
                <td>
                    <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                </td>
            </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)

@app.route('/album/<user>/<album>')
@app.route('/album/<user>/<album>/<song>')
def album_page(user,album,song=None):
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song and int(song) in like[int(song)]:
        button_text="Unlike"
    else:
        button_text="Like"
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
    for i in df.index:
        if album==df['Album'][i]:
            if song:
                table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
            else:
                table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)


@app.route('/artist/<user>/<artist>')
@app.route('/artist/<user>/<artist>/<song>')
def artist_page(user,artist,song=None):
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song and int(song) in like[int(song)]:
        button_text="Unlike"
    else:
        button_text="Like"
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
    for i in df.index:
        if artist==df['Artist'][i]:
            if song:
                table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
            else:
                table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)


@app.route('/genre/<user>/<genre>')
@app.route('/genre/<user>/<genre>/<song>')
def genre_page(user,genre,song=None):
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song and int(song) in like[int(song)]:
        button_text="Unlike"
    else:
        button_text="Like"
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
    for i in df.index:
        if genre==df['Genre'][i]:
            if song:
                table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
            else:
                table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)



@app.route('/recent/<user>')
@app.route('/recent/<user>/<song>')
def recent_page(user,song=None):
    print(recent[int(user)])
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song and int(song) in like[int(song)]:
        button_text="Unlike"
    else:
        button_text="Like"
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
    for i in recent[int(user)]:
        if song:
            table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
        else:
            table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)


@app.route('/liked/<user>')
@app.route('/liked/<user>/<song>')
def like_page(user,song=None):
    print(like[int(user)])
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song and int(song) in like[int(song)]:
        button_text="Unlike"
    else:
        button_text="Like"
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
    for i in like[int(user)]:
        if song:
            table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
        else:
            table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)

@app.route('/mostliked/<user>')
@app.route('/mostliked/<user>/<song>')
def most_liked(user,song=None):
    table_data=""
    song_data=""
    like_link=f"/liked/{user}"+(f"/{song}" if song else "")
    recent_link=f"/recent/{user}"+(f"/{song}" if song else "")
    button_text=""
    if song and int(song) in like[int(song)]:
        button_text="Unlike"
    else:
        button_text="Like"
    like_by_song=dict()
    for user in like:
        for song in like[int(user)]:
            if song in like_by_song:
                like_by_song[song]+=1
            else:
                like_by_song[song]=1
    if song:
        song_id=int(song)
        song_data = df['Title'][song_id]+" - "+df['Artist'][song_id]
    for i in sorted(like_by_song, key=like_by_song.get, reverse=True):
        if song:
            table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}/{song}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}/{song}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}/{song}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
        else:
            table_data=table_data+f"""<tr>
                    <td>
                        <a class="song" href="/profile/{user}/{i}" style="text-decoration: none;" color="white">{df['Title'][i]}</a>
                    </td>
                    <td>
                        {df['Length'][i]}
                    </td>
                    <td>
                        <a class="artist" href="/artist/{user}/{df['Artist'][i]}" style="text-decoration: none;" color="white">{df['Artist'][i]}</a>
                    </td>
                    <td>
                        <a class="album" href="/album/{user}/{df['Album'][i]}" style="text-decoration: none;" color="white">{df['Album'][i]}</a>
                    </td>
                    <td>
                        <a class="genre" href="/genre/{user}/{df['Genre'][i]}" style="text-decoration: none;" color="white">{df['Genre'][i]}</a>
                    </td>
                </tr>"""
    return render_template('top_songs.html', table_data = table_data, song_data=song_data, like_data=button_text, recent_link=recent_link,like_link=like_link,song=song, user=user)

@app.route('/like/<user>/<song>')
def like_song(user,song):
    song=int(song)
    user=int(user)
    if user in like and song in like[user]:
        like[user].remove(song)
    elif user in like:
        like[user].append(song)
    else:
        like[user]=[song]
    return redirect(f"/profile/{user}/{song}")
if __name__ == '__main__':
   app.run(debug = True)