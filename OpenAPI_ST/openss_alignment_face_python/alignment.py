# -*- coding: utf-8 -*-

"""
Facial keypoints detect case
"""
import json
import os

import requests

import utils

# Authentication token request url
token_url = "https://open.study.sensetime.com/api/common/v1/token"
# Facial keypoints detect request url
alignment_url = "https://open.study.sensetime.com/api/internal_sdk/v1/alignment"
# API calling access key
ACCESS_KEY_ID = "ZS3jAnJ3gk0rT3dj";
ACCESS_KEY_SECRET = "sRhnCCrgpXnCusU8SBPVZKgIn6OMNAJM";
# Image resource
file_name = "source_image.jpeg"
file_path = os.path.join(".", file_name)

# obtain authentication token
headers = {"languageType": "zh_CHS"}
token_params = {"accessKeyId":ACCESS_KEY_ID, "accessKeySecret":ACCESS_KEY_SECRET}
token_response = requests.get(url=token_url, headers=headers, params=token_params, verify=False).text
token = json.loads(token_response).get("data")

if not token:
    print("failed to obtain authentication token")
else:
    # request headers
    headers = {"languageType": "zh_CHS", "X-Authorization": token}
    # request parameters
    params = {"rotateDegree": 0, "modelType": 0, "isResponseImageRequired": True}

    use_binary = False

    if use_binary:
        binary_files = {'file': (file_name, open(file_path, 'rb'))}
        response = requests.post(url=alignment_url, headers=headers, data=params, files=binary_files, verify=False).text
        response = json.loads(response)
        print(json.dumps(response, ensure_ascii=False))
    else:
        base64_img = utils.img_to_base64(file_path)
        base64_files = {'base64Image': (None, base64_img)}
        response = requests.post(url=alignment_url, headers=headers, data=params, files=base64_files, verify=False).text
        response = json.loads(response)
        print(json.dumps(response, ensure_ascii=False))
    
    # If isResponseImageRequired is set to True, store the processed image
    response_data = response.get('data')
    if response_data:
        base64_img_data = response_data.get('base64ImageDst')
        if base64_img_data and base64_img_data != '':
            utils.base64_to_img(base64_img_data, utils.get_current_timestamp() + ".jpg")
