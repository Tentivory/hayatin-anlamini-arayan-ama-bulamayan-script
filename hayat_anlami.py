#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayatın Anlamını Arayan Ama Asla Bulamayan Script
Tamamen gereksiz, ama çalışıyor.
"""

import random
import time
import base64

# Gizli mesaj (base64 ile saklanmış)
GIZLI = "w5Z6Z8O8cmzDvGsgaGVyIHphbWFuIGthemFuxLFyLCBzYW5kxLFrIGtvbnXFn3VyLg=="

def decode_gizli():
    try:
        return base64.b64decode(GIZLI).decode('utf-8')
    except:
        return "Gizli mesaj çözülemedi, belki de anlamsızdır."

def rastgele_anlam():
    anlamlar = [
        "Kahve içmek ve sonra pişman olmak.",
        "Çorapların neden kaybolduğunu anlamak.",
        "Kedilerin dünya hakimiyeti için plan yapmak.",
        "Neden herkes aynı anda konuşuyor diye düşünmek.",
        "Bir sonraki yemeği planlamak.",
        "Hiçbir şey. Kesinlikle hiçbir şey.",
        "Sadece var olmak. O da yeterince ağır.",
        "Bu scripti çalıştırmak."
    ]
    return random.choice(anlamlar)

def main():
    print("=" * 50)
    print("  HAYATIN ANLAMINI ARAMA PROGRAMI v1.0")
    print("  (Bulamazsın ama denemeye devam et)")
    print("=" * 50)
    
    ad = input("\nAdın ne? (Yalan söyleyebilirsin): ")
    print(f"\nMerhaba {ad}. Anlam aramaya başlıyoruz...")
    
    for i in range(5):
        print(f"\n[{i+1}/5] Arıyorum...")
        time.sleep(1.5)
        print(f"Bulduğum şey: {rastgele_anlam()}")
    
    print("\n" + "=" * 50)
    print("Sonuç: Anlam bulunamadı. Tekrar dene.")
    print("Gizli ipucu (eğer çözebilirsen):", decode_gizli())
    print("=" * 50)
    print("\nProgram sona erdi. Hayat devam ediyor...")

if __name__ == "__main__":
    main()
