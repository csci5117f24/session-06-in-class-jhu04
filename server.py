from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    with psycopg2.connect(os.environ['DATABASE_URL']) as conn:
        with conn.cursor() as cur:
            cur.execute("select * from tmp")
            return render_template('hello.html', name=cur.fetchone()[0])