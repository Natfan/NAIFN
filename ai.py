from gtts import gTTS
import os
import platform
from pygame import mixer

# import vlc

# NAIFN
#   A personal psudeoAI used to answer simple questions.
#   By      Natfan     and        ryankrage77
#   https://natfan.io/ and http://ryankrage77.github.io/

opsys = ''
verbose = {
    "operating_system": False
}

mixer.init()


def getsys():
    if platform.system() == 'Windows':
        opsys = 'w'
    elif platform.system() == 'Darwin':
        opsys = 'm'
    elif platform.system() == 'Linux':
        opsys = 'l'
    else:
        opsys = 'x'
    if verbose["operating_system"]:
        print('You are currently running', platform.system() + '.', opsys)
    return opsys


def talk(speech, lang='en-us', slow=False):
    getsys()
    # if opsys == 'w':
    if True:
        audio = 'audio/' + speech + '.wav'
        tts = gTTS(text=speech, lang=lang, slow=slow)
        tts.save(audio)
        print('created a new audio file:', speech + '.wav')
        # p = vlc.MediaPlayer(audio)
        # p.play()
        # mixer.music.load(audio)
        # mixer.music.play()
        return


talk("hello there, my name is naifn and I am an artificial intelligence.", 'en-us')

name = input(">")
