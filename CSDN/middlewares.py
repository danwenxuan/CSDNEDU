# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

#监视拦截多少个爬虫spider启动，启动有多少个url
class  Start_Requests_Middleware(object):
    def process_start_requests(self, start_requests, spider):
        #打印关键信息
        print("##########1111111111 Start_Requests_Middleware %s#####%s"%(start_requests,
                                                                          spider))

        for r in start_requests:
            print("##########RRRRRRRRRRRRR Start_Requests_Middleware %s#####%s" % (r,
                                                                                spider))
            yield r

class   Process_spider_input_Middleware(object):
    def process_spider_input(self, response, spider):
        # 打印关键信息,处理输入每一个链接
        print("##########33333333333 process_spider_input %s#####%s" % (response,
                                                       spider))
        return None

class   Process_spider_output_Middleware(object):
    def process_spider_output(self, response, result, spider):
        # 打印关键信息。爬取每一个页面
        print("##########44444444444 process_spider_output %s#####%s######%s" % (response,
                                                                          spider,result))
        #返回每一个结果
        for i in result:
            print("##########55555555555 process_spider_output %s#####%s######%s" % (i,
                                                                                     spider, result))
            yield i


class CsdnSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
