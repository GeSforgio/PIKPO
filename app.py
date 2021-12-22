import datetime
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/main')
def main():
    connection = sqlite3.connect('sqlite_python.db')
    cur = connection.cursor()

    result = cur.execute('select * from movie')
    list = []

    for rowproxy in result:
        movie_dict = {}
        movie_dict['rating'] = rowproxy[0]
        movie_dict['name'] = rowproxy[1]
        movie_dict['release_date'] = rowproxy[2]
        movie_dict['director'] = rowproxy[3]
        list.append(movie_dict)
    return render_template('main.html', table=list)

@app.route('/review')
def review():
    return render_template('review.html', table=list)

@app.route('/get_contact', methods=['POST'])
def get_contact():
    connection = sqlite3.connect('sqlite_python.db')
    cur = connection.cursor()
    input_value_name = str(request.form.get("contact_name"))
    input_value_mail = str(request.form.get("contact_mail"))
    if input_value_name !='' and input_value_mail!='':
        date = datetime.datetime.now()
        cur.execute('insert into contact (user_name,user_mail,date) values (?,?,?)', (input_value_name,input_value_mail,date))
        connection.commit()
        return render_template('review.html')
    else:
        return render_template('review.html')

@app.route('/search', methods=['POST'])
def search():
    connection = sqlite3.connect('sqlite_python.db')
    cur = connection.cursor()
    input_value = str(request.form.get("search"))
    if input_value !='':
        result = cur.execute('select * from movie where movie match :value', {'value':input_value})
        list = []
        for rowproxy in result:
            movie_dict = {}
            movie_dict['rating'] = rowproxy[0]
            movie_dict['name'] = rowproxy[1]
            movie_dict['release_date'] = rowproxy[2]
            movie_dict['director'] = rowproxy[3]
            list.append(movie_dict)
        return render_template('main.html', table=list)
    else:
        result = cur.execute('select * from movie')
        list = []
        for rowproxy in result:
            movie_dict = {}
            movie_dict['rating'] = rowproxy[0]
            movie_dict['name'] = rowproxy[1]
            movie_dict['release_date'] = rowproxy[2]
            movie_dict['director'] = rowproxy[3]
            list.append(movie_dict)
        return render_template('main.html', table=list)

@app.route('/')
def hello():
    return render_template('hello.html', table=list)


if __name__ == '__main__':
    app.run(host="localhost", port=6666)







