 #using SpeechRecognition library
import speech_recognition as sr 

#defining a function that recognizes speech and converts to text
   
def SpeechRecognition():

    #adding a while loop so that user can perform doesnt terminate after one execution 
    while True:

    # Initialize the speech recognizer object and microphone
     r = sr.Recognizer()
     mic = sr.Microphone()

    # Use the default microphone as the audio source
     with mic as source:

        # Adjusst for ambient noise
        r.adjust_for_ambient_noise(source)

        # Asks user to provide audio input
        print('Speak now or say "stop listening" to quit...')

        # Records the speech provided by the user from the microphone
        audio_data = r.listen(source)

        # To let the user know that the audio is being processed
        print('Processing audio...')

        # Performs speech recognition on the audio data 
        try:
            speech = r.recognize_google(audio_data)
            print('Recognized speech:', speech)

            # To terminate the program if user provides audio input as 'stop listening'
            if speech.lower() == 'stop listening':
                break

            #if the audio cannot be recognised or understandable by the system
        except sr.UnknownValueError:
            print('Speech recognition could not understand audio')
        except sr.RequestError as e:
            print('Speech recognition error:', e)

    # Release the resources associated with the speech recognizer and microphone
    r = None
    mic = None

