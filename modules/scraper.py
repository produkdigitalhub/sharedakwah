import instaloader
from datetime import datetime

class MedsosScraper:
    def __init__(self):
        # Inisialisasi Instaloader tanpa login (untuk akun publik)
        self.L = instaloader.Instaloader(
            download_pictures=False,
            download_videos=False,
            download_video_thumbnails=False,
            save_metadata=False,
            compress_json=False
        )

    def scrape_instagram_profile(self, target_account: str, limit: int = 5):
        """
        Mengambil postingan terbaru dari akun Instagram publik.
        """
        print(f"Sedang mengambil {limit} postingan terbaru dari @{target_account}...")
        
        try:
            profile = instaloader.Profile.from_username(self.L.context, target_account)
            posts_data = []

            for count, post in enumerate(profile.get_posts()):
                if count >= limit:
                    break
                
                # Ekstraksi informasi penting dari postingan
                post_info = {
                    "source": f"Instagram (@{target_account})",
                    "caption": post.caption if post.caption else "",
                    "date": post.date_utc.strftime("%Y-%m-%d %H:%M:%S"),
                    "url": f"https://www.instagram.com/p/{post.shortcode}/",
                    "likes": post.likes,
                }
                posts_data.append(post_info)

            return posts_data

        except Exception as e:
            print(f"Gagal mengambil data dari Instagram: {e}")
            return []

# ---------------------------------------------------------
# UJI COBA MODUL
# ---------------------------------------------------------
if __name__ == "__main__":
    scraper = MedsosScraper()
    
    # Contoh nama akun info kajian (ganti sesuai target)
    target_akun = "infokajianmakassar" 
    
    hasil_scrape = scraper.scrape_instagram_profile(target_account=target_akun, limit=3)
    
    print("\n--- HASIL SCRAPING ---")
    for idx, post in enumerate(hasil_scrape, 1):
        print(f"\n[Post {idx}] {post['date']}")
        print(f"Link: {post['url']}")
        print(f"Caption:\n{post['caption'][:150]}...") # Tampilkan 150 karakter pertama
