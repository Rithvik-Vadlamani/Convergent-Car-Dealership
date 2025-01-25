from flask import Flask, render_template, redirect, url_for
import requests

response = requests.get("https://dealership.naman.zip/cars")
cars = response.json()

app = Flask(__name__)

lenCars = (int)(len(cars)/4)
lenCars = lenCars*4

for s in range(lenCars):
    min_idx = s
    for i in range(s + 1, lenCars):
        if cars[i]["price"] < cars[min_idx]["price"]:
            min_idx = i
    (cars[s]["price"], cars[min_idx]["price"]) = (cars[min_idx]["price"], cars[s]["price"])

for i in range(0,lenCars):
    cars[i]["price"] = "{:,}".format(cars[i]["price"])

@app.route("/")
def index():
    return render_template("home.html", carList=cars, length=lenCars)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
