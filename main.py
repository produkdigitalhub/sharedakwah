from modules.spinner import ContentSpinner

def main():
    print("=== PENGUJIAN MODUL CONTENT SPINNER ===\n")
    
    # Inisialisasi Spinner
    spinner = ContentSpinner()
    
    # Contoh teks postingan kajian (seolah-olah hasil dari scraper)
    caption_contoh = """
    Bismillah, hadirlah kajian rutin besok malam Minggu di Masjid Raya Makassar. 
    Tema: Menjaga Hati di Akhir Zaman bersama Ust. Ahmad. 
    Acara gratis dan terbuka untuk umum. Silakan ajak keluarga dan kerabat!
    """
    
    print("--- TEKS ASLI ---")
    print(caption_contoh.strip())
    
    print("\n--- HASIL SPINNER (REWRITE) ---")
    hasil_spin = spinner.spin_text(caption_contoh)
    print(hasil_spin)

if __name__ == "__main__":
    main()
