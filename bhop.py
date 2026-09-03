import pymem, pymem.process, time, ctypes, os
 
jump_ptr = 0x52C0F50
local_player_ptr = 0xDEF97C
flags_ptr = 0x104
 
def check_window():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    pid = ctypes.c_ulong()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    hproc = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid.value)
    buf = ctypes.create_unicode_buffer(512)
    ctypes.windll.kernel32.QueryFullProcessImageNameW(hproc, 0, buf, ctypes.byref(ctypes.c_ulong(512)))
    ctypes.windll.kernel32.CloseHandle(hproc)
    return "csgo.exe" in buf.value.lower()
 
def main():
    pm = pymem.Pymem("csgo.exe")
    c_dll = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    
    print("by fiorith UNKNOWNCHEATS")
 
    while 1:
        time.sleep(0.001)
        
 
        if not (ctypes.windll.user32.GetAsyncKeyState(0x20) & 0x8000): continue
        if not check_window(): continue
            
        p_base = pm.read_int(c_dll + local_player_ptr)
        if not p_base: continue
            
        f = pm.read_int(p_base + flags_ptr)
        
 
        if f == 257 or f == 263:
            pm.write_int(c_dll + jump_ptr, 5)
            time.sleep(0.015)
            pm.write_int(c_dll + jump_ptr, 4)
 
main()
