import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import openai


audio = sr.Recognizer()
maquina = pyttsx3.init()

def listen_comand():
    comando = ""
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'jarvis' in comando:
                comando = comando.replace('jarvis', '')
                maquina.say(comando)
                maquina.runAndWait()

    except Exception as e:
        print(f'Um erro inesperado aconteceu: {e}')

    return comando

def execute_command():
    comando = listen_comand()
    if 'procure por' in comando or 'pesquise por' in comando:
        procurar = comando.replace('procure por', '').replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, sentences=2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    else:
        pass


while True:
    execute_command()