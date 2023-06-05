




import requests
from django.http import HttpResponseForbidden
class CountryRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.api_key = 'IP2Location API key'
    def __call__(self, request):
        client_ip = self.get_user_public_ip(request)
        if client_ip and self.is_korean_ip(client_ip):
            return self.get_response(request)
        else:
            return HttpResponseForbidden(client_ip)
    def get_user_public_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    def is_korean_ip(self, ip):
        url = f'https://api.ip2location.io/?key={self.api_key}&ip={ip}'
        response = requests.get(url)
        if (ip == '192.168.0.1'):
            return True
        if response.status_code == 200:
            data = response.json()
            return data['country_code'] == 'KR'
        else:
            return False
          
          
          
          
          
          
          
          
          
          
          
          
