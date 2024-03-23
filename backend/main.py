import json

from flask import Flask, jsonify

from backend.Objects.Campaign import Campaign

app = Flask(__name__)


def write_campaign_json(campaigns):
    serial_data = [d.get_serial() for d in campaigns]
    jsn = json.dumps(serial_data, indent=4)
    with open("Data/Campaigns.json", "w") as outfile:
        outfile.write(jsn)


def get_campaigns_data(jsn=True):
    with open("Data/Campaigns.json", "r") as infile:
        serial_data = json.load(infile)
        if jsn:
            return serial_data
        cpns = [Campaign(d) for d in serial_data]
        return cpns



@app.route("/get_campaigns")
def get_campaigns():
    return jsonify(get_campaigns_data())


if __name__ == '__main__':
    tc = Campaign()
    tc.start = "3/22/2024"
    tc.end = "3/25/2024"
    tc.name = "Ukraine Hosptial war relif"
    tc.description = "desc"
    tc.hospital_name = "ukr nat hospital"
    tc.pledge_amount = 10000000000000
    tc.city = "Kiev"
    tc.country = "Ukraine"
    tc.contact_email = "someone@gmail.com"
    tc.paypal = "@paypaluser"
    tc.name = "test hospital"
    tc.location = "ukraine"
    tc.patients = ["patient_1"]
    campaigns = [tc]
    write_campaign_json(campaigns)
    # jsn = json.dumps(hospitals, indent=4)
    #
    # # Writing to sample.json
    # with open("Data/Hospitals.json", "w") as outfile:
    #     outfile.write(jsn)
    app.run(debug=True)
