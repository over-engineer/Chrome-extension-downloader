#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Downloads crx files
# of Chrome extensions
#
# Copyright (c) 2018 Konstantinos
# Version: 0.1.0

import os
import sys
import urllib
import zipfile


def get_extension_id(arg):
    """
    Return the extension id from the given console argument

    :param arg: The console argument
    :return: The extension id
    """

    if arg.startswith('http://'):
        arg = arg.replace('http://', 'https://')

    if arg.startswith('https://'):
        return arg.split('/')[-1:][0]

    return arg


def get_crx_url(extension_id, browser_version='49.0'):
    """
    Return the URL to download the crx file for the extension with the given extension id

    :param extension_id: The id of the extension we want to get its crx url
    :param browser_version: The Chrome version (defaults to '49.0')
    :return: The url to download the crx file
    """

    return ('https://clients2.google.com/service/update2/crx?response=redirect&prodversion={version}'
            '&x=id%3D{extension_id}%26installsource%3Dondemand%26uc'.format(version=browser_version,
                                                                            extension_id=extension_id))


def get_script_path():
    """
    Return the path to the directory of the script

    :return: The path to the directory of the script
    """

    return os.path.dirname(os.path.realpath(__file__))


def download_extension(extension_id, browser_version):
    """
    Download the crx file for the extension with the given extension id

    :param extension_id: The id of the extension
    :param browser_version: The Chrome version
    :return: A tuple with the (filename, path) of the downloaded crx file
    """

    crx_url = get_crx_url(extension_id, browser_version)
    print 'Downloading {crx_url}...'.format(crx_url=crx_url)
    status_code = urllib.urlopen(crx_url).getcode()

    if status_code == 200:
        # TODO: Replace the filename with the name of the Chrome extension
        filename = '{0}.crx'.format(extension_id)
        dst_path = os.path.join(get_script_path(), filename)

        try:
            urllib.urlretrieve(crx_url, dst_path)
        except Exception as e:
            print 'Couldn\'t download the crx file ({0})'.format(e)
            return None
        else:
            print 'Chrome extension crx file downloaded successfully'
            return (filename, dst_path)
    else:
        print 'Couldn\'t download the crx file (status code: {0})'.format(status_code)
        return None


def extract_archive(filename, path):
    """
    Extract the contents of the given archive

    :param filename: The name of the crx file
    :param path: The path to the crx file
    :return: Whether the contents of the crx file were extracted successfully or not
    """

    dst_dir = os.path.join(get_script_path(), filename[:-4])
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print 'Directory {dir} created'.format(
            dir=filename[:-4])

    try:
        print 'Extracting the contents of {0}...'.format(filename)
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall(dst_dir)
        zip_ref.close()
    except Exception as e:
        print 'Couldn\'t extract the contents of the crx file ({0})'.format(e)
        return False
    else:
        print 'Extracted successfully'
        return True


def main():
    # Confirm that we got the extension url (or extension id)
    if len(sys.argv) == 1:
        print 'Expected at least 2 arguments, got 1'
        return

    # If the console argument is -h, --h, help, or -help, display the help message
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--h', 'help', '-help']:
        print ('Usage: python {filename} extension_url browser_version'
               '\ne.g. python {filename} {extension_url} 49.0'.format(
                filename=sys.argv[0],
                extension_url='https://chrome.google.com/webstore/detail/extension/abcdefabcdefabcdefabcdefabcdefab'))
        return

    # Get the extension id and crx url
    extension_id = get_extension_id(sys.argv[1])

    # Get the browser version (if there is a third console argument)
    browser_version = sys.argv[2] if len(sys.argv) == 3 else '49.0'

    # Download the crx file
    print 'Fetching extension \'{extension_id}\'...'.format(extension_id=extension_id)
    crx_tuple = download_extension(extension_id, browser_version)
    if crx_tuple is not None:
        extract_archive(*crx_tuple)


if __name__ == '__main__':
    main()
