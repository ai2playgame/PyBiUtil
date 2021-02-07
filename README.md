# PyBiUtil

Pythonで自作したバイナリファイル操作の便利ツール類

## 構成

### findHex.py

```sh
python findHex.py <検索対象のディレクトリ> <検索したい16進数>
```

検索対象のディレクトリ内のバイナリファイル中に、16進数で表現したバイナリ列が存在するか調べ、その結果を標準出力する。

### makebinary.py

```sh
python makebinary.py
```

`./testdata`以下にテスト用のバイナリファイルを出力する