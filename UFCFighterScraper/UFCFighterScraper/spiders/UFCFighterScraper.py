import scrapy

class UFCFighterSpider(scrapy.spider):
    name = "UFCFighter"

    start_urls = ["http://www.ufcstats.com/statistics/fighters"]

    def parse(self, response):
        char = getattr(response.url, "char", None)
        page = getattr(response.url, "page", None)
        table_rows = response.xpath("""//table[@class='b-statistics__table']
                                    //tbody//tr""")
        for row in table_rows[2:]:
            fight_page = row.xpath('td/a/@href').extract_first