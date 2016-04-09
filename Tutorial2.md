# Pythonで動かしてみる
次に、実際にPythonでスクリプトを作って動かしてみましょう。
使用するサンプルコードは[こちら](/sample/sample1.py)からも確認できます。

それでは最初から作成していきましょう。

## 必要なライブラリをimportする
今回の処理ではbase64, json, requestsのライブラリを必要とします。
必要なライブラリを最初にimportしておきます。

```
from base64 import b64encode
import json
import requests
```

## API Requestの送信先
APIの接続先を指定します。(https://cloud.google.com/vision/docs/requests-and-responses)
の情報によると、(https://vision.googleapis.com/v1/images:annotate)
にJSONのデータをPOSTしろとあるのでそのURLを定義しておきます。

```
ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
```

## JSONデータを作成する。
次にJSONのデータを作成します。
Google Cloud APIは先に行ったQuickStartで説明したとおり、JSON形式で必要なパラメータをAPIに送り、結果もJSONで受け取ります。  
先のQuickStartではGoogle Cloud Storage上に置いた画像ファイルを参照していましたが、今回はローカルのイメージを指定するようにします。
今回作成するのはいかのような関数になります。
```
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
```

### 画像ファイルを読み込む
まずは指定したファイルを読み込みます。open関数を使って読み込みます。
```
f = open(image_filenames, "rb")
```


### 画像をBase64でエンコードする

ローカルの画像ファイルを送信するために、まずはBase64に変換する必要があります。
そのための処理がいかになります。
```
ctxt = b64encode( f.read()).decode('UTF-8')
```
ここで、decodeで文字コードはUTF-8を指定しておかないとAPIにはじかれる場合があるのでご注意を。

### JSONのデータを作成する
Base64に変換したデータを使って送信するJSONのデータを作成します。

```
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

```
このなかでfeaturesの中を変えることで使う機能を切り替えることができます。

ここまできたらjson.dumpを使ってrequestできる形式にします。
```
img_json = json.dumps({"requests": img_requests }).encode()
```

## APIに通知して結果を得る
JSONのデータができたらAPIにPOSTして結果を受け取ります。
```
response = requests.post(ENDPOINT_URL,
                         data=request_str,
                         params={'key': api_key},
                         headers={'Content-Type': 'application/json'})
```
ここで、api_keyには先に作成したブラウザキーを設定します。
応答がresponseに戻ってきます。response.status_codeにはステータスコードが、response.textにはJSON形式の応答データが入ってきます。
エラーかチェックするにはstatus_codeが200であることを確認します。

これでPythonからGoogle Cloud APIにアクセスすることができるようになりました。

実際に動かすと、以下のようなJSON形式の応答が戻ります。

```

{
  "responses": [
    {
      "labelAnnotations": [
        {
          "mid": "/m/03qtwd",
          "description": "crowd",
          "score": 0.90327162
        },
        {
          "mid": "/m/0ltv",
          "description": "auto racing",
          "score": 0.50959766
        }
      ]
    }
  ]
}

```

実際にPythonでjsonを扱う場合にはJSON形式のデータからPythonのデータ形式に変換する必要があります。


参考URL：
Python 2.7系列 http://docs.python.jp/2.7/library/json.html  
Python 3系列 http://docs.python.jp/3/library/json.html  



以下に今回作成したサンプルをすべて載せておきます。

```
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


```
