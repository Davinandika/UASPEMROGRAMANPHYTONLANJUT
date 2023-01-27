import speech_recognition as sr 
engine = sr.Recognizer()
mic = sr.Microphone()
Hasil = ""

with mic as source:
    print("Silahkan mulai Bicara")
    rekaman = engine.listen(source)
    print("Waktu Habis")

    try:
        hasil = engine.recognize_google(rekaman, language = "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Maaf tidak di deteksi, Mohon coba lagi")
    except Exception as e:
        print (e)

text_file = open("Hasil.txt", "w")
text_file.write(hasil)
text_file.close()
