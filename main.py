# -*- coding: utf-8 -*-
from time import sleep
from requests import get

import utils

utils.init()

print("Getting 2b2t player list...")
oldQueuePlayerList = get("https://2bqueue.info/players").json()["queue"]["players"]
oldMainPlayerList = get("https://2bqueue.info/players").json()["server"]["players"]
print("Done.")

while True:
    sleep(5)

    newQueuePlayerList = get("https://2bqueue.info/players").json()["queue"]["players"]
    newMainPlayerList = get("https://2bqueue.info/players").json()["server"]["players"]

    utils.compare(oldQueuePlayerList, newQueuePlayerList, oldMainPlayerList, newMainPlayerList)

    oldQueuePlayerList = newQueuePlayerList
    oldMainPlayerList = newMainPlayerList
