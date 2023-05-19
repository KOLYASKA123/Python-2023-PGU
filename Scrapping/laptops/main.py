from collectAllLaptopUrls import collectAllLaptopUrls
from detailLaptopUrl import detailLaptopUrl


base_url = 'https://webscraper.io'
main_laptops_url = '/test-sites/e-commerce/allinone/computers/laptops'
#res =  requests.get(f'{base_url}{main_laptops_url}')

links = collectAllLaptopUrls(base_url + main_laptops_url)
detailLaptopUrl(base_url, links)