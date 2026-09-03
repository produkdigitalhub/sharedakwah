import requests

class IslamicDataFetcher:
    @staticmethod
    def get_surah(nomor_surah: int = 1):
        """
        Mengambil detail surah dan ayat Al-Qur'an dari EQuran.id API
        """
        url = f"https://equran.id/api/v2/surat/{nomor_surah}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json().get("data", {})
            return None
        except Exception as e:
            print(f"Error fetching Quran API: {e}")
            return None

    @staticmethod
    def get_hadits_list():
        """
        Contoh pengambil referensi hadits shahih pilihan
        """
        # Daftar referensi hadits populer
        return [
            {
                "kitab": "Shahih Bukhari",
                "nomor": 1,
                "matan": "Innamal a'malu bin niyyat...",
                "terjemah": "Sesungguhnya setiap perbuatan tergantung pada niatnya..."
            },
            {
                "kitab": "Shahih Muslim",
                "nomor": 2581,
                "matan": "Al-Muslimu man salimal muslimuna min lisanihi wa yadihi...",
                "terjemah": "Seorang muslim yang baik adalah yang muslim lainnya selamat dari gangguan lisan dan tangannya."
            }
        ]
