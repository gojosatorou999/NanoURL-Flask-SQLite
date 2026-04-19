import sqlite3
import string
import random
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_id TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(chars) for _ in range(length))
        conn = get_db_connection()
        res = conn.execute('SELECT id FROM urls WHERE short_id = ?', (short_id,)).fetchone()
        conn.close()
        if not res:
            return short_id

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        
        if not original_url:
            flash('URL is required!')
            return redirect(url_for('index'))

        if not (original_url.startswith('http://') or original_url.startswith('https://')):
            original_url = 'http://' + original_url

        short_id = generate_short_id()
        
        conn = get_db_connection()
        conn.execute('INSERT INTO urls (original_url, short_id) VALUES (?, ?)',
                     (original_url, short_id))
        conn.commit()
        conn.close()

        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_url(short_id):
    conn = get_db_connection()
    url_data = conn.execute('SELECT original_url FROM urls WHERE short_id = ?',
                           (short_id,)).fetchone()
    conn.close()

    if url_data:
        return redirect(url_data['original_url'])
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
