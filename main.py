import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import weathercom
import json
import pyjokes
import pywhatkit
import datetime
from wikipedia import wikipedia

r = sr.Recognizer()



def voice_command_processor(ask=False):
    with sr.Microphone() as source:
        print("Listening...")
        if (ask):
            audio_playback(ask)
        audio = r.listen(source, phrase_time_limit=4)
        text = ''
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print("service is down")

        return text.lower()


def audio_playback(text):
    filename = "test.mp3"
    tts = gTTS(text=text, lang='en-us')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def execute_voice_command(text):
    if "your name" in text:
        audio_playback("I am Helex, at your service")

    elif "hai" in text:
        audio_playback("Hi there, what can I help")

    elif "weather" in text:
        city = voice_command_processor("May I know the city?")
        humidity, temp, phrase = weatherReport(city)
        audio_playback("currently in " + city + "  temperature is " + str(temp)
                       + " degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)
        print("currently in " + city + "  temperature is " + str(temp)
              + "degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)

    elif "good morning" in text:
        audio_playback("Good morning sir, have a good day ahead")

    elif "good night" in text:
        audio_playback("Good night sir, hope you had a great day")

    elif "thank you" in text:
        audio_playback("No problem sir, it's my duty")

    elif "what are you" in text:
        audio_playback(
            "I am a virtual assistant, programmed to assist who ever wants my help! currently at your service.")

    elif "play" in text:
        song = text.replace('play', '')
        audio_playback("Playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        audio_playback('Current time is ' + time)

    elif 'joke' in text:
        audio_playback(pyjokes.get_joke())

    elif 'search' in text:
        person = text.replace('search', '')
        info = wikipedia.summary(person, 1)
        audio_playback(info)
        print(info)

    elif "what can you do" in text:
        audio_playback("Lemme make this clear for you, i am a virtual assistant build to assit your daily needs more easily! again my name is HELEX, at your service.")

    elif "myself" in text:
        audio_playback("According to my information, Your name is Manikanta, born on 12th october 2005 and your Father name is Amarnath, Mother name is Sowmya! You love to explore new things daily and build something on that. You would like to build AI in the future.  ")

def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    return humidity, temp, phrase


while True:
    command = voice_command_processor()
    print(command)
    execute_voice_command(command)
