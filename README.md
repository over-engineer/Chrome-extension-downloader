# Chrome extension downloader
Downloads crx files of Chrome extensions

## Usage
```
python download_extension.py extension_url [browser_version='49.0']
```

- Open the [Chrome Web Store](https://chrome.google.com/webstore/)
- Find an extension you like and click on it
- Copy the url (which looks like this `https://chrome.google.com/webstore/detail/extension/abcdefabcdefabcdefabcdefabcdefab`)
- Run the Python script passing the extension url as an argument
- Optionally, pass a second argument with the browser version

For example
```
python download_extension.py https://chrome.google.com/webstore/detail/extension/abcdefabcdefabcdefabcdefabcdefab 49.0
```

You need [Python 2.7](https://www.python.org/download/releases/2.7/) 
to run this script.

## License

The MIT License, check the `LICENSE` file
