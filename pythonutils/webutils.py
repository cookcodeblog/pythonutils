# Web utils
import urllib.parse
import re
import os
import requests


def unquote(s):
    """
    Replace %xx
    :param s: %xx
    :return: Decoded string
    """
    return urllib.parse.unquote(s)


def quote(s):
    """
    Replace plain text with %xx
    :param s: Plain text
    :return: %xx
    """
    return urllib.parse.quote(s)


def fake_request_headers(refer='', cookie=''):
    """
    Build a fake HTTP request headers won't be blocked via server

    :param refer: Refer of HTTP request headers
    :param cookie: Cookie of HTTP request headers
    :return: A faked HTTP request headers
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Refer': refer,
        'Cookie': cookie
    }
    return headers


def get_attachment_name(content_disposition, is_unquote=True):
    if not content_disposition:
        return None
    file_names = re.findall('filename=(.+)', content_disposition)
    if len(file_names) == 0:
        return None
    if is_unquote:
        return unquote(file_names[0])
    else:
        return file_names[0]


def get_attachment_name_of_response(response, is_unquote=True):
    return get_attachment_name(response.headers.get('content-disposition'), is_unquote)


def download_file(url, target_file=None):
    """
    Download small file by HTTP get, allow redirects

    https://likegeeks.com/downloading-files-using-python

    :param url: File url
    :param target_file: Target file, default is None;
    when target file is None, get file name from content-disposition
    :return: None
    """
    response = requests.get(url=url, allow_redirects=True)
    file_name = get_attachment_name_of_response(response)
    if not target_file and file_name:
        target_file = file_name
    with open(target_file, 'wb') as file:
        file.write(response.content)


def download_large_file(url, target_file=None, chunk_size=1024):
    """
    Download large file by HTTP get, chunk by chunk, allow redirects

    :param url: File url
    :param target_file: Target file, default is None;
    when target file is None, get file name from content-disposition
    :param chunk_size: Chunk size, default is 1024
    :return: None
    """
    response = requests.get(url=url, allow_redirects=True, stream=True)
    file_name = get_attachment_name_of_response(response)
    if not target_file and file_name:
        target_file = file_name
    with open(target_file, 'wb') as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
