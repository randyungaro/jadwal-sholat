import requests
from datetime import datetime
from django.core.cache import cache

class PrayerTimeService:
    BASE_URL = "https://api.myquran.com/v2/sholat/"
    
    @staticmethod
    def search_city(query):
        cache_key = f'city_search_{query}'
        cached_result = cache.get(cache_key)
        
        if cached_result:
            return cached_result
            
        try:
            response = requests.get(
                f"{PrayerTimeService.BASE_URL}kota/cari/{query}",
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            data = response.json()
            
            if data['status'] and data['data']:
                cache.set(cache_key, data['data'], timeout=86400)  # Cache for 24 hours
                return data['data']
            return []
        except Exception as e:
            return []

    @staticmethod
    def get_prayer_times(city_id, date=None):
        if not date:
            date = datetime.now().strftime('%Y/%m/%d')
            
        cache_key = f'prayer_times_{city_id}_{date}'
        cached_result = cache.get(cache_key)
        
        if cached_result:
            return cached_result
            
        try:
            response = requests.get(
                f"{PrayerTimeService.BASE_URL}jadwal/{city_id}/{date}",
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            data = response.json()
            
            if data['status']:
                cache.set(cache_key, data['data'], timeout=3600)  # Cache for 1 hour
                return data['data']
            return None
        except Exception as e:
            return None