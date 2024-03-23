import json

from flask import Flask, render_template, url_for

from backend.Objects.Hospital import Hospital
from backend.Objects.Patient import Patient

app = Flask(__name__)


@app.route("/hospitals")
def hospitals():
    pass

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


def write_hospital_json(hospitals):
    hospitals_serial = [hospital.get_serial() for hospital in hospitals]
    jsn = json.dumps(hospitals_serial, indent=4)
    with open("Data/Hospitals.json", "w") as outfile:
        outfile.write(jsn)


def get_hospitals():
    with open("Data/Hospitals.json", "r") as infile:
        hospitals_serial = json.load(infile)
        hospitals = [Hospital(hospital_serial) for hospital_serial in hospitals_serial]
        return hospitals


def write_patient(patient):
    jsn = json.dumps(patient.get_serial(), indent=4)
    with open(f"Data/Patients/{patient.id}.json", "w") as outfile:
        outfile.write(jsn)


def get_patient_from_id(patient_id):
    with open(f"Data/Patients/{patient_id}.json", "r") as infile:
        patient_serial = json.load(infile)
        patient = Patient(patient_serial)
        return patient


if __name__ == '__main__':
    test_hospital = Hospital()
    test_hospital.name = "test hospital"
    test_hospital.location = "ukraine"
    test_hospital.patients = ["patient_1"]
    test_hospital.curr_donations = 5
    test_hospital.donation_goal = 10
    hospitals = [test_hospital]
    write_hospital_json(hospitals)
    # jsn = json.dumps(hospitals, indent=4)
    #
    # # Writing to sample.json
    # with open("Data/Hospitals.json", "w") as outfile:
    #     outfile.write(jsn)
    app.run(debug=True)
