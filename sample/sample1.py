# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 09:10:08 2016

@author: Yutaka
"""
from base64 import b64encode
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

def make_image_data(image_filenames):
    img_requests = []
    f = open(image_filenames, "rb")
    ctxt = b64encode( f.read()).decode('UTF-8')
    img_requests.append( 
            {
                "image":{"content":  ctxt  },
                "features":[
                    {
                        "type":"LABEL_DETECTION",
                        "maxResults":10
                    }
                ]
            }
    )
    
    img_json = json.dumps({"requests": img_requests }).encode()
    return img_json
        

if __name__ == '__main__':
    api_key = 'API_KEY'
    image_file = 'Test Image'
    
    print api_key
    print image_file
    
    request_str = make_image_data( image_file )
    
    response = requests.post(ENDPOINT_URL,
                             data=request_str,
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})
    
    print response.status_code
    print response.text
    
    
    
    
    
