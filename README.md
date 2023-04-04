# Save links to my personal wiki directly from the browser

## Install
This is a for Mac OS only.

You will need [py2app](https://github.com/ronaldoussoren/py2app), then run
`python setup.py py2app`

Use [SwiftDefaultApps](https://github.com/Lord-Kamina/SwiftDefaultApps) to set
wikisave as the default app for `wikisave:` URIs.

Install SwiftDefaultApps, go to SystemPreferences where you can add a new
default app for `wikisave:`.

Use the following bookmarket in the browser of your choice:
```
javascript:url=location.href; title=document.title; if(document.getSelection)     {quote=document.getSelection();} else     {quote='';}; void(open('wikisave:' + title + '\n<br>\n' + url + '\n<br>\n' + quote, 'toolbar=no'));
```

## Usage
Press bookmarklet if on website, might show a popup.

