import requests
import configparser
from lxml import etree


class URLTool(object):

    entire_url = ''
    target = ''

    def conf_reader(self, config_file_path='info.conf'):
        cf = configparser.ConfigParser()
        cf.read(config_file_path)
        self.entire_url = cf.get("URL", "entire_url")
        self.target = cf.get("URL", "target")

    def get_urls(self):
        urls = []
        self.conf_reader()
        for i in range(1, 4):
            url = self.entire_url + str(i)
            r = requests.get(url)
            selector = etree.HTML(r.text)
            # get records quantity
            count = len(selector.xpath('//div[@class="product"]'))
            for each in range(count):
                path = '//div[@class="product"][%d]/a/@href' % (each + 1)
                url = selector.xpath(path)
                real_path = self.target + url[0]
                urls.append(real_path)
        return urls

if __name__ == '__main__':
    ut = URLTool()
    list = ut.get_urls()
    for each in list:
        print(each)
