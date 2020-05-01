#Import Libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)

#Define a secret key to encrypt and decrypt session data
app.secret_key = "hello"

#Permanent Sessions
#Session data is deleted when browser is closed. Session data is stored in a temporary directory on the server and length of session can be defined
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True #Session will last as long as it is defined above 
        user = request.form["nm"] #store data that was typed into name form through the dictionary key nm (for the input box) store in variable called user
        session["user"] = user #store user information in a session
        return redirect(url_for("user"))
    else:
        #Check if when are on login page, if we are already logged in, redirect to user page otherwise render login page with form
        if "user" in session:
            return redirect(url_for("user"))
        #Render login page
        return render_template('login.html')

@app.route("/user")
def user():
    #Check if there is any information in the session
    if "user" in session:
        user = session["user"] #Access user value after you have checked that it exists
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None) #Remove user data from session, remove session data from dictionary
    flash("You have been successfully logged out", "info") #info is the category for a message
    return redirect(url_for("login"))

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

#Redirect user to page that shows them the name they entered into the form
# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"
