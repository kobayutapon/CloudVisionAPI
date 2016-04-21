# 検出方法と応答の違い

## LOGO_DETECTION
LOGO_DETECTIONで戻ってくる応答ファイルの例を示します。
このような画像ファイルを認識させた場合、以下のような応答ファイルが戻ります。  

![](./image/vaio.jpg)

```
{
  "responses": [
    {
      "logoAnnotations": [
        {
          "mid": "/m/01g5tx",
          "description": "VAIO",
          "score": 0.16112483,
          "boundingPoly": {
            "vertices": [
              {
                "x": 327,
                "y": 43
              },
              {
                "x": 420,
                "y": 43
              },
              {
                "x": 420,
                "y": 161
              },
              {
                "x": 327,
                "y": 161
              }
            ]
          }
        }
      ]
    }
  ]
}
```
* mid
ナレッジグラフ用のIDが入ります。ナレッジグラフに関してはこちらを参照してください。
https://developers.google.com/knowledge-graph/#knowledge_graph_entities

* description  
検出したロゴの名称がはいります。  

* score  
検出結果の確度を示します。0から1の間の値が入ります。  

* boundingPoly  
検出したロゴの境界情報が格納されます。2次元のポリゴンで指定され、後述するverticesで頂点の位置が指定されます。  

* vertices  
boundingPolyで検出したポリゴンの頂点の座標です。2次元座標で、x, yの要素で構成されます。  

## LANDMARK_DETECTION
LANDMARK_DETECTIONは画像から位置情報などを取得するものです。  
例えばこのような画像（たしかベイブリッジだったはず）を行うと、次のような応答が戻ってきます。  
![](./image/bridge.jpg)


応答例  
```
"landmarkAnnotations": [
  {
    "mid": "/m/07dfk",
    "description": "Tokyo",
    "score": 0.25928351,
    "boundingPoly": {
      "vertices": [
        {
          "x": 163,
          "y": 685
        },
        {
          "x": 481,
          "y": 685
        },
        {
          "x": 481,
          "y": 748
        },
        {
          "x": 163,
          "y": 748
        }
      ]
    },
    "locations": [
      {
        "latLng": {
          "latitude": 35.651009,
          "longitude": 139.76073
        }
      }
    ]
  }
],
```

* mid
ナレッジグラフ用のIDが入ります。ナレッジグラフに関してはこちらを参照してください。
https://developers.google.com/knowledge-graph/#knowledge_graph_entities

* description  
検出したランドマークの名称が入ります。ここではTokyoとなっています。  

* score  
検出結果の確度を示します。0から1の間の値が入ります。  

* boundingPoly  
検出したロゴの境界情報が格納されます。2次元のポリゴンで指定され、後述するverticesで頂点の位置が指定されます。  

* vertices  
boundingPolyで検出したポリゴンの頂点の座標です。2次元座標で、x, yの要素で構成されます。  

* locations
 位置情報が入ります。緯度、経度がそれぞれlatitutude, longitudeに入ります。入る値はそれぞれ-90°～90°,-180°～180°となります。  
 位置情報はWGS84 Standardに準拠します。
