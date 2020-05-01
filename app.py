#Import Libraries
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"] #store data that was typed into name form through the dictionary key nm (for the input box) store in variable called user
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

#------------------- OLD CODE --------------------
# from flask import Flask, render_template
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# mysql = MySQL(app)

# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Thecheezer1!'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_DB'] = 'drinks_database'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #Column can be keys and vlaues can be values in that particular column

# @app.route("/")
# def index():
#     cur = mysql.connection.cursor()
#     cocktails = cur.execute("SELECT name FROM drinks_database.cocktails")
#     # return render_template('index.html')
#     return cocktails

# if __name__ == "__main__":
#     app.run(debug=True)


#Import database
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Thecheezer1!",
#     database="drinks_database"
# )


