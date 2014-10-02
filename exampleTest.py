import cStringIO
import base64
import copy
import json
import httplib
import socket
import re
import time
import string

MATCH = re.compile(
    '(?P<app>[a-z0-9-]+)_?(?P<version>v[0-9]+)?\.?(?P<c_type>[a-z]+)?.(?P<c_num>[0-9]+)')

POD_TEMPLATE = '''{
  "id": "$id",
  "kind": "$pod",
  "apiVersion": "$version",
  "desiredState": {
    "manifest": {
    "version": "$version",
    "id": "$id",
    "containers": [{
      "name": "master",
      "image": "dockerfile/redis",
      "ports": [{
        "containerPort": 6379,
        "hostPort": 6379
      }]
    }]
    }
  },
  "labels": {
  "name": "$name"
  }
}'''



def create(id,pod,version,name):
  l = {}
  l["id"]=id
  l["pod"]=pod
  l["version"]=version
  l["name"]=name
  template=string.Template(POD_TEMPLATE).substitute(l)
  print template
  print copy.deepcopy(template)
  print json.dumps(template)


create("redis","Pod","v1beta1","ramz")
