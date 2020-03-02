#!/usr/bin/env python3

import sys
import os
import web
import logging

from remote import remote

# Logging
LOG_LEVEL = logging.INFO
if os.getenv("DEBUG", "") != "":
    LOG_LEVEL = logging.DEBUG

logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S %z',
        level=LOG_LEVEL
)

if __name__ == '__main__':
    logging.info("Starting...")

    port = os.getenv("HTTP_PORT")
    if port is None:
        port = "8080"

    r = remote.Remote("light", "hitachi", "ir-a03h")

    web.start(port, r)

