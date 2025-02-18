# prayer_times/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests
from datetime import datetime
import json

def index(request):
    return render(request, 'prayer_times/index.html')

def search_city(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)
    
    try:
        url = f"https://api.myquran.com/v2/sholat/kota/cari/{query}"
        response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Try to parse the JSON response
        try:
            data = response.json()
            return JsonResponse(data)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Response content: {response.content}")
            return JsonResponse({'error': 'Invalid response from server'}, status=500)
            
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return JsonResponse({'error': f'Failed to fetch data: {str(e)}'}, status=500)

def get_prayer_times(request):
    city_id = request.GET.get('city_id')
    if not city_id:
        return JsonResponse({'error': 'City ID is required'}, status=400)
    
    try:
        date = datetime.now().strftime('%Y/%m/%d')
        url = f"https://api.myquran.com/v2/sholat/jadwal/{city_id}/{date}"
        response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        response.raise_for_status()
        
        try:
            data = response.json()
            return JsonResponse(data)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Response content: {response.content}")
            return JsonResponse({'error': 'Invalid response from server'}, status=500)
            
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return JsonResponse({'error': f'Failed to fetch data: {str(e)}'}, status=500)