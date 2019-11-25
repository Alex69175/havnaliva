import requests
from bs4 import BeautifulSoup
import time
import csv
from random import choice

def get_html(url, proxies):
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19',
        'Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    ]
    user_agent = {'User-Agent': choice(user_agents)}
    proxy = {'http': choice(proxies)}

    response = requests.get(url, headers=user_agent, proxies = proxy)

    return response.text

def main():
    name_ = []
    img_ = []
    price_ = []

    csv_file = open('cms_scrape.csv', 'w', encoding = "utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Image', 'Price'])

    source = requests.get('https://www.us-proxy.org/').text
    soup = BeautifulSoup(source, 'lxml')
    proxy = []
    for a in soup.tbody.find_all('tr'):
        proxy.append(a.find_all('td')[0].string)

    for i in range(1, 2):
        time.sleep(2)https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_smartfon.html?page={i}'
        source = get_html(f', proxy)
        soup = BeautifulSoup(source, 'lxml')

        href = soup.find_all('a', {'class': 'listing-link detail-link'})
        print(href)
        for a in href:
            time.sleep(2)
            html = get_html('https://www.foxtrot.com.ua' + a['href'],proxy)
            item = BeautifulSoup(html, 'lxml')

            name = item.find('div', attrs={'class': "mark"}).h1.get_text(' ', strip=True)
            name = name.replace('Смартфон ', '')
            name_.append(name)
            print(name)

            img = item.find('div', class_='img-wrapper').img['src']
            img_.append(img)
            print(img)

            price = item.find('div', attrs={'class': "price__relevant"}).span.text
            for char in ' \n':
                price = price.replace(char, '')
            price_.append(price)
            print(price + '\n')

    for j in range(1, len(name_)):
        csv_writer.writerow([name_[j], img_[j], price_[j]])
    csv_file.close()

if __name__ == '__main__':
    main()
