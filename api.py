from flask import Flask, render_template, request, redirect
import sqlite3
import pickle

app = Flask(__name__)

with open("model.pkl","rb") as file:
    model = pickle.load(file)

@app.route("/")
def index():

    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        patients=patients
    )


@app.route("/add", methods=["POST"])
def add_patient():

    full_name = request.form["full_name"]
    dob = request.form["dob"]
    email = request.form["email"]

    glucose = float(request.form["glucose"])
    haemoglobin = float(request.form["haemoglobin"])
    cholesterol = float(request.form["cholesterol"])

    prediction = model.predict(
        [[glucose, haemoglobin, cholesterol]]
    )

    if prediction[0] == 1:
        remarks = "High Risk"
    else:
        remarks = "Low Risk"

    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ))

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)