obfuscated_flag = [
    0x8a, 0x101, 0x11e, 0x178, 0x163, 0x108, 0x136, 0x101, 0x104, 0x12d, 
    0x178, 0x17f, 0x165, 0x11d, 0x171, 0x136, 0x101, 0x171, 0x17f, 0x135, 
    0x135, 0x163, 0x11b, 0x178, 0x11e, 0x127, 0x3f, 0x12b
]

print("[*] Task 4 üçün ətraflı simvol analizi başladıldı...\n")

for idx, target in enumerate(obfuscated_flag):
    valid_chars = []
    
    # Bütün oxunabilən ASCII simvollarını tək-tək yoxlayırıq
    for candidate in range(32, 127):
        # Assembly-dəki (target ^ 0x55) - 7 məntiqinin candidate ilə əlaqəsi
        # Əgər candidate bu hədəfə tam bölünürsə (qalıqsız və ya yaxın)
        val = ((target ^ 0x55) - 7) // 3
        if candidate == val:
            valid_chars.append(chr(candidate))
            
    # Nəticəni hər indeks üçün ekrana çıxarırıq
    chars_str = "  və ya  ".join([f"'{c}'" for c in valid_chars])
    print(f"Index {idx:02d}: {chars_str if valid_chars else 'Yoxdur!'}")
