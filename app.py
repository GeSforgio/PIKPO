import datetime
from collections import defaultdict

from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

app = Flask(__name__)


@app.route('/main')
def main():
    conn = create_engine("postgresql+psycopg2://movie:movie@localhost:31000/movie")
    sql = text(
        open("views/sql_all", encoding="utf8").read()
    )
    result = conn.execute(sql)
    list = []
    for rowproxy in result:
        movie_dict = dict(rowproxy)
        list.append(movie_dict)
    return render_template('main.html', table=list)

@app.route('/review')
def review():
    return render_template('review.html', table=list)

@app.route('/get_contact', methods=['POST'])
def get_contact():
    conn = create_engine("postgresql+psycopg2://movie:movie@localhost:31000/movie")
    input_value_name = str(request.form.get("contact_name"))
    input_value_mail = str(request.form.get("contact_mail"))
    if input_value_name !='' and input_value_mail!='':
        sql = text(
            open("views/sql_insert_contact", encoding="utf8").read()
        )
        date = datetime.datetime.now()
        conn.execute(sql, name=input_value_name,mail=input_value_mail,date=date)
        return render_template('review.html')
    else:
        return render_template('review.html')

@app.route('/search', methods=['POST'])
def search():
    conn = create_engine("postgresql+psycopg2://movie:movie@localhost:31000/movie")
    input_value = str(request.form.get("search"))
    if input_value !='':
        sql = text(
            open("views/sql_search", encoding="utf8").read()
        )
        result = conn.execute(sql, string=input_value)
        list = []
        for rowproxy in result:
            movie_dict = dict(rowproxy)
            list.append(movie_dict)

        return render_template('main.html', table=list)
    else:
        sql = text(
            open("views/sql_all", encoding="utf8").read()
        )
        result = conn.execute(sql)
        list = []
        for rowproxy in result:
            movie_dict = dict(rowproxy)
            list.append(movie_dict)
        return render_template('main.html', table=list)

@app.route('/')
def hello():
    return render_template('hello.html', table=list)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
