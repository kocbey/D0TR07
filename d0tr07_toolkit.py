
#!/usr/bin/env python3
import os
import subprocess
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_menu():
    clear_screen()
    print("\033[1;33m--- d0tr07 Pentest Toolkit Ana Menü ---\033[0m")
    print("1) Bilgi Toplama Araçları")
    print("2) Ağ Sızma Araçları")
    print("3) Web Uygulama Test Araçları")
    print("4) Kabuk Erişimi ve Post-Exploit")
    print("5) Zafiyet Analiz Araçları")
    print("6) Şifre Kırma Araçları")
    print("7) Kablosuz Ağ Test Araçları")
    print("8) Dosya ve Sistem Analiz Araçları")
    print("9) Sosyal Mühendislik Araçları")
    print("10) Log ve İzleme Araçları")
    print("11) Steganografi ve Adli Bilişim Araçları")
    print("12) Kötü Amaçlı Yazılım Analizi")
    print("13) Exploit Geliştirme Araçları")
    print("14) Kriptografi Araçları")
    print("15) Network Trafik Analiz Araçları")
    print("16) Otomasyon ve Script Araçları")
    print("17) AI Destekli Analiz")
    print("18) Gelişmiş Proxy ve VPN Araçları")
    print("19) Raporlama ve Belgeleme")
    print("20) Çıkış")
    print("\nSeçiminizi giriniz:")

def main():
    while True:
        print_menu()
        choice = input("> ").strip()
        if choice == "20":
            print("Çıkış yapılıyor. Görüşürüz, d0tr07!")
            sys.exit(0)
        else:
            print(f"Seçim: {choice} için alt menüler ve fonksiyonlar yakında gelecek...")

if __name__ == "__main__":
    main()
