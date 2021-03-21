# WolframAplha CLI

Command Line Interface to run queries on [WolframAlpha](http://www.wolframalpha.com)

## Usage

```shell
usage: wa [-h] [-q] [--appid APPID] QUERY

WolframAlpha cli

positional arguments:
  QUERY          Query to search in WolframAlpha (group multiple words with quotes)

optional arguments:
  -h, --help     show this help message and exit
  -q             Quiet, only print the results
  --appid APPID  WolframAlpha AppID - If not informed will be asked and saved in a file for future use
```