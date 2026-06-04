# Araştırma Notları / Research Notes

> Konu / Module: İşletim Sistemi Bellek Yönetimi ve OS API Hooking
> Tarih / Date: 2026-06-04

---

## What I'm Investigating / Araştırdığım Konu

Oyun hilelerinin (memory hacking) çalışma mantığı. Bir uygulamanın, işletim sisteminin bellek izolasyon mekanizmalarını (ASLR) nasıl aştığı ve başka bir uygulamanın (process) RAM'de tuttuğu verilere (örneğin can, mermi, koordinat) nasıl ulaştığı.

## Resources Found / Bulunan Kaynaklar

- [Microsoft Win32 API - Memory Management](https://learn.microsoft.com/en-us/windows/win32/memory/memory-management) — `OpenProcess` ve `ReadProcessMemory` fonksiyonlarının çalışma mantığı.
- [OWASP Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — İstemci taraflı kontrollerin zafiyetleri.

## Key Findings / Temel Bulgular

1. Windows işletim sisteminde, uygun yetkilere (Process Access Rights) sahip bir script, hedef sürecin RAM alanını kısıtlamasız okuyabilir.
2. ASLR (Address Space Layout Randomization) her başlatmada adresleri değiştirse de, `Base Address + Static Offset` mantığı kullanılarak doğru veri her zaman bulunabilir.

## Dead Ends / Çıkmaz Sokaklar

Things I tried that didn't work and why:
- Node.js ile direkt pointer adresine erişmeye çalışmak → Başarısız oldu çünkü sanal bellek (virtual memory) adresleri doğrudan OS API çağrısı olmadan okunamıyor. `memoryjs` kütüphanesi bu yüzden kullanıldı.

## Questions Remaining / Kalan Sorular

- [ ] Kernel seviyesinde (Ring 0) çalışan Anti-Cheat sistemleri bu bellek okuma işlemlerini nasıl tespit ediyor?
- [ ] DMA (Direct Memory Access) donanımları ile yapılan donanımsal hileler aynı mantıkla mı çalışır?

## 5-Step Breakdown / Çözümleme Adımları

1. Step 1: İşletim sisteminden aktif süreç (PID) nasıl alınır?
2. Step 2: PID kullanılarak sürecin Base Address'i nasıl bulunur?
3. Step 3: Cheat Engine vb. araçlarla statik offset'ler nasıl tespit edilir?
4. Step 4: Base Address ile Offset toplanarak dinamik adres nasıl hesaplanır?
5. Step 5: `ReadProcessMemory` ile hesaplanan adresteki byte'lar nasıl okunur?
