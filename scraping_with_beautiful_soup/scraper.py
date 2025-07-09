import re

from constants import BASE_URL
from utils import get_soup_by_selenium_driver


def get_product_details(soup):
    # get product details
    name_el = soup.find('div', id='scroll_car_info')
    name = name_el.get_text(separator='\n', strip=True).split('\n')[0]

    price_el = soup.find('div', class_='price-box').find("strong").get_text(strip=True)
    price = re.sub(r'(\d)([A-Za-z])', r'\1 \2', price_el)

    location = soup.select_one("p.detail-sub-heading i").find_parent("a").get_text(strip=True)

    model_year = soup.find('span', class_='engine-icon year').parent.get_text(strip=True)

    mileage = soup.find('span', class_='engine-icon millage').parent.get_text(strip=True)

    seller_name_data = soup.find('div', class_='owner-detail-main').get_text(separator=',', strip=True).split(',')

    # checking "is seller 'Dealer' or not?"
    seller_name = seller_name_data[0]
    if seller_name == 'Dealer:':
        seller_name = seller_name_data[1]

    featured_or_not = soup.find('div', id='myCarousel').get_text(separator=',', strip=True).split(',')[0]
    is_featured = featured_or_not == 'FEATURED'

    images_carousel = soup.select_one("div#myCarousel div[class*='img-box'] ul")
    all_images = images_carousel.find_all('img')

    cover_image_url = all_images[1]['data-original'] if len(all_images) > 1 else all_images[0]['data-original']
    image_1_url = all_images[2]['data-original'] if len(all_images) > 2 else None
    image_2_url = all_images[3]['data-original'] if len(all_images) > 3 else None

    return {
        'name': name,
        'price': price,
        'location': location,
        'model_year': model_year,
        'mileage': mileage,
        'seller_name': seller_name,
        'is_featured': is_featured,
        'cover_image_url': cover_image_url,
        'image_1_url': image_1_url,
        'image_2_url': image_2_url,
    }


# def get_last_page(url):
#     soup = get_soup_by_selenium_driver(url)
#
#     last_page_url_data = soup.find('li', class_='last next')
#
#     if last_page_url_data:
#         last_page_url = last_page_url_data.find('a')['href']
#         return BASE_URL + last_page_url
#
#     return None


def get_last_page_index(last_page_url):
    # regex (Regular expression) pattern to find the page number
    pattern = r'page=(\d+)$'

    # Search for the pattern
    match = re.search(pattern, last_page_url)
    page_number = match.group(1)

    return int(page_number)


def get_page_urls(url):
    page_urls_list = [url]
    first_page_soup = get_soup_by_selenium_driver(url)

    last_page_url_data = first_page_soup.find('li', class_='last next')
    if last_page_url_data:
        last_page_url = BASE_URL + last_page_url_data.find('a')['href']
        last_page_index = get_last_page_index(last_page_url)

        for page_num in range(2, last_page_index + 1):
            page_urls_list.append(f'{url}?page={page_num}')

    return page_urls_list, first_page_soup


def get_product_urls(page_urls, first_page_soup=None):
    product_urls_list = []

    for index, url in enumerate(page_urls):
        soup = first_page_soup if index == 0 and first_page_soup else get_soup_by_selenium_driver(url)
        all_product_urls = soup.find_all('a', class_='car-name ad-detail-path')

        # avoiding products other-then that user selected
        city_or_province_value = soup.find('input', id='selected_city_slug')
        normalized_pattern = city_or_province_value['value'].replace("-", "-?")

        for product_url in all_product_urls:
            if re.search(normalized_pattern, str(product_url)):
                product_urls_list.append(f'{BASE_URL}{product_url["href"]}')

    return product_urls_list


def get_all_product_details(product_urls_list):
    products = []

    for product_url in product_urls_list:
        soup = get_soup_by_selenium_driver(product_url)
        products.append(get_product_details(soup))

    return products
