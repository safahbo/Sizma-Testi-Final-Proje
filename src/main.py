import ctypes

OpenProcess = ctypes.windll.kernel32.OpenProcess
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
CloseHandle = ctypes.windll.kernel32.CloseHandle

# 64-bit bellek adreslerini okuyabilmek icin arguman tiplerini belirliyoruz
ReadProcessMemory.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]

PROCESS_ALL_ACCESS = 0x1F0FFF

def read_memory(pid, address):
    process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    buffer = ctypes.c_int()
    bytes_read = ctypes.c_size_t()
    # Adresi c_void_p ile 64-bit formata ceviriyoruz
    ReadProcessMemory(process_handle, ctypes.c_void_p(address), ctypes.byref(buffer), 4, ctypes.byref(bytes_read))
    CloseHandle(process_handle)
    return buffer.value

try:
    env_vars = {}
    with open('.env', 'r') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, val = line.strip().split('=', 1)
                env_vars[key] = val

    pid = int(env_vars["TARGET_PID"])
    health_addr = int(env_vars["ADDR_HEALTH"], 16)
    ammo_addr = int(env_vars["ADDR_AMMO"], 16)

    print("[*] Bellek Okuma (Memory Read) PoC Baslatildi...")
    print(f"[+] Hedef PID: {pid}")
    print(f"[*] Guncel Can (Health): {read_memory(pid, health_addr)}")
    print(f"[*] Guncel Mermi (Ammo): {read_memory(pid, ammo_addr)}")
except Exception as e:
    print(f"[-] Detayli Hata: {e}")