# Proje Yol Haritası (Roadmap)

Bu dosya projenin 0'dan 100'e geliştirme ve analiz aşamalarını takip etmek için oluşturulmuştur.

- [x] **Aşama 1: Proje Kurulumu ve İskeletin Oluşturulması**
  - [x] Repo dizin yapısının hazırlanması.
  - [x] `README.md` ve şablonların entegrasyonu.

- [ ] **Aşama 2: Teori ve Araştırma (docs/research/)**
  - [ ] İşletim sistemi bellek yönetimi analizi.
  - [ ] ASLR ve DMA mantığının incelenmesi.

- [ ] **Aşama 3: PoC Geliştirme (src/)**
  - [ ] Node.js ile hedef process'i tespit eden betiğin yazılması.
  - [ ] `memoryjs` veya benzeri OS API hook'ları ile bellek adreslerinden veri okuma.
  - [ ] Offset hesaplama mantığının entegrasyonu.

- [ ] **Aşama 4: Test ve Kanıt Toplama**
  - [ ] PoC'nin lokal test ortamında çalıştırılması.
  - [ ] Terminal üzerinden bellek okuma işleminin ekran görüntüleri ile belgelenmesi.

- [ ] **Aşama 5: Sızma Testi Raporlaması (docs/modules/)**
  - [ ] Zafiyet rapor şablonuna göre bulguların yazılması.
  - [ ] Çözüm ve anti-cheat yaklaşımlarının eklenmesi.
