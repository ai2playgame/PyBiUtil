import argparse
import binascii
import glob


def main():
    # コマンドライン引数処理
    parser = argparse.ArgumentParser()
    parser.add_argument('searchDir', help='<検索対象のディレクトリ>')
    parser.add_argument('searchHex', help='<検索キーワード(16進数)>')

    args = parser.parse_args()

    # 16進数文字列をバイナリ列に変換する
    searchWordBin = binascii.unhexlify(args.searchHex)

    # 指定したフォルダ以下のファイルを取得
    files = glob.glob(f'{args.searchDir}/*')

    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
            if searchWordBin in content:
                print(f"hit!: {file}")


if __name__ == '__main__':
    main()
