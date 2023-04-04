#!/usr/bin/env python3

import sys
import urllib.parse
import datetime as dt
import traceback

PROTOCOL = 'wikisave:'

"""
Use the following bookmarklet:

```
javascript:url=location.href; title=document.title; if(document.getSelection)     {quote=document.getSelection();} else     {quote='';}; void(open('wikisave:' + title + '\n<br>\n' + url + '\n<br>\n' + quote, 'toolbar=no'));
```

Also need to set savetowiki as the default program to open `wikisave:` URLs.


"""

with open('/Users/cg/workspace/wiki/autosave.md', 'a', encoding='utf-8') as file:
    try:
        data = sys.argv[1]
        try:
            data = urllib.parse.unquote(data)
        except Exception:
            pass
        if data[:len('wikisave:')] == PROTOCOL:
            data = data[len(PROTOCOL):]
        try:
            title, url, citation = data.split('<br>', maxsplit=2)
        except ValueError:
            title = data
            url = citation = ''

        file.write(f'## {dt.date.today():%Y-%m-%d}\n')
        citation = f' {citation}' if citation != '' else citation
        file.write(f'[{title}]({url}) {citation}\n')
        file.write('\n')
    except Exception as error:
        file.write(str(error))
        file.write('\n')
