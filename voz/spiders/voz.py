import scrapy 


class shopeeSpider(scrapy.Spider):
    name='voz'
    allowed_domains=['voz.vn']
    start_urls=['https://voz.vn/t/bo-vo-tuong-lai-cua-cong-phuong-la-giam-doc-ngan-hang-nha-nuoc-chi-nhanh-tp-hcm.59142/page-1']
    def parse(self, response):
        for item in response.css('div.message-inner'):
            yield {
                'time'    : item.css('time.u-dt::text').get(),
                'username': item.css('a.username::text').get(),
                'message' : ','.join(item.css('div.bbWrapper::text').getall()),
                'img'     : str(item.css('div.message-avatar-wrapper img::attr("src")').get()),
        }
        next_page=response.css('div.pageNavSimple a::attr("href")')[2].get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

