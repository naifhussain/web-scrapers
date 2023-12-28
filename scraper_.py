import scrapy
import pandas as pd

class MSpider(scrapy.Spider):
    name = "m"
    start_urls = ["https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/"]

    def parse(self, response):
        products = []
        name = response.xpath('//div[@class="catalogItemsHolder"]//article[@class="itemInfo"]')
        if name:
            for n in name:
                product = {
                    'Url': response.url,
                    'Name': n.xpath('.//a//text()').get(default='').strip(),
                    'Price': n.xpath('.//span[@class="itemPrice"]//text()').get(default='').strip()
                }
                if product not in products:
                    products.append(product)
        df = pd.DataFrame(products, columns=['Url', 'Name', 'Price'])
        df.to_csv('products.csv', index=False)