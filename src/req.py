#!/usr/bin/env python

'''
Used to use requestes module to requeste website and save the data return the data.
Will use random data to pretend manually requst from different http head.
explorer, time... 
should keep in thread safe.
'''
import requests
import threading
import time
import random

websites = [
'http://www.baidu.com',
'http://www.zhihu.com',
'https://www.github.com']
UAs = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
]


class RequestThread(threading.Thread):
    """Request some, every Request would be a single thread."""
    def __init__(self, threadId, threadName, waitTime = None):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.waitTime = waitTime if waitTime is not None else random.randint(10,60)


    def run(self):
        print("%s-(%d)-RequestThread-start-waitTime(%d)" % (self.threadName, self.threadId, self.waitTime))
        time.sleep(self.waitTime)
        global websites
        website = random.choice(websites)
        r = self.webRequest(website)
        if r.status_code == 200:
            print("------Success get website(%d): %s -------" % (r.status_code, website))
        else:
            print("!!!!!!Failuse get website(%d): %s -------" % (r.status_code, website))
        print("%s-(%d)-RequestThread-end" % (self.threadName, self.threadId))

    #0.start create http header
    def getWebHeader(self):
        global USA
        return {'User-Agent': random.choice(UAs)}
    #1.start request
    def webRequest(self, website):
        '''Use requsts to start requst http website'''
        self.r = requests.get(website, headers = self.getWebHeader())
        return self.r

    #2.return request
    def saveWebSite(self):
        '''To save website to a special container'''
        pass

if __name__ == '__main__':
    for i in range(2):
        RequestThread(i, "Thread-(%d)-main" % i, random.randint(1,5)).start()
    print("Exit Main Function")
