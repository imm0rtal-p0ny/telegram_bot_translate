import speech_recognition as sr
from pydub import AudioSegment
from os import remove


def convert_odd_to_wav(path):
    song = AudioSegment.from_file(path)
    remove(path)
    path = path.replace('.ogg', '.wav')
    with open(path, 'wb') as f:
        song.export(f, format='wav')

    return path


def audio_to_text(name_file):
    name_file = convert_odd_to_wav(name_file)
    song = sr.Recognizer()
    with sr.AudioFile(name_file) as source:
        audio = song.record(source)
    try:
        text = song.recognize_google(audio_data=audio, language='uk-UA')
    except (sr.UnknownValueError, sr.RequestError):
        text = 'Непонятно говорить'
    remove(name_file)

    return text


if __name__ == "__main__":
    print(audio_to_text('audio_2023-01-23_04-56-21.ogg'))

