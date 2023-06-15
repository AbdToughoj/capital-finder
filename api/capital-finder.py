from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)
    # print(111,my_dict)
    if 'country' in my_dict:
      contry = my_dict.get('country')
      url= 'https://restcountries.com/v3.1/name/'
      res = requests.get(url+contry)
      data = res.json()
      # print(222,data)
      for country_data in data :
        capital = country_data['capital'][0]
        message = f'the capital of {contry} is {capital}'
    elif 'capital' in my_dict:
      cpital = my_dict.get('capital')
      url= 'https://restcountries.com/v3.1/capital/'
      res = requests.get(url+cpital)
      data2 = res.json()
      print(222,data2)
      for country_data2 in data2 :
        capital = country_data2['name']["common"]
        message = f' {cpital} is the capital of  {capital}'
    self.wfile.write(message.encode())
    return












