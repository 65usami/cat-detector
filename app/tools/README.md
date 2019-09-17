# Pre-Trained Model(学習済みモデル)作成

## Summary

`app/apps/predict.py` で使用する学習済みモデル作成手順

## Requirements

python 3.6.7

## Usage

- データのダウンロード

Flickrを利用して学習対象のデータを収集

```
$ python download_images.py 'NAME'

# python download_images.py 'cat'
```

- 学習データの作成

学習対象のデータから学習データを作成

`img_classess.py` の配列に __データのダウンロード__ で指定した __NAME__ を追加する。

```
$ python generate_train_data.py 'NAME'

# python generate_train_data.py 'cat'
```

- 学習済みモデルデータ作成

```
$ python generate_model.py
```

`cat_cnn.h5` のモデルデータが出力されます。

