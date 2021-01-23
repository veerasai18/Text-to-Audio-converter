from gtts import gtts
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="my name is chamana veerasai",lang=language,slow=false)
sp.save(audio)
playsound(audio)
print("=====audio is playing======")
