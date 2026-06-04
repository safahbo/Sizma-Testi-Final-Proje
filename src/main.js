const memoryjs = require('memoryjs');
require('dotenv').config();

const processName = process.env.TARGET_PROCESS;

try {
    const processObject = memoryjs.openProcess(processName);
    
    const healthOffset = parseInt(process.env.OFFSET_HEALTH, 16);
    const ammoOffset = parseInt(process.env.OFFSET_AMMO, 16);

    const baseAddress = processObject.modBaseAddr;

    const healthAddress = baseAddress + healthOffset;
    const ammoAddress = baseAddress + ammoOffset;

    const healthValue = memoryjs.readMemory(processObject.handle, healthAddress, memoryjs.INT);
    const ammoValue = memoryjs.readMemory(processObject.handle, ammoAddress, memoryjs.INT);

    console.log(`[+] Process: ${processName} (PID: ${processObject.th32ProcessID})`);
    console.log(`[+] Base Address: 0x${baseAddress.toString(16)}`);
    console.log(`[*] Health: ${healthValue}`);
    console.log(`[*] Ammo: ${ammoValue}`);

    memoryjs.closeProcess(processObject.handle);
} catch (error) {
    console.error(`[-] Hata: ${processName} process tablosunda bulunamadı veya erisim yetkisi yok.`);
}
