from modules.scraper import MedsosScraper

def main():
    scraper = MedsosScraper()
    
    # Masukkan akun target kajian di sini
    target_akun = "infokajianmakassar" 
    print(f"Menjalankan scraper untuk @{target_akun}...\n")
    
    hasil = scraper.scrape_instagram_profile(target_account=target_akun, limit=3)
    
    if not hasil:
        print("Tidak ada data ditemukan atau akun dibatasi.")
        return

    for idx, post in enumerate(hasil, 1):
        print(f"=== Post {idx} [{post['date']}] ===")
        print(f"Link: {post['url']}")
        print(f"Caption:\n{post['caption'][:200]}...")
        print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
