from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)


@app.route("/")
# add /home to the url (http://127.0.0.1:5000/) to see the home page
def home():
    return render_template("home.html", data=stations.to_html())
    # flask is configured to look for templates in the templates folder


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # change port to avoid port conflict

# this will allow to see errors on the website
