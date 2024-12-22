from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('presents.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM presents")
    data = cursor.fetchall()
    conn.close()
    return render_template('presents.html', data=data)

if __name__ == '__main__':
   app.run (host='0.0.0.0')

