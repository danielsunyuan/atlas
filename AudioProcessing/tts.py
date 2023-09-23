from os import system

def os_speech(text):

    voice = 'Bruce'
    system(f'say -v {voice} {text}')
    return

# from AppKit import NSSpeechSynthesizer
# speechSynthesizer = NSSpeechSynthesizer.alloc().initWithVoice_("com.apple.speech.synthesis.voice.Bruce")
# speechSynthesizer.startSpeakingString_('Hi! Nice to meet you!')

# if __name__ == "__main__":
#     os_speech(words='this is a test run of the inbuilt OS text to speech system...')