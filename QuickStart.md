
#Quick Startを試してみる

それではGoogle Cloud Vision APIのQuick Startの内容に沿ってどのような内容が戻ってくるか試してみましょう。  
Quick Start は以下のURLから参照できます。  
https://cloud.google.com/vision/docs/getting-started?hl=ja


##画像データの保存
Quick Startの内容にそって、画像データをGoogle Cloud Storage上にアップロードします。
まず、Google Cloud StorageでBucketを作成します。
![Image1](/image/QuickStart1_f.jpg)

バケット名を指定する画面が出てくるので名前を入力し、作成をクリックします。
![Image2](/image/QuickStart2_f.jpg)
この時、バケットの名前はユニークなものでなくてはいけません。

作成が完了すると以下のような画面になります。
画面の上にある"ファイルをアップロード"をクリックし、試したい画像をアップロードします。
![Image2](/image/QuickStart3_f.jpg)

お試し画像の準備が終わったら[ここ](https://cloud.google.com/vision/reference/rest/v1/images/annotate?hl=ja#try-it)のサイトで試してみます。
このような画面になるので、Request bodyのフォームの部分をクリックします。
![Image2](/image/QuickStart4_f.jpg)

すると、以下のようにプルダウンが開くので、"requests"を選びます。
![Image2](/image/QuickStart5_f.jpg)

選択したあと、もう一度フォームの中をクリックすると以下のように項目横にアイコンが出てきます。
緑の＋をクリックします。
![Image2](/image/QuickStart6_f.jpg)

で、ここでfeaturesを選びます。
![Image2](/image/QuickStart7_f.jpg)

ということを繰り返して以下のように設定します。
![Image2](/image/QuickStart8_f.jpg)
typeは使用する検出方式を指定します。
gcsImageUriはGoogle Cloud Storageで作成したバケット名とファイル名を指定します。

ここまで指定したらExecuteをクリックし、実行します。

しばらくするとAPIに対して通知された内容と、それに対する応答がJSON形式で表示されます。

通知
```

POST https://vision.googleapis.com/v1/images:annotate?key={YOUR_API_KEY}

{
"requests": [
 {
  "features": [
   {
    "type": "LABEL_DETECTION"
   }
  ],
  "image": {
   "source": {
    "gcsImageUri": "gs://vision_test_yutapon/train_1920x1080x061_wd30553a.jpg"
   }
  }
 }
]
}
```

応答
```
200 null

- Show headers -

{
 "responses": [
  {
   "labelAnnotations": [
    {
     "mid": "/m/07bsy",
     "description": "transport",
     "score": 0.97909647
    },
    {
     "mid": "/m/07jdr",
     "description": "train",
     "score": 0.97592318
    },
    {
     "mid": "/m/07yv9",
     "description": "vehicle",
     "score": 0.9274289
    },
    {
     "mid": "/m/01g5v",
     "description": "blue",
     "score": 0.92238986
    },
    {
     "mid": "/m/06d_3",
     "description": "rail transport",
     "score": 0.89261347
    }
   ]
  }
 ]
}
```
この例では電車（北斗星）の画像を使いましたが、descriptionを見るとtransport, train, vehicle, blue, rail transportと、乗り物、電車と認識できていることがわかります。
blueが入っているのは今は亡きBlue Trainの写真だからでしょう。
このように、かなり簡単に使えることがわかります。

ご自分で好きな画像をアップロードし、どのように応答が帰ってくるか試してみてください。


注意
Google Cloud Storageにバケットやファイルが残っていると無料期間が過ぎた後に課金されます。
必要がない場合は必ず削除しておきましょう。
