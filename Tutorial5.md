# 検出方法と応答の違い

## LOGO_DETECTION
LOGO_DETECTIONで戻ってくる応答ファイルの例を示します。
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
