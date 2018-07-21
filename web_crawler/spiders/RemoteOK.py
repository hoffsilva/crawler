# -*- coding: utf-8 -*-
import scrapy


class RemoteokSpider(scrapy.Spider):
    name = 'RemoteOK'
    allowed_domains = ['remoteok.io/remote-dev-jobs']
    start_urls = ['http://remoteok.io/remote-dev-jobs/']

    def parse(self, response):
        for title in response.css("tr td a h2 ::text").extract():
            jobTitle = title
        for company in response.css("tr td a h3 ::text").extract():
            companyName = company
        for description in response.css("tr td div.expandContents div.description").extract():
            jobDescription = description
        for logo in response.css("tr td a.preventLink div.logo::attr(src)").extract():
            companyURL = logo

        yield {'jobTitle': title, 'companyName': companyName, 'jobDescription': jobDescription, 'companyURL': companyURL}
