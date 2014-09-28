import cStringIO
import base64
import copy
import json
import httplib
import re
import time


class KubeHTTPClient():

      def __init__(self, ipaddr,port,apiversion):
        self.ipaddr = ipaddr
        self.port = port
        self.apiversion = apiversion
        self.conn = httplib.HTTPConnection(self.ipaddr+":"+self.port)

        # single global connection
      def testurl(self):

        print "hello"
        self.conn.request('GET','/')
        resp = self.conn.getresponse()
        print resp.read()

      def _get_pods(self):
        self.conn.request('GET','/api/'+self.apiversion+'/'+'pods')
        resp = self.conn.getresponse()
        print resp.read()
        print "headers"
        print resp.getheaders()


j=KubeHTTPClient("172.17.8.100","8080","v1beta1")
j._get_pods()
