import ctypes
import os
import time

# RAM'de tutulacak statik degiskenler
health = ctypes.c_int(100)
ammo = ctypes.c_int(30)

print("--- HEDEF OYUN (DUMMY PROCESS) CALISIYOR ---")
print(f"TARGET_PID={os.getpid()}")
print(f"ADDR_HEALTH={hex(ctypes.addressof(health))}")
print(f"ADDR_AMMO={hex(ctypes.addressof(ammo))}")
print("\n[!] Lutfen bu degerleri .env dosyasina kopyalayin.")
print("[!] Okuma yapmak icin diger terminalde 'python src/main.py' calistirin.")

# Kapanmamasi icin sonsuz dongu
while True:
    time.sleep(5)
