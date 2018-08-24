from flask import Flask, render_template, request#(html파일을 넘겨주는 명령이 가능, templates 기본폴더 생성) (hmtl 5.2표준)
import sqlite3 as lite



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return "You sholdn`t be here."

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            _name = request.form["name"] 
            _lang = request.form["lang"]
            _age = request.form["age"]
            with lite.connect('users.db') as conn:
                cur = conn.cursor()
                cur.execute('insert into users(name, lang, age) values(?,?,?)', (_name, _lang, _age))
                conn.commit()
                msg = "Sign up complete"

        except:
            conn.rollback()
            msg = "Sign up failed"
        finally:
            return render_template('signup.html', msg=msg)

@app.route('/users')
def show_users():
    conn = lite.connect('./users.db')
    conn.row_factory = lite.Row
    cur = conn.cursor()
    cur.execute('select * from users;')

    rows = cur.fetchall()
    
    return render_template('users.html', rows=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

