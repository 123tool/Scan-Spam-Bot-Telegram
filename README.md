## SCAN & SPAM BOT APK TELEGRAM v2.0
> **Anti Scam Bot Neutralizer & APK Scanner**

Alat "offensive-defense" yang dirancang untuk membantu pengembang dan praktisi keamanan dalam melacak serta menetralisir bot Telegram yang digunakan untuk aktivitas ilegal (Phishing/Scam APK).

---

## 🚀 Fitur
*   **Auto APK Scanner**: Ekstraksi Token Bot & Chat ID langsung dari binary APK tanpa decompile manual.
*   **Async Swarm Engine**: Pengiriman spam ribuan pesan/file secara asinkronus (super cepat).
*   **Cross-Platform**: Support penuh untuk Termux (Android), Ubuntu, dan berbagai distro Linux.

---

## 🛠️ Panduan

## Instalasi di Termux (Android)
Pastikan Termux sudah diizinkan mengakses penyimpanan (`termux-setup-storage`).

1. **Update & Install Dependencies**
```
pkg update && pkg upgrade
pkg install python python-pip git -y
```
2. **Clone Repository**
```
git clone https://github.com/123tool/Scan-Spam-Bot-Telegram.git
cd Scan-Spam-Bot-Telegram
```
3. **Install Library**
```
pip install -r requirements.txt
```
4. **Jalankan Program**
```
python app.py
```
5. **Akses dashboard di :**
```
http://127.0.0.1:5000
```

## Instalasi di Ubuntu / Debian / Linux Mint
1. **Update sistem**
```
sudo apt update && sudo apt upgrade -y
```
2. **Install Python & Pip**
```
sudo apt install python3 python3-pip -y
```
3. **Masuk ke direktori**
```
git clone https://github.com/123tool/Scan-Spam-Bot-Telegram.git
cd Scan-Spam-Bot-Telegram
```
4. **Install Virtual Environment (Opsional tapi disarankan)**
```
python3 -m venv venv
source venv/bin/activate
```
5. **Install Requirements**
```
pip install -r requirements.txt
```
6. **Jalankan Program**
```
python3 app.py
```
7. **Akses dashboard di :**
```
http://localhost:5000
atau
http://IP_SERVER:5000
```

## Cara Penggunaan

1. **​Metode Otomatis (Scan APK) :**
- ​Klik tombol "Upload APK".
- ​Sistem akan otomatis mencari Token Bot dan Chat ID yang tersembunyi di dalam kode APK tersebut.
- ​Data akan otomatis terisi ke form konfigurasi.

2. ​**Metode Manual :**
- ​Masukkan Token Bot dan Chat ID target secara manual jika sudah memilikinya.
- ​Masukkan URL Media (Gambar/File) sebagai muatan spam.

3. **​Eksekusi :**
- ​Atur jumlah pesan dan delay.
- ​Klik "KIRIM" dan pantau log di konsol bawah.

## ​⚠️ Disclaimer

**​Alat ini dibuat untuk tujuan edukasi, riset keamanan, dan membantu korban penipuan digital. Penggunaan alat ini untuk tindakan yang melanggar hukum di luar konteks pertahanan/riset sepenuhnya menjadi tanggung jawab pengguna. Gunakan dengan bijak!**
