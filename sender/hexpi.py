#!/usr/bin/env python3

import urllib.request, json

def send(signal):
    url = "http://192.168.20.100:8081/api/v1/ir"

    entry = {"code": signal}
    json_data = json.dumps(entry).encode("utf-8")

    request = urllib.request.Request(url, data=json_data, method="POST", headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
