# Tugas Modul 1: CI/Cd

---

## Identitas Mahasiswa

| Nama | Prodi | NRP |
| :--- | :--- | :--- |
| Muhammad Akhdan Alwaafy | Teknik Informatika | 5025241223 |

---

## Deskripsi Tugas

implementasikan modul CI/CD ini pada sebuah sistem server sederhana, dengan detail sebagai berikut
1. Buatlah API publik dengan endpoint /health yang menampilkan informasi sebagai berikut:

   CONTOH (value disesuaikan)
```
{
  "nama": "Sersan Mirai Afrizal",
  "nrp": "5025241999",
  "status": "UP",
  “timestamp”: time	// Current time
  "uptime": time		// Server uptime
}
```
Bahasa pemrograman dan teknologi yang digunakan dibebaskan kepada peserta.

2. Lakukan deployment API tersebut di dalam container pada VPS publik. Gunakan port selain 80 dan 443 untuk menjalankan API.
3. Gunakan Ansible untuk menginstall dan meletakkan konfigurasi nginx pada VPS. Nginx akan berperan sebagai reverse proxy yang meneruskan request ke API. Sehingga, API harus bisa diakses hanya dengan menjalankan Ansible Playbook tanpa intervensi/konfigurasi nginx secara manual.
4. Lakukan proses CI/CD menggunakan GitHub Actions untuk melakukan otomasi proses deployment API. Terapkan juga best practices untuk menjaga kualitas environment CI/CD.
5. Dokumentasikan pengerjaan di sebuah laporan berbentuk Markdown pada repositori peserta masing-masing.


## Cara Menjalankan Program

### Prasyarat (Prerequisites)

Pastikan sistem Anda sudah menginstal beberapa kebutuhan berikut sebelum menjalankan program:
* [Contoh: Python 3.10+ / Java 17 / GCC]
* [Contoh: Library tambahan atau environment khusus]

### Langkah-langkah Instalasi & Eksekusi

1. Clone repositori ini ke mesin lokal Anda:
   ```bash
   git clone [https://github.com/username/nama-repositori.git](https://github.com/username/nama-repositori.git)

## Sources

[https://docs.google.com/document/d/11yzgwByWrnmcZ4dQC1MYS_dq12UrjpYHqdl0XIi9gVY/edit?tab=t.0](https://docs.google.com/document/d/11yzgwByWrnmcZ4dQC1MYS_dq12UrjpYHqdl0XIi9gVY/edit?tab=t.0)

[https://github.com/arsitektur-jaringan-komputer/oprec2026-module-deployment/blob/main/README.md](https://github.com/arsitektur-jaringan-komputer/oprec2026-module-deployment/blob/main/README.md)

[https://drive.google.com/drive/folders/1e5DI6a4RpKRRC-03cDWSIkMNQczNDcAT?usp=sharing](https://drive.google.com/drive/folders/1e5DI6a4RpKRRC-03cDWSIkMNQczNDcAT?usp=sharing)

[https://youtu.be/4BibQ69MD8c?si=K0D5XEhe1VohIdsz](https://youtu.be/4BibQ69MD8c?si=K0D5XEhe1VohIdsz)

[https://gemini.google.com/share/4f72f612b0fb](https://gemini.google.com/share/4f72f612b0fb)
