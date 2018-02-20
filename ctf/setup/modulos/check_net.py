#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import urllib.request


def check():
    while True:
        try:
            file = urllib.request.urlopen('http://google.com');
            print('conectado[+]');
            break;

        except urllib.error.URLError:
            print('falha[+]');
            print("check the router[+]")
            from sys import exit
            exit()
            time.sleep(3);