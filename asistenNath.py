import speech_recognition as sr
import webbrowser
import datetime
import time
from gtts import gTTS
import os

nama_pengguna = "Boss Nath"

# ubah teks ke suara (tts)
def speak(text):
    tts = gTTS(text=text, lang='id')
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # Windows
    time.sleep(2)  # waktu tunggu respon

# ucap salam
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        speak(f"Selamat Pagi, {nama_pengguna}!")
        print(f"Selamat Pagi, {nama_pengguna}!")
    elif 12 <= currentH < 18:
        speak(f"Selamat Siang, {nama_pengguna}!")
        print(f"Selamat Siang, {nama_pengguna}!")
    else:
        speak(f"Selamat Malam, {nama_pengguna}!")
        print(f"Selamat Malam, {nama_pengguna}!")

# dengar perintah suara
def myCommand():
    """Mendengarkan perintah suara"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ayy: Saya siap mendengar perintah...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio, language='id-ID').lower()
        print(f'{nama_pengguna}: {command}\n')
    except sr.UnknownValueError:
        print('Ayy: Saya tidak mendengar perintah dengan jelas, coba lagi!')
        return myCommand()
    return command

# list perintah
def assistant(command):
    """Menjalankan perintah berdasarkan input suara"""
    if 'halo' in command:
        speak(f"Halo {nama_pengguna}! Ada yang bisa saya bantu?")
        print(f'Ayy: Halo {nama_pengguna}! Ada yang bisa saya bantu?')
    
    elif 'buka google' in command:
        speak("Membuka Google")
        print('Ayy: Google telah dibuka!')
        webbrowser.open('https://www.google.com')
    
    elif 'cari di google' in command:
        search_query = command.replace('cari di google', '').strip()
        speak(f"Saya mencari {search_query} di Google.")
        print(f'Ayy: Saya mencari {search_query} di Google.')
        webbrowser.open(f'https://www.google.com/search?q={search_query}')
    
    elif 'buka youtube' in command:
        speak("Membuka YouTube")
        print('Ayy: YouTube telah dibuka!')
        webbrowser.open('https://www.youtube.com')

    elif 'buka kamera' in command:
        speak("Membuka Kamera")
        print('Ayy: Kamera telah dibuka!')
        os.system('start microsoft.windows.camera:')

    elif 'buka vscode' in command:
        speak("Membuka VS Code")
        print('Ayy: VS Code telah dibuka!')
        os.system('code')
    
    elif 'cari di youtube' in command:
        search_query = command.replace('cari di youtube', '').strip()
        speak(f"Saya mencari {search_query} di YouTube.")
        print(f'Ayy: Saya mencari {search_query} di YouTube.')
        webbrowser.open(f'https://www.youtube.com/results?search_query={search_query}')

    elif 'buka web saya' in command:
        speak(f"Saya membuka web {nama_pengguna}.")
        print(f'Ayy: Saya membuka web {nama_pengguna}.')
        webbrowser.open('https://vnath-portfolio.vercel.app')
    
    elif 'jam berapa sekarang' in command:
        waktu_sekarang = datetime.datetime.now().strftime('%H:%M')
        speak(f"Sekarang jam {waktu_sekarang}")
        print(f'Ayy: Sekarang jam {waktu_sekarang}')
    
    elif 'terima kasih' in command:
        speak(f"Sama-sama, {nama_pengguna}! Senang bisa membantu. Sampai jumpa!")
        print(f'Ayy: Sama-sama, {nama_pengguna}! Senang bisa membantu. Sampai jumpa!')
        exit()
    else:
        print('Ayy: Maaf, saya tidak mengerti perintah tersebut.')

# salam saat program dimulai
greetMe()
speak("Saya siap mendengar perintah...")

# Loop agar program terus berjalan
while True:
    assistant(myCommand())
    time.sleep(2)  # waktu tunggu respon
