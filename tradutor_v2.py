# Importar recursos
from translate import Translator
import speech_recognition as sr
import pyttsx3

print('-' * 15, 'TRADUTOR 2.0', '-' * 15)

# Inicializa o mecanismo de sistese de voz.
motor_de_sistese_de_fala = pyttsx3.init()

# Obtém todas as vozes disponíveis no sistema
voices = motor_de_sistese_de_fala.getProperty('voices')

# Define a voz a ser usada pelo robô como a segunda voz
motor_de_sistese_de_fala.setProperty('voice', voices[1].id)


# Define uma função para reconhecer a fala do usuário.
def reconhecer_fala(idioma_de_entrada):
    # Inicializa o reconhecedor de fala.
    microfone = sr.Recognizer()
    # Configura o microfone como fonte de áudio.
    with sr.Microphone() as source:
        # Ajusta o reconhecimento para o ruído ambiente.
        microfone.adjust_for_ambient_noise(source)
        print('Diga o que quer Traduzir: ')
        # Escuta o áudio do microfone.
        audio = microfone.listen(source)
        # Tenta reconhecer a fala três vezes.
        for _ in range(3):
            try:
                # Reconhece a fala do usuário usando o Google Speech Recognition.
                frase_reconhecida = microfone.recognize_google(audio, language=idioma_de_entrada)
                print(f'Você disse: {frase_reconhecida}')
                # Retorna a frase
                return frase_reconhecida
            except:
                pass
        print('Não entendi o que você disse :(')
        return None


# Traduz a frase reconhecida pelo usuário.
def tradutor(idioma_de_entrada_do_usuario, idioma_de_saida_do_usuario):
    # Inicializa o tradutor com os idiomas de entrada e saída.
    translator = Translator(from_lang=idioma_de_entrada_do_usuario, to_lang=idioma_de_saida_do_usuario)
    # Chama a função para reconhecer a fala do usuário
    frase_original = reconhecer_fala(idioma_de_entrada_do_usuario)
    # Traduz a frase reconhecida pelo tradutor.
    frase_traduzida_pelo_tradutor = translator.translate(frase_original)
    return frase_traduzida_pelo_tradutor


"""Define um dicionário de idiomas suportados com as correspondências de idiomas.
Solicita ao usuário o idioma de entrada e de saída, verificando se estão na lista de idiomas suportados."""


idiomas = {'português': 'pt-br', 'inglês': 'en-us', 'alemão': 'de'}

print('Lista de idiomas suportados')
print('-'*15)
print('''
1-Inglês
2-Alemão
3-Português''')
print('-'*15)

idioma_entrada = input('Digite i idioma de ENTRADA: ').lower()
while idioma_entrada not in idiomas.keys():
    print('IDIOMA INVÁLIDO! DIGITE: PORTUGUÊS, INGLÊS OU ALEMÃO.')
    idioma_entrada = input('Digite i idioma de ENTRADA: ').lower()

idioma_saida = input('Digite i idioma de ENTRADA: ').lower()
while idioma_saida not in idiomas.keys():
    print('IDIOMA INVÁLIDO! DIGITE: PORTUGUÊS, INGLÊS OU ALEMÃO.')
    idioma_saida = input('Digite i idioma de ENTRADA: ').lower()

# Chama a função tradutor com os idiomas de entrada e saída selecionados pelo usuário
frase = tradutor(idiomas[idioma_entrada], idiomas[idioma_saida])

# Usa o motor de síntese de fala para falar a frase traduzida.
motor_de_sistese_de_fala.say(frase)
print(f'A Frase traduzida de {idioma_entrada} para {idioma_saida} é {frase}')
motor_de_sistese_de_fala.runAndWait()
motor_de_sistese_de_fala.stop()
