'''
main.py
'''

from openai import OpenAI
from playsound import playsound

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input="Hai Jisna, You are awesome! Let's create something amazing together.",
)
response.write_to_file("output.mp3")

# Play the audio
playsound("output.mp3")
