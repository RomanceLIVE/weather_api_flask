from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
# add /home to the url (http://127.0.0.1:5000/) to see the home page
def home():


    return render_template("home.html")
    #flask is configured to look for templates in the templates folder

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)
#this will allow to see errors on the website