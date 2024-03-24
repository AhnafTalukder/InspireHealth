import json
import uuid

from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from Objects.Campaign import Campaign

from datetime import timedelta
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import os
import whisper
import ssl

ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), "static", "uploads")
cpns_filename = os.path.join(os.path.dirname(__file__), "Data", "Campaigns.json")
tmp_dir = os.path.join(os.path.dirname(__file__), "tmp")


def add_captions(dst, src, name):

    ssl._create_default_https_context = ssl._create_unverified_context

    model = whisper.load_model("base")

    def extract_audio(vid, outfilename):
        clip = VideoFileClip(vid)
        resfile = os.path.join(tmp_dir, outfilename)
        clip.audio.write_audiofile(resfile, codec="libmp3lame")
        return resfile

    def transcribe_audio(aud):
        transcribe = model.transcribe(aud, task="translate")
        segments = transcribe['segments']

        for segment in segments:
            startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
            endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
            text = segment['text']
            segmentId = segment['id'] + 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

            srtFilename = os.path.join(tmp_dir, f"{name}.srt")
            with open(srtFilename, 'a', encoding='utf-8') as srtFile:
                srtFile.write(segment)

        return srtFilename

    def combine_video_audio(vid, aud):
        os.system("ffmpeg -i " + vid + " -i " + aud + " -c:v copy -c:a aac " + dst)

    audio = extract_audio(src, f"{name}.mp3")

    srtfilename = transcribe_audio(audio)

    generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
    subs = SubtitlesClip(srtfilename, generator)
    subtitles = SubtitlesClip(subs, generator)

    video = VideoFileClip(src)
    audio = AudioFileClip(src)
    result = CompositeVideoClip([video, subtitles.set_pos(('center', 'bottom'))])
    result.audio = audio

    result.write_videofile(dst, audio=True)

    combine_video_audio(dst, f"{name}.mp3")


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
        # video.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{video_name}.png"))
        video_orig_loc = os.path.join(tmp_dir, f"{video_name}.png")
        video.save(video_orig_loc)
        add_captions(os.path.join(app.config['UPLOAD_FOLDER'], f"{video_name}.mp4"), video_orig_loc, video_name)

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

        return redirect("http://127.0.0.1:5173/discover")


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
    app.run(debug=True)
