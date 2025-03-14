# 🎙️ Voice Assistant - Asisten Virtual Berbasis Suara

Asisten virtual berbasis **Python** yang dapat menerima perintah suara dalam Bahasa Indonesia dan memberikan respons menggunakan **Google Text-to-Speech (gTTS)**. Program ini dapat membuka website, menampilkan waktu, serta mengontrol kamera.

## ✨ Fitur Utama
✅ **Salam Otomatis** berdasarkan waktu
✅ **Pengenalan Suara** menggunakan `speech_recognition`
✅ **Text-to-Speech** dalam Bahasa Indonesia dengan `gTTS`
✅ **Membuka Website** seperti Google & YouTube
✅ **Menampilkan Waktu Saat Ini**
✅ **Membuka Kamera** dengan OpenCV

## 🔧 Instalasi
Pastikan Python telah terinstal di komputer Anda, lalu install dependensi dengan perintah berikut:
```bash
pip install speechrecognition gtts opencv-python webbrowser
```

## 🚀 Cara Menggunakan
1. **Jalankan Program**
   ```bash
   python voice_assistant.py
   ```
2. **Bagi dua layar setelah menjalankan program** agar saat **audio voice assistant diputar**, aplikasi pemutar audio tidak menggangu tampilan terminal.

3. **Berikan Perintah Suara**, seperti:
   - **"Buka Google"** → Membuka Google
   - **"Cari di YouTube Python Tutorial"** → Mencari video di YouTube
   - **"Jam berapa sekarang?"** → Menampilkan waktu
   - **"Buka kamera"** → Mengaktifkan kamera
   - **"Terima kasih"** → Menghentikan asisten

## 🛠 Teknologi yang Digunakan
- `speech_recognition` → Mendeteksi suara pengguna
- `gtts` → Mengubah teks menjadi suara
- `webbrowser` → Membuka halaman web
- `datetime` → Menampilkan waktu saat ini
- `os` → 'membuka aplikasi system dan membantu memutar audio voice asisstant'

## 📌 Catatan
- Program ini hanya mendukung Bahasa Indonesia.
- Pastikan mikrofon berfungsi dengan baik untuk pengenalan suara yang optimal.

Selamat mencoba! 🚀

