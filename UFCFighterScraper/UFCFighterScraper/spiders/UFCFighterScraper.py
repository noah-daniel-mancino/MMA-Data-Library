import scrapy
import string


class UFCFighterSpider(scrapy.spider):
    name = "UFCFighter"

    # The pages are alphabetized by last name.
    start_urls = ["http://www.ufcstats.com/statistics/fighters?" +
                  f"char={c}&page=all" for c in string.ascii_lowercase]

    def parse(self, response):
        table_rows = response.xpath("""//table[@class='b-statistics__table']
                                    //tbody//tr""")
        if table_rows is not None: # I heard Rubens Xavier might get cut...
            for row in table_rows[2:]:
                fighter_page = row.xpath('td/a/@href').extract_first()
                yield response.follow(fighter_page, callback=parse_fighter_page)

    def parse_fighter_page(self, response):
        pass