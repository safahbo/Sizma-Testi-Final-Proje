# 🎮 Oyun Hileleri ve Bellek Zafiyetleri Analizi

<div align="center">

<img src="docs/assets/istinye-university-logo.webp" alt="Istinye University Logo" width="180"/>

![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square\&logo=github)
![Language](https://img.shields.io/badge/Language-Node.js-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![Course](https://img.shields.io/badge/Course-BGT006-purple?style=flat-square)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)

**İstinye Üniversitesi – Penetration Testing (BGT006) Dersi Projesi**

</div>

---

# 🎓 Danışman

| Bilgi    | Değer                                                                 |
| -------- | --------------------------------------------------------------------- |
| Ad Soyad | Keyvan Arasteh                                                        |
| GitHub   | @keyvanarasteh                                                        |
| E-posta  | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| LinkedIn | linkedin.com/in/keyvanarasteh                                         |
| Website  | qline.tech                                                            |

---

# 👤 Öğrenci Bilgileri

| Bilgi      | Değer               |
| ---------- | ------------------- |
| Ad Soyad   | Safa Hacıbayramoğlu |
| Öğrenci No | 2420191014          |

---

# 📚 Ders Bilgileri

| Bilgi      | Değer                             |
| ---------- | --------------------------------- |
| Ders Adı   | Penetration Testing (Sızma Testi) |
| Ders Kodu  | BGT006                            |
| Kredi      | 3 ECTS                            |
| Dönem      | 2025–2026 Bahar                   |
| Üniversite | İstinye Üniversitesi              |

---

# 📋 Proje Özeti

Bu çalışma, rekabetçi bilgisayar oyunlarında kullanılan hile yazılımlarının (örneğin Wallhack ve Aimbot) işletim sistemi seviyesinde bellek erişimi mekanizmalarını nasıl kötüye kullanabildiğini teorik ve akademik açıdan incelemektedir.

Proje kapsamında;

* Hedef süreçlerin (process) tespit edilmesi,
* Bellek haritalarının analiz edilmesi,
* Pointer zincirlerinin incelenmesi,
* Bellek adreslerinin dinamik yapısının değerlendirilmesi,
* ASLR (Address Space Layout Randomization) mekanizmasının etkilerinin araştırılması,
* Süreç belleğinden veri elde edilmesine yönelik yöntemlerin teorik analizi

sızma testi metodolojisi çerçevesinde ele alınmaktadır.

Bu çalışma tamamen eğitimsel ve savunma amaçlı güvenlik araştırması niteliğindedir.

---

# 🎯 Proje Hedefleri

* Oyun hilelerinin çalışma mantığını anlamak
* İşletim sistemi bellek yönetimini incelemek
* Süreçler arası bellek erişim mekanizmalarını araştırmak
* ASLR ve benzeri koruma mekanizmalarını analiz etmek
* Bellek tabanlı saldırı yüzeylerini değerlendirmek
* Güvenlik perspektifinden riskleri raporlamak

---

# 🗂 Repository Yapısı

```text
.
├── README.md
├── ROADMAP.md
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── docs/
│   ├── modules/
│   ├── research/
│   └── references/
└── src/
```

---

# 🚀 Kurulum

## Repository'yi Klonlama

```bash
git clone https://github.com/safahbo/pentest-memory-analysis.git

cd pentest-memory-analysis
```

## Ortam Değişkenleri

```bash
cp .env.example .env
```

Daha sonra `.env` dosyasını kendi test ortamınıza uygun şekilde düzenleyin.

---

## Docker ile Çalıştırma

```bash
docker-compose up -d
```

---

## Lokal Çalıştırma

```bash
cd src

npm install

node main.js
```

---

# 📊 Teslim Planı

| Görev                                    | Durum |
| ---------------------------------------- | ----- |
| Bellek ve İşletim Sistemi Teorik Analizi | ⬜     |
| Araştırma ve Literatür Taraması          | ⬜     |
| Yerel Test Ortamının Kurulumu            | ⬜     |
| Kanıt ve Ekran Görüntülerinin Toplanması | ⬜     |
| Zafiyet Değerlendirme Raporu             | ⬜     |
| Final Dokümantasyonu                     | ⬜     |

---

# 📖 Dokümantasyon

| Klasör          | Açıklama                         |
| --------------- | -------------------------------- |
| docs/modules    | Modül bazlı teknik dokümantasyon |
| docs/research   | Araştırma notları ve analizler   |
| docs/references | Akademik ve teknik kaynaklar     |

---

# 🔍 Kullanılan Metodoloji

Bu proje aşağıdaki sızma testi aşamalarını referans almaktadır:

1. Keşif (Reconnaissance)
2. Numaralandırma (Enumeration)
3. Analiz (Analysis)
4. İstismar Simülasyonu (Controlled Exploitation)
5. Etki Değerlendirmesi (Impact Assessment)
6. Raporlama (Reporting)

---

# 📚 Kaynaklar

* Microsoft Win32 API Documentation
* Microsoft Memory Management Documentation
* OWASP Penetration Testing Guide
* OWASP Testing Guide v4
* Windows Internals
* Practical Malware Analysis
* Game Hacking Academy Research Notes

---

# ⚠️ Yasal Uyarı

Bu proje yalnızca eğitimsel, akademik ve savunma amaçlı güvenlik araştırmaları için hazırlanmıştır.

Projede yer alan tüm çalışmalar kontrollü laboratuvar ortamlarında gerçekleştirilmeli ve üçüncü taraf sistemlere izinsiz erişim amacıyla kullanılmamalıdır.

Yazar ve danışman, içeriğin kötüye kullanımından sorumlu değildir.

---

<div align="center">

**İstinye Üniversitesi**
**Penetration Testing (BGT006)**
**2025–2026 Bahar Dönemi**

</div>
