import sqlite3
import eyeD3
import time

def insert(filename, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queue
                 (FILE text, SONG text, ARTIST text, TIME bigint)''')

    song_data = []
    song_data.append(filename)
    
    audiofile = eyeD3.Mp3AudioFile(filename)
    tag = audiofile.getTag()
    tag.link(filename)
    
    song_data.append(tag.getTitle())
    song_data.append(tag.getArtist())
    song_data.append(int(round(time.time() * 1000)))

    c.execute("INSERT INTO queue VALUES (?,?,?,?)", song_data)

    conn.commit()
    conn.close()

def get(filename, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM queue WHERE FILE = ?", [filename] )

    ret = c.fetchone()
    conn.close()
    return ret

def get_most_recent(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT MIN(TIME) FROM queue")
    time = c.fetchone()[0]

    c.execute("SELECT * FROM queue WHERE TIME = ?", [time])
    ret = c.fetchone()

    conn.close()
    return ret

def remove(filename, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("DELETE FROM queue WHERE FILE=?", [filename])

    conn.close()
