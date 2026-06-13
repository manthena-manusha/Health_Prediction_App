from flask import Flask, render_template, request, redirect
import oracledb

app = Flask(__name__)

def get_connection():
    return oracledb.connect(
        user="system",
        password="YOUR_PASSWORD",
        dsn="localhost/XEPDB1"
    )

@app.route('/')
def index():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT patient_id,
               full_name,
               dob,
               email,
               glucose,
               haemoglobin,
               cholesterol,
               remarks
        FROM patients
        ORDER BY patient_id
    """)

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'index.html',
        patients=patients
    )

@app.route('/add', methods=['POST'])
def add_patient():

    full_name = request.form['full_name']
    dob = request.form['dob']
    email = request.form['email']
    glucose = request.form['glucose']
    haemoglobin = request.form['haemoglobin']
    cholesterol = request.form['cholesterol']

    remarks = "Prediction Pending"

    conn = get_connection()
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
        VALUES
        (
            :1,
            TO_DATE(:2,'YYYY-MM-DD'),
            :3,
            :4,
            :5,
            :6,
            :7
        )
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

    cursor.close()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)