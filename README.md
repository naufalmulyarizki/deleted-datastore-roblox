![preview1](https://r2.fivemanage.com/WX5Hv6yMgODTgG2WF6rml/images/backgroundgithub.png)

# 🗑️ Roblox DataStore Deleter

Script Python untuk **menghapus DataStore** dari game Roblox menggunakan Roblox Open Cloud API v2. Dilengkapi mode **DRY RUN** (simulasi) sebelum eksekusi sungguhan agar aman digunakan.

> ⚠️ **PERINGATAN KERAS:** Penghapusan DataStore bersifat **permanen dan tidak dapat dibatalkan**. Seluruh data di dalam DataStore tersebut akan hilang selamanya. Gunakan dengan sangat hati-hati.

---

## 📋 Daftar Isi

1. [Fitur & Cara Kerja](#-fitur--cara-kerja)
2. [Peringatan Penting](#-peringatan-penting)
3. [Instalasi Python](#-instalasi-python)
4. [Cara Membuat API Key](#-cara-membuat-api-key)
5. [Cara Mendapatkan Universe ID](#-cara-mendapatkan-universe-id)
6. [Cara Mendapatkan Nama DataStore](#-cara-mendapatkan-nama-datastore)
7. [Konfigurasi Script](#-konfigurasi-script)
8. [Cara Menjalankan](#-cara-menjalankan)
9. [Alur Penggunaan yang Direkomendasikan](#-alur-penggunaan-yang-direkomendasikan)
10. [Contoh Output](#-contoh-output)
11. [Troubleshooting](#-troubleshooting)

---

## ✨ Fitur & Cara Kerja

### Fitur
- **DRY RUN Mode** — Simulasi penghapusan tanpa benar-benar menghapus data
- **Konfirmasi Manual** — Wajib mengetik ulang nama DataStore sebelum dihapus
- **Feedback Jelas** — Menampilkan status HTTP dan pesan error jika gagal
- **URL Encoding Otomatis** — Nama DataStore dengan karakter khusus di-encode secara otomatis

### Cara Kerja

```
Script Dijalankan
      │
      ▼
Cek DRY_RUN = True?
  ├─ YA  → Tampilkan simulasi, TIDAK ada yang dihapus
  └─ TIDAK → Minta konfirmasi nama DataStore
                  │
                  ▼
         Nama cocok?
           ├─ TIDAK → Batalkan
           └─ YA   → Kirim request DELETE ke Roblox API
                              │
                              ▼
                   Tampilkan hasil (sukses/gagal)
```

Script ini memanggil endpoint berikut:
```
DELETE https://apis.roblox.com/cloud/v2/universes/{universeId}/data-stores/{dataStoreName}
```

---

## ⚠️ Peringatan Penting

| Peringatan | Penjelasan |
|---|---|
| **Data hilang permanen** | Tidak ada fitur undo/restore di Roblox API untuk DataStore yang sudah dihapus |
| **Jangan share API Key** | API Key memberi akses penuh ke game kamu. Jangan pernah upload ke GitHub publik |
| **Pastikan nama DataStore benar** | Satu kesalahan ketik = DataStore yang salah terhapus |
| **Backup dulu** | Export atau backup data penting sebelum menjalankan script ini |

---

## 🐍 Instalasi Python

### Langkah 1 — Download Python

1. Buka browser dan kunjungi **https://www.python.org/downloads/**
2. Klik tombol **"Download Python 3.x.x"** (versi terbaru)
3. File installer akan terunduh (contoh: `python-3.12.3-amd64.exe`)

### Langkah 2 — Install Python

1. Jalankan file installer yang sudah diunduh
2. ✅ **PENTING:** Centang kotak **"Add Python to PATH"** di bagian bawah sebelum klik Install
3. Klik **"Install Now"**
4. Tunggu proses instalasi selesai, lalu klik **Close**

### Langkah 3 — Verifikasi Instalasi

Buka **Command Prompt** (tekan `Win + R`, ketik `cmd`, tekan Enter) lalu jalankan:

```bash
python --version
```

Output yang diharapkan:
```
Python 3.12.3
```

Jika muncul error `'python' is not recognized`, coba:
```bash
python3 --version
```

### Langkah 4 — Install Library `requests`

Library `requests` dibutuhkan script ini untuk melakukan HTTP request ke Roblox API.

```bash
pip install requests
```

Verifikasi berhasil diinstall:
```bash
pip show requests
```

---

## 🔑 Cara Membuat API Key

API Key adalah kunci otorisasi untuk mengakses Roblox Open Cloud API. Berikut cara membuatnya:

### Langkah 1 — Buka Creator Dashboard

1. Buka browser dan pergi ke **https://create.roblox.com/**
2. Login dengan akun Roblox kamu
3. Di sidebar kiri, klik **"Credentials"**

### Langkah 2 — Buat API Key Baru

1. Klik tombol **"Create API Key"** (pojok kanan atas)
2. Isi form berikut:
   - **Name:** Beri nama deskriptif, contoh: `DataStore Deleter Script`
   - **Description:** (opsional) Keterangan kegunaan key ini

### Langkah 3 — Atur Permission

Ini bagian **terpenting**. API Key harus punya izin yang benar:

1. Di bagian **"Access Permissions"**, klik **"Add API System"**
2. Pilih **"DataStore"** dari daftar
3. Setelah DataStore ditambahkan, klik dropdown di sebelahnya
4. Pilih experience/game yang ingin kamu kelola
5. Centang permission **"Write"** (diperlukan untuk menghapus)

> 💡 **Tips Keamanan:** Pilih hanya experience yang spesifik, jangan pilih "All Experiences" kecuali benar-benar diperlukan.

### Langkah 4 — Atur IP Whitelist (Opsional tapi Disarankan)

1. Di bagian **"Accepted IP Addresses"**
2. Masukkan IP address kamu (cari di **https://whatismyipaddress.com/**)
3. Klik **"Add IP"**

### Langkah 5 — Simpan API Key

1. Klik **"Save & Generate Key"**
2. **SALIN dan SIMPAN** API Key yang muncul di tempat aman (password manager, notepad terenkripsi, dll.)
3. API Key **hanya ditampilkan SEKALI**. Jika hilang, harus buat yang baru.

---

## 🌐 Cara Mendapatkan Universe ID

Universe ID adalah ID unik untuk game/experience Roblox kamu. Ada dua cara untuk mendapatkannya:

### Cara 1 — Dari Creator Dashboard (Paling Mudah)

1. Buka **https://create.roblox.com/dashboard/creations**
2. Klik game kamu
3. Di URL browser, kamu akan melihat format seperti:
   ```
   https://create.roblox.com/dashboard/creations/experiences/9417372845/overview
   ```
4. Angka setelah `/experiences/` adalah **Universe ID** kamu
   - Contoh di atas: `9417372845`

### Cara 2 — Konversi dari Place ID

Jika kamu hanya tahu **Place ID** game (bukan Universe ID):

1. Buka game kamu di Roblox, lihat URL di browser:
   ```
   https://www.roblox.com/games/123456789/NamaGame
   ```
   Angka `123456789` adalah **Place ID**

2. Gunakan Roblox API untuk konversi. Buka URL ini di browser (ganti dengan Place ID kamu):
   ```
   https://apis.roblox.com/universes/v1/places/123456789/universe
   ```

3. Response akan berupa JSON seperti ini:
   ```json
   {
     "universeId": 9417372845
   }
   ```

4. Nilai `universeId` itulah yang kamu butuhkan

---

## 📦 Cara Mendapatkan Nama DataStore

Kamu perlu tahu nama persis DataStore yang ingin dihapus. Ada dua cara:

### Cara 1 — Dari Script Roblox Studio

Cek script game kamu di Roblox Studio. Cari baris yang menggunakan `DataStoreService`:

```lua
-- Contoh script Roblox (Lua)
local DataStoreService = game:GetService("DataStoreService")
local myDataStore = DataStoreService:GetDataStore("DonationData_v2")
--                                                 ^^^^^^^^^^^^^^
--                                        Ini nama DataStore kamu
```

Nama yang ada di dalam tanda kutip di `GetDataStore(...)` adalah nama DataStore kamu.

### Cara 2 — List DataStore via Roblox API

Kamu bisa mendapatkan daftar semua DataStore yang ada menggunakan API. Jalankan perintah berikut di terminal (ganti nilai yang sesuai):

**Windows (Command Prompt):**
```bash
curl -H "x-api-key: API_KEY_KAMU" "https://apis.roblox.com/cloud/v2/universes/UNIVERSE_ID_KAMU/data-stores?maxPageSize=50"
```

**Contoh output JSON:**
```json
{
  "dataStores": [
    {
      "path": "universes/9417372845/data-stores/DonationData_v2",
      "id": "DonationData_v2"
    },
    {
      "path": "universes/9417372845/data-stores/PlayerData",
      "id": "PlayerData"
    }
  ]
}
```

Nilai `"id"` di setiap item adalah nama DataStore yang bisa kamu gunakan.

---

## ⚙️ Konfigurasi Script

Buka file `deleted_datastore.py` dengan text editor (Notepad, VS Code, dll.) dan ubah bagian konfigurasi di bagian atas:

```python
# ─── KONFIGURASI ──────────────────────────────────────────
API_KEY        = "ISI_DENGAN_API_KEY_KAMU"
UNIVERSE_ID    = "ISI_DENGAN_UNIVERSE_ID_KAMU"
DATASTORE_NAME = "NamaDataStoreMu"
DRY_RUN        = True
# ──────────────────────────────────────────────────────────
```

### Penjelasan Setiap Parameter

| Parameter | Tipe | Contoh Nilai | Keterangan |
|---|---|---|---|
| `API_KEY` | `string` | `"abc123xyz..."` | API Key dari Roblox Creator Dashboard. Wajib diisi. |
| `UNIVERSE_ID` | `string` | `"9417372845"` | Universe ID game Roblox kamu. Wajib diisi. |
| `DATASTORE_NAME` | `string` | `"DonationData_v2"` | Nama persis DataStore yang ingin dihapus. Case-sensitive (huruf besar/kecil berpengaruh). |
| `DRY_RUN` | `boolean` | `True` atau `False` | `True` = mode simulasi (aman, tidak ada yang dihapus). `False` = eksekusi sungguhan (permanen). |

> 🔒 **Keamanan:** Jangan pernah commit file ini ke repository **publik** selagi masih berisi API Key asli. Gunakan `.gitignore` atau simpan API Key di environment variable.

---

## ▶️ Cara Menjalankan

### Langkah 1 — Buka Terminal / Command Prompt

- **Windows:** Tekan `Win + R`, ketik `cmd`, tekan Enter
- **Atau:** Klik kanan di folder script → "Open in Terminal"

### Langkah 2 — Navigasi ke Folder Script

Gunakan perintah `cd` untuk masuk ke folder tempat file `deleted_datastore.py` berada:

```bash
cd "C:\Users\NamaKamu\Downloads\deleted_datastore"
```

Verifikasi kamu berada di folder yang benar:
```bash
dir
```

Kamu harusnya melihat `deleted_datastore.py` di daftar file.

### Langkah 3 — Jalankan Script

```bash
python deleted_datastore.py
```

---

## 🔄 Alur Penggunaan yang Direkomendasikan

Ikuti urutan ini untuk meminimalkan risiko kesalahan:

```
LANGKAH 1: Set DRY_RUN = True
     │
     ▼
LANGKAH 2: Jalankan script → python deleted_datastore.py
     │
     ▼
LANGKAH 3: Verifikasi output — pastikan Universe ID,
           DataStore Name, dan Mode sudah benar
     │
     ▼
LANGKAH 4: Jika sudah yakin, ubah DRY_RUN = False
     │
     ▼
LANGKAH 5: Jalankan script lagi
     │
     ▼
LANGKAH 6: Ketik ulang nama DataStore saat diminta konfirmasi
     │
     ▼
LANGKAH 7: Penghapusan dieksekusi — cek hasil di terminal
```

---

## 💻 Contoh Output

### Mode DRY RUN (`DRY_RUN = True`)

```
============================================================
  Roblox DataStore Deleter [FIXED]
============================================================
  Universe ID    : 9417372845
  DataStore Name : DonationData_v2
  Mode           : DRY RUN (simulasi)
============================================================

  [DRY RUN] Akan menghapus DataStore: 'DonationData_v2'
  Ubah DRY_RUN = False untuk eksekusi sungguhan.
```

Script berhenti di sini — **tidak ada yang dihapus.**

---

### Mode Eksekusi Sungguhan (`DRY_RUN = False`)

```
============================================================
  Roblox DataStore Deleter [FIXED]
============================================================
  Universe ID    : 9417372845
  DataStore Name : DonationData_v2
  Mode           : ⚠  EKSEKUSI SUNGGUHAN
============================================================

  Ketik nama DataStore 'DonationData_v2' untuk konfirmasi:
```

Setelah mengetik nama DataStore dengan benar:

```
  Ketik nama DataStore 'DonationData_v2' untuk konfirmasi: DonationData_v2

[INFO] Menghapus DataStore...

============================================================
  ✓ DataStore 'DonationData_v2' berhasil dihapus!
============================================================
```

---

### Jika Konfirmasi Salah

```
  Ketik nama DataStore 'DonationData_v2' untuk konfirmasi: donationdata

[INFO] Nama tidak cocok. Dibatalkan.
```

---

## 🔧 Troubleshooting

### ❌ `ModuleNotFoundError: No module named 'requests'`

**Penyebab:** Library `requests` belum diinstall.

**Solusi:**
```bash
pip install requests
```

---

### ❌ `'python' is not recognized as an internal or external command`

**Penyebab:** Python belum ditambahkan ke PATH sistem.

**Solusi:**
1. Uninstall Python dari Control Panel
2. Install ulang Python, dan pastikan mencentang **"Add Python to PATH"**
3. Restart Command Prompt setelah install

---

### ❌ Status `403 Forbidden`

**Penyebab:** API Key tidak punya permission yang cukup, atau Universe ID salah.

**Solusi:**
1. Buka Creator Dashboard → Credentials
2. Edit API Key kamu
3. Pastikan sudah menambahkan permission **DataStore → Write** untuk experience yang benar
4. Pastikan `UNIVERSE_ID` di script sudah benar

---

### ❌ Status `404 Not Found`

**Penyebab:** DataStore dengan nama tersebut tidak ditemukan, atau Universe ID salah.

**Solusi:**
1. Periksa kembali `DATASTORE_NAME` — nama harus **persis sama**, termasuk huruf besar/kecil
2. Periksa kembali `UNIVERSE_ID`
3. Gunakan cara list DataStore via API untuk memastikan nama yang benar

---

### ❌ Status `401 Unauthorized`

**Penyebab:** API Key tidak valid atau sudah kedaluwarsa.

**Solusi:**
1. Buka Creator Dashboard → Credentials
2. Pastikan API Key yang kamu copy sudah benar (tidak ada spasi ekstra)
3. Jika API Key sudah dihapus, buat yang baru

---

### ❌ `ConnectionError` atau `TimeoutError`

**Penyebab:** Tidak ada koneksi internet atau Roblox API sedang down.

**Solusi:**
1. Periksa koneksi internet kamu
2. Coba akses `https://apis.roblox.com` dari browser
3. Cek status Roblox di **https://status.roblox.com/**

---

## 📄 Lisensi

Script ini dibuat untuk keperluan pribadi/administrasi game Roblox. Gunakan dengan tanggung jawab penuh.
