import instaloader

class MedsosScraper:
    def __init__(self, username=None, password=None):
        self.L = instaloader.Instaloader(
            download_pictures=False,
            download_videos=False,
            download_video_thumbnails=False,
            save_metadata=False,
            compress_json=False
        )
        
        # Login untuk menghindari Error 429
        if username and password:
            try:
                self.L.login(username, password)
                print("Berhasil login ke Instagram.")
            except Exception as e:
                print(f"Gagal login: {e}")

       def scrape_instagram_profile(self, target_account: str, limit: int = 5):
        """
        Mengambil postingan terbaru dari akun Instagram publik.
        """
        try:
            profile = instaloader.Profile.from_username(self.L.context, target_account)
            posts_data = []

            for count, post in enumerate(profile.get_posts()):
                if count >= limit:
                    break
                
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
            print(f"Error saat scraping: {e}")
            return []
