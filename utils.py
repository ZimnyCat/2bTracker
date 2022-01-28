# -*- coding: utf-8 -*-
from requests import post

names = []


def init():
    createWebhookTXT()
    loadNames()


def createWebhookTXT():
    try:
        open("webhook.txt", "r").close()
    except FileNotFoundError:
        open("webhook.txt", "w").close()


def loadNames():
    try:
        f = open("names.txt", "r")
        for line in f.readlines():
            names.append(line.replace("\n", ""))
        f.close()
    except FileNotFoundError:
        f = open("names.txt", "w")
        f.write("popbob")
        f.close()
        names.append("popbob")


def compare(qold, qnew, mainold, mainnew):
    action = "joined the queue"
    for line in qnew:
        if line not in qold:
            print(line, action)
            send(line, action)
    action = "left the queue"
    for line in qold:
        if line not in qnew:
            print(line, action)
            send(line, action)
    action = "joined the main server"
    for line in mainnew:
        if line not in mainold:
            print(line, action)
            send(line, action)
    action = "left the main server"
    for line in mainold:
        if line not in mainnew:
            print(line, action)
            send(line, action)


def send(name, action):
    if name in names:
        print("------\n" + name + " just " + action + ", sending POST request to the webhook...")
        try:
            f = open("webhook.txt", "r")
            post(f.read().replace("\n", ""), json={"content": name + " " + action})
            print("Sent!")
            f.close()
        except:
            print("Webhook (webhook.txt) is invalid!")
        print("------")
