from modules.spinner import ContentSpinner
from modules.kajian_map import KajianLocator
from modules.islamic_api import IslamicDataFetcher

def main():
    print("==========================================")
    print(" 🚀 APLIKASI INFRASTRUKTUR KONTEN DAKWAH ")
    print("==========================================")

    # 1. TES CONTENT SPINNER
    print("\n[1] TEST CONTENT SPINNER")
    spinner = ContentSpinner()
    teks_lama = "Bismillah, hadirlah kajian rutin besok malam di Masjid Raya. Tema: Menjaga Hati. Gratis!"
    print("Teks Asli :", teks_lama)
    print("Hasil Spin:", spinner.spin_text(teks_lama))

    # 2. TES LOKASI KAJIAN TERDEKAT (Contoh titik lokasi di Makassar)
    print("\n[2] TEST LOKASI KAJIAN TERDEKAT")
    user_lat, user_lon = -5.1400, 119.4200 # Koordinat Makassar
    locator = KajianLocator(user_lat, user_lon)
    
    daftar_kajian = [
        {"judul": "Kajian Subuh Tematik", "masjid": "Masjid Raya Makassar", "lat": -5.1476, "lon": 119.4327},
        {"judul": "Fiqih Muamalah", "masjid": "Masjid Al-Markaz Al-Islami", "lat": -5.1333, "lon": 119.4167}
    ]
    
    kajian_terdekat = locator.cari_kajian_terdekat(daftar_kajian)
    for k in kajian_terdekat:
        print(f"• {k['judul']} @ {k['masjid']} -> Jarak: {k['jarak_km']} km")

    # 3. TES AL-QUR'AN API
    print("\n[3] TEST AL-QUR'AN API (Surah Al-Fatihah)")
    surah = IslamicDataFetcher.get_surah(1)
    if surah:
        print(f"Surah: {surah['namaLatin']} ({surah['nama']}) - {surah['jumlahAyat']} Ayat")
        print(f"Ayat 1: {surah['ayat'][0]['teksArab']}")
        print(f"Arti  : {surah['ayat'][0]['teksIndonesia']}")

if __name__ == "__main__":
    main()
