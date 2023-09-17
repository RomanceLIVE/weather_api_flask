from flask import Flask, render_template

app = Flask("Website")

@app.route("/home")
# add /home to the url (http://127.0.0.1:5000/) to see the home page
def home():


    return render_template("sample.html")
    #flask is configured to look for templates in the templates folder

@app.route("/about/")
def about():
    return render_template("about.html")

app.run(debug=True)
#this will allow to see errors on the website