from collections import defaultdict

from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

app = Flask(__name__)



@app.route('/')
def ind():
    conn = create_engine("postgresql+psycopg2://movie:movie@localhost:31000/movie")
    sql = text(
        open("views/sql_all", encoding="utf8").read()
    )
    result=conn.execute(sql)
    list = []
    for rowproxy in result:
        movie_dict = dict(rowproxy)
        list.append(movie_dict)
    #list=get_anime()
    return render_template('main.html',table=list)

@app.route('/search',methods=['POST'])
def search():
    conn = create_engine("postgresql+psycopg2://movie:movie@localhost:31000/movie")
    kok=str(request.form.get("comment"))
    sql = text(
        open("views/sql_search", encoding="utf8").read()
    )
    result = conn.execute(sql,string =kok)
    list = []
    for rowproxy in result:
        movie_dict = dict(rowproxy)
        list.append(movie_dict)
    # list=get_anime()
    return render_template('main.html', table=list)
if __name__ == '__main__':
    app.run(host="localhost",port=6666)
