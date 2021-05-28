#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import base64
import time


def get_md5(src):
    """
    Get the MD5 value
    :return:
    """
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()


def change_to_base64(s):
    """
    Encode the string with Base64
    :param s:
    :return:
    """
    return base64.b64encode(s.encode("utf-8"))


def img_to_base64(img_path):
    with open(img_path,"rb") as f:
        return base64.b64encode(f.read())


def get_current_timestamp():
    """
    Gets the current timestamp
    :return:
    """
    millis = int(round(time.time() * 1000))
    return str(millis)


def base64_to_img(data,images_path):
    """
    Restore Base64 to a picture and save it
    :param data:
    :return:
    """
    imgdata=base64.b64decode(data)
    with open(images_path,'wb') as f:
        f.write(imgdata)
