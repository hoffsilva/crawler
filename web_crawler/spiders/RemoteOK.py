# -*- coding: utf-8 -*-
import scrapy
from web_crawler.items import WebCrawlerItem

class RemoteokSpider(scrapy.Spider):
    name = 'RemoteOK'
    allowed_domains = ['remoteok.io/remote-dev-jobs']
    start_urls = ['http://remoteok.io/remote-dev-jobs/']



    def parse(self, response):
        currentJob = WebCrawlerItem(companyName="", jobDescription="", companyURL="", applyURL="", jobTitle="", tags="")
        jobs = [WebCrawlerItem]
        for company in response.css("tr td.company.position.company_and_position a.companyLink h3 ::text").extract():
            currentJob.companyName = company
        for description in response.css("tr td.heading div.expandContents div.description div").extract():
            currentJob.jobDescription = description
        for item in response.css("tr td.tags a").extract():
            currentJob.tags = item
        for logo in response.css("tr td a.preventLink div.logo::attr(src)").extract():
            currentJob.companyURL = logo
        for application in response.css("tr td.source a.no-border.tooltip ::attr(href)").extract():
            currentJob.applyURL= application
        for title in response.css("tr td.company.position.company_and_position a.preventLink h2 ::text").extract():
            currentJob.jobTitle = title

        yield currentJob
