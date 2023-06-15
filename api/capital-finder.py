from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_list)
        
        if 'country' in query_dict:
            country_query = query_dict.get('country')
            message = self.get_country_info(country_query)
        
        elif 'capital' in query_dict:
            capital_query = query_dict.get('capital')
            message = self.get_capital_info(capital_query)
        
        else:
            message = "Invalid query parameter"
        
        self.wfile.write(message.encode())
        return

    def get_country_info(self, country_query):
        country_url = f'https://restcountries.com/v3.1/name/{country_query}'
        response = requests.get(country_url)
        
        if response.status_code == 200:
            country_data = response.json()
            
            if country_data:
                for country_info in country_data:
                    capital = country_info['capital'][0]
                    message = f"The capital of {country_query} is {capital}"
                return message
            else:
                return "Data not found"
        
        return "API request failed"

    def get_capital_info(self, capital_query):
        capital_url = f'https://restcountries.com/v3.1/capital/{capital_query}'
        response = requests.get(capital_url)
        
        if response.status_code == 200:
            capital_data = response.json()
            
            if capital_data:
                for capital_info in capital_data:
                    country_name = capital_info['name']['common']
                    message = f"{capital_query} is the capital of {country_name}"
                return message
            else:
                return "Data not found"
        
        return "API request failed"
