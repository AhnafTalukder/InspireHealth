from datetime import timedelta
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import os
import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("base")

def extract_audio(vid):
    clip = VideoFileClip(vid)
    clip.audio.write_audiofile(f"input.mp3")
    return "input.mp3"

def transcribe_audio(aud):
    transcribe = model.transcribe(aud, task="translate")
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srtFilename = os.path.join(os.path.dirname(__file__), f"subtitles.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return srtFilename

def combine_video_audio(vid, aud):
    os.system("ffmpeg -i " + vid + " -i " + aud + " -c:v copy -c:a aac final.mp4")

audio = extract_audio("input.mp4")

print(transcribe_audio(audio))

generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
subs = SubtitlesClip('subtitles.srt', generator)
subtitles = SubtitlesClip(subs, generator)

video = VideoFileClip("input.mp4")
audio = AudioFileClip("input.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])
result.audio = audio

result.write_videofile("output.mp4", audio=True)

combine_video_audio("output.mp4", "input.mp3")
