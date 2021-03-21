#!/usr/bin/env ./venv/bin/python
#coding: utf-8

__version__ = '1.0'

import requests
import re
import os
from urllib.parse import quote
import argparse
try:
    from colorama import init, Fore, Back, Style
    init()
except Exception as e:
    class Fore():
        GREEN = '** '
        RESET = ' **'
        YELLOW = ''

def read_key_from_file():
    try:
        with open(os.path.expanduser("~/.wolframalpha_appid"), "r") as _file:
            wolframalpha_appid = "".join(_file.readlines())
        return wolframalpha_appid
    except Exception as e:
        print('Invalid or empty API key!\nGet one at https://developer.wolframalpha.com/portal/apisignup.html')
        api_key = input('Enter your WolframAlpha AppID: ')
        wolframalpha_appid = api_key
        with open(os.path.expanduser("~/.wolframalpha_appid"), "w") as _file:
            _file.writelines(api_key)
        return wolframalpha_appid

def main():
    parser = argparse.ArgumentParser(description="WolframAlpha cli")
    parser.add_argument("QUERY", help="Query to search in WolframAlpha (group multiple words with quotes)")
    parser.add_argument("-q", help="Quiet, only print the results", action="store_true")
    parser.add_argument("--appid", help="WolframAlpha AppID - If not informed will be asked and saved in a  file for future use")

    args = parser.parse_args()
    if (args.appid): 
        wolframalpha_appid = args.appid
    else:
        if (not args.q):
            print(f'Reading WolframAlpha AppID from {os.path.expanduser("~/.wolframalpha_appid")}')
        wolframalpha_appid = read_key_from_file()

    url = f'https://api.wolframalpha.com/v2/query?input={quote(args.QUERY)}&appid={wolframalpha_appid}&format=plaintext'

    resp = requests.get(url)

    all_pods = re.findall(r'<pod.+?>.+?</pod>', resp.text, re.S)

    for pod in all_pods:
        title = re.findall(r'<pod.+?title=[\'"](.+?)[\'"].*>', pod, re.S)
        print(Fore.GREEN + "".join(title).strip() + Fore.RESET)
        for inner in re.findall(r'<plaintext>(.*?)</plaintext>', pod, re.S):
            lines = inner.strip().split('\n')
            print(Fore.YELLOW + lines[0].strip() + Fore.RESET)
            for l in lines[1:]:
                print(l.strip())
        print()

    if all_pods and not args.q:
        print("Copy this link to open this search in your browser")
        print(f'https://www.wolframalpha.com/input/?i={quote(args.QUERY)}')
    
    if not all_pods:
        print("No results")

if __name__ == '__main__':
    main()
