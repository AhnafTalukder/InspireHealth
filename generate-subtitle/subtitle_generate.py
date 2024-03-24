from datetime import timedelta
import moviepy as mpe
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import os
import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("base")

audio = "input.mp3"

# result_sp = model.transcribe(audio)
# result_en = model.transcribe(audio, task="translate")
#
#
# print("English translation:" + result_en["text"])
# print("Spanish transcript:" + result_sp["text"])



#
# with open(transcription, 'w') as file:
#     file.write("English translation:" + result_en["text"] + "\n")
#     file.write("Spanish transcription:" + result_sp["text"])



def transcribe_audio(path):
    transcribe = model.transcribe(audio, task="translate")
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srtFilename = os.path.join("/Users/lillymoo/PycharmProjects/hooHacks/InspireHealth/generate-subtitle", f"subtitles.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return srtFilename

link = "https://www.youtube.com/watch?v=nBZOuNxQ8R0&pp=ygUdNSBtaW51dG9zIGRlIGhhYmxhbmRvIGVzcGFub2w%3D"
print(transcribe_audio(link))

generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
subs = SubtitlesClip('subtitles.srt', generator)
subtitles = SubtitlesClip(subs, generator)

video = VideoFileClip("input.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("output.mp4")


video_clip = VideoFileClip("output.mp4")
audio_clip = AudioFileClip("input.mp3")
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("final.mp4")

print("done")