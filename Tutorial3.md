# Pythonで動かしてみる
次にいろいろな識別方法を試してみましょう。

識別方法を切り替えるのは、JSONのfeaturesの中を変えます。
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
ここのtypeで、何を識別するかを指定します。ドキュメントは[ここ](https://cloud.google.com/vision/reference/rest/v1/images/annotate?hl=ja)で確認できます。
ここでは簡単に何ができるかを示します。

|設定値|説明|
|:-----|----|
|TYPE_UNSPECIFIED |	Unspecified feature type.|
|FACE_DETECTION	| Run face detection.|
|LANDMARK_DETECTION |	Run landmark detection.|
|LOGO_DETECTION	| Run logo detection. |
|LABEL_DETECTION	| Run label detection. |
|TEXT_DETECTION	| Run OCR. |
| SAFE_SEARCH_DETECTION	 | Run various computer vision models to compute image safe-search properties. |
|IMAGE_PROPERTIES	 | Compute a set of properties about the image (such as the image's dominant colors).|

maxResultsは確からしい順番でいくつ戻すか、を指定します。10にすると確からしい10個が戻ってきます。10個もない場合はあるだけ戻ってきます。

いろいろ変えてどうなるか試してみましょう。
