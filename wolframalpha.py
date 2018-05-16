#!/usr/bin/env python
#coding: utf-8

__version__ = '1.0'

import requests
import sys
import re
import os
from urllib.parse import quote
try:
    from colorama import init, Fore, Back, Style
    init()
except Exception as e:
    class Fore():
        GREEN = '** '
        RESET = ' **'
        YELLOW = ''
try:
    with open(os.path.expanduser("~/.wolfram_key"), "r") as _file:
        wolfram_alpha_key = "".join(_file.readlines())
except Exception as e:
    print('Invalid API key!\nGet one at https://developer.wolframalpha.com/portal/apisignup.html')
    api_key = input('Enter your WolframAlpha API key: ')
    wolfram_alpha_key = api_key
    with open(os.path.expanduser("~/.wolfram_key"), "w") as _file:
        _file.writelines(api_key)


def main():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input('Enter query: ')

    url = f'http://api.wolframalpha.com/v2/query?input={quote(query)}&appid={wolfram_alpha_key}&format=plaintext'

    resp = requests.get(url)

    for pod in re.findall(r'<pod.+?>.+?</pod>', resp.text, re.S):
        title = re.findall(r'<pod.+?title=[\'"](.+?)[\'"].*>', pod, re.S)
        print(Fore.GREEN + "".join(title).strip() + Fore.RESET)
        for inner in re.findall(r'<plaintext>(.*?)</plaintext>', pod, re.S):
            lines = inner.strip().split('\n')
            print(Fore.YELLOW + lines[0].strip() + Fore.RESET)
            for l in lines[1:]:
                print(l.strip())
        print()


if __name__ == '__main__':
    main()
