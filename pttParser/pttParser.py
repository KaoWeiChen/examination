#! /usr/bin/env python3

import httplib2

from html.parser import HTMLParser

class pttParser():

    def __init__(self,lookside):
        self.url =  "https://www.ptt.cc/bbs/" +lookside

    def getPttContent(self):
        return self.getDataFromURL(self.url)
        
    def getDataFromURL(self, url):
        h = httplib2.Http()
        resp, content = h.request(url)
        content = content.decode()
        return  content

class MyHTMLParser(HTMLParser):
    start = False
    content =""
    result=[]
    row =[]

    def handle_starttag(self, tag, attrs):
        print (tag)
    def handle_endtag(self, tag):
        print (tag)
    def handle_data(self, data):
        print (data)

if __name__  == "__main__":

    myPttParser = pttParser("NBA")
    data = myPttParser.getPttContent()
    parser = MyHTMLParser()
    parser.feed(data)
