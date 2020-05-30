from os import getenv
import requests
import argparse
from dotenv import load_dotenv

TOKEN = getenv('BITLY_TOKEN')

def shorten_link(token, long_url):
  headers = {'Authorization': f'Bearer {token}'}
  params = {'long_url': long_url}
  url = 'https://api-ssl.bitly.com/v4/bitlinks'
  response = requests.post(url, headers=headers, json=params)
  response.raise_for_status()
  bitlink = response.json()['id']
  return bitlink

def count_clicks(token, bitlink):
  headers = {'Authorization': f'Bearer {token}'}
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
  params = {'units': '-1'}
  response = requests.get(url, headers=headers, params=params)
  response.raise_for_status()
  total_clicks = response.json()['total_clicks']
  return total_clicks

def main():
  load_dotenv()
  parser = argparse.ArgumentParser(description='Укорачивает ссылку или считает клики')
  parser.add_argument('link', help='Длинная или короткая ссылка')
  args = parser.parse_args()
  user_input = args.link

  if user_input.startswith('bit.ly'):
    try:
      clicks_count = count_clicks(TOKEN, user_input)
    except requests.exceptions.HTTPError:
      print('Неправильная ссылка.')
    print('Количество переходов:', clicks_count)
  else:
    try:
      bitlink = shorten_link(TOKEN, user_input)
    except requests.exceptions.HTTPError:
      print('Неправильная ссылка.')
    print('Битлинк', bitlink)

if __name__ == '__main__':
  main()