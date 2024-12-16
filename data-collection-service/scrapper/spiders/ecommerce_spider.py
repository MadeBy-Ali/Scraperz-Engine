import scrapy

from bs4 import BeautifulSoup

from scrapy.crawler import CrawlerProcess

class ECommerceSpider(scrapy.Spider):
    name = "ecommerce_spider"
    start_url = ["https://shopee.co.id/Pro-4-TWS-Headset-Bluetooth-TWS-with-Mic-Smart-Touch-Control-Earphone-HiFi-Stereo-Headset-Wireless-i.52922719.19893051668?sp_atk=3da5009c-f4d1-4bc0-82c4-654f63623ecc&xptdk=3da5009c-f4d1-4bc0-82c4-654f63623ecc"]
    
    def parse(self, respone):
        soup = BeautifulSoup(respone.body, "html.parser")
        products = []
        
        # Extract product details
        for product in soup.select(".product-item"):
            products.append({
                "name": product.select_one(".product-title").text.strip(),
                "price": product.select_one(".product-price").text.strip(),
                "url": product.select_one("a")["href"],
            })
        
        yield {"products": products}