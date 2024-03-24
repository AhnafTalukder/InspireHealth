import json
import os
import uuid

from flask import Flask, request, jsonify, redirect
from werkzeug.utils import secure_filename
from flask_cors import CORS
from Objects.Campaign import Campaign

ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), "static", "uploads")
cpns_filename = os.path.join(os.path.dirname(__file__), "Data", "Campaigns.json")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_video', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # if 'file' not in request.files:
        #     return redirect("http://localhost:5173")
        # file = request.files['file']
        # # If the user does not select a file, the browser submits an
        # # empty file without a filename.
        # if file.filename == '':
        #     return redirect("http://localhost:5173")
        #
        # if not allowed_file(file.filename):
        #     return redirect("http://localhost:5173")
        #
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img = request.files["image"]
        img_name = str(uuid.uuid4())
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{img_name}.png"))

        video = request.files["video"]
        video_name = str(uuid.uuid4())
        video.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{video_name}.png"))

        c = Campaign()
        c.start = request.form["start_date"]
        c.end = request.form["end_date"]
        c.name = request.form["campaign_name"]
        c.description = request.form["description"]
        c.hospital_name = request.form["hospital_name"]
        c.pledge_amount = request.form["pledge_amount"]
        c.city = request.form["city_name"]
        c.country = request.form["country_name"]
        c.contact_email = request.form["contact_email"]
        c.paypal = request.form["paypal_user"]
        c.image_link = f"/static/uploads/{img_name}.png"
        c.video_link = f"/static/uploads/{video_name}.png"
        c.id = str(uuid.uuid4())

        cpns = get_campaigns_data(jsn=False)
        cpns.append(c)
        write_campaign_json(cpns)

        return redirect("http://localhost:5173/discover")


def write_campaign_json(campaigns):
    serial_data = [d.get_serial() for d in campaigns]
    jsn = json.dumps(serial_data, indent=4)
    with open(cpns_filename, "w") as outfile:
        outfile.write(jsn)


def get_campaigns_data(jsn=True):
    with open(cpns_filename, "r") as infile:
        serial_data = json.load(infile)
        if jsn:
            return serial_data
        cpns = [Campaign(d) for d in serial_data]
        return cpns


@app.route("/get_campaigns")
def get_campaigns():
    return jsonify(get_campaigns_data())


@app.route("/get_id")
def get_id():
    id = request.args.get("cid")
    cpns = get_campaigns_data(jsn=False)
    for cpn in cpns:
        if cpn.id == id:
            return jsonify(cpn.get_serial())

    return jsonify("No matching ID")

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
    tc.image_link = "test_image.png"
    tc.video_link = "test_video.mp4"
    tc.id = "test_id"
    campaigns = [tc]
    write_campaign_json(campaigns)
    app.run(debug=False)
