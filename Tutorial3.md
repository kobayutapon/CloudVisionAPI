# 検出方法を変えてみる

次にいろいろな識別方法を試してみましょう。

識別方法を切り替えるのは、JSONのfeaturesの中を変更します。
```
{
    "image":{"content":  ctxt  },
    "features":[
        {
            "type":"LABEL_DETECTION",
            "maxResults":10
        }
    ]
}
```
ここのtypeで、何を識別するかを指定します。
ドキュメントは[ここ](https://cloud.google.com/vision/reference/rest/v1/images/annotate?hl=ja)で確認できます。  
また、featuresの中に、以下のように複数指定することで同時に解析を行うこともできます。
```
{
    "image":{"content":  ctxt  },
    "features":[
        {
            "type":"LABEL_DETECTION",
            "maxResults":10
        },
        {
            "type":"LOGO_DETECTION",
            "maxResults":10
        },
        {
            "type":"FACE_DETECTION",
            "maxResults":10
        },
        {
            "type":"LANDMARK_DETECTION",
            "maxResults":10
        }
    ]
}
```

featuresのtypeには以下のパラメータが設定できます。

|設定値|説明|
|:-----|----|
|TYPE_UNSPECIFIED |	Unspecified feature type.|
|FACE_DETECTION	| Run face detection.|
|LANDMARK_DETECTION |	Run landmark detection.|
|LOGO_DETECTION	| Run logo detection. |
|LABEL_DETECTION	| Run label detection. |
|TEXT_DETECTION	| Run OCR. |
|SAFE_SEARCH_DETECTION	 | Run various computer vision models to compute image safe-search properties. |
|IMAGE_PROPERTIES	 | Compute a set of properties about the image (such as the image's dominant colors).|

maxResultsは確からしい順番でいくつ戻すか、を指定します。10にすると確からしい10個が戻ってきます。10個もない場合はあるだけ戻ってきます。

なお、それぞれの認識画像については推奨設定があります。
詳細はこちら(https://cloud.google.com/vision/docs/image-best-practices)で確認できます。  
簡単にまとめると  

画像形式
* JPEG  
* PNG8/24  
* GIF/Animated GIF (first frame only)  
* BMP
* WEBP
* RAW
* ICO

推奨解像度
* FACE_DETECTION: 1600 x 1200
* LANDMARK_DETECTION: 640 x 480
* LOGO_DETECTION: 640 x 480
* LABEL_DETECTION: 640 x 480
* TEXT_DETECTION: 1024 x 768
* SAFE_SEARCH_DETECTION: 640 x 480

使用リミット
* MB per image: 4 MB
* MB per request: 8 MB
* Requests per second: 10
* Requests per feature per day: 700,000
* Requests per feature per month: 20,000,000
* Images per second: 8
* Images per request: 16

となります。これらの制限を踏まえないと、誤検出しやすくなります。
同じ画像で解像度を変えた場合の例を載せます。片方はFull-HDの解像度、もう片方がGoogleのImage検索の際に縮小されたものを使った結果です。

* Full HD
```
"labelAnnotations": [
  {
    "mid": "/m/09j2d",
    "description": "clothing",
    "score": 0.98353541
  },
  {
    "mid": "/m/01g317",
    "description": "person",
    "score": 0.9257217
  },
  {
    "mid": "/m/03bt1vf",
    "description": "woman",
    "score": 0.88134611
  },
  {
    "mid": "/m/0250x",
    "description": "costume",
    "score": 0.78441125
  }
]
```

* 縮小画像
```
"labelAnnotations": [
  {
    "mid": "/m/09j2d",
    "description": "clothing",
    "score": 0.98163253
  },
  {
    "mid": "/m/0250x",
    "description": "costume",
    "score": 0.7833634
  },
  {
    "mid": "/m/025dq0",
    "description": "sari",
    "score": 0.55992115
  }
]
```
どちらも服があって、コスチュームっぽいということは認識できていますが、Ful-HD画像のほうは人がいて、それが女性であることまで検出できています。縮小画像のほうはなぜかサリーと認識していますね。。。  
このように、検出したいものに合わせて適切に解像度などを合わせる必要があります。



いろいろ変えてどうなるか試してみましょう。
