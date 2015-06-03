__author__ = 'vishal'

import urllib2
import cookielib

class Utils(object):

    def __init__(self, host, key):
        self.host = host
        self.key = key
        self.cookiejar = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejar))
        urllib2.install_opener(self.opener)

    def get_request(self, absolute_url):
        print self.host+absolute_url+"?api_key="+self.key
        request = urllib2.Request(self.host+absolute_url+"?api_key="+self.key)
        request.get_method = lambda : "GET"
        response = self.opener.open(request)
        return response

