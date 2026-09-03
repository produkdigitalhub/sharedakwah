from geopy.distance import geodesic

class KajianLocator:
    def __init__(self, user_lat: float, user_lon: float):
        self.user_coords = (user_lat, user_lon)

    def cari_kajian_terdekat(self, list_kajian: list) -> list:
        """
        Menghitung jarak dari koordinat user ke tiap lokasi kajian,
        lalu mengurutkan dari yang terdekat.
        """
        hasil = []
        for kajian in list_kajian:
            kajian_coords = (kajian["lat"], kajian["lon"])
            jarak_km = geodesic(self.user_coords, kajian_coords).km
            
            # Buat salinan data dan tambahkan info jarak
            item_kajian = kajian.copy()
            item_kajian["jarak_km"] = round(jarak_km, 2)
            hasil.append(item_kajian)

        # Urutkan berdasarkan jarak terkecil
        hasil_terurut = sorted(hasil, key=lambda x: x["jarak_km"])
        return hasil_terurut
