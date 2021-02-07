import argparse
import os


def bin_cut(filePath, start, end):
    partialSize = end - start + 1
    with open(filePath, "rb") as f:
        f.seek(start)
        data = f.read(partialSize)

        return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath', help='<一部を切り出したいバイナリファイルのパス>')
    parser.add_argument('start', help='<カットする開始アドレス>')
    parser.add_argument('end', help='<カットする終了アドレス>')

    args = parser.parse_args()

    partialData = bin_cut(args.filePath, int(args.start), int(args.end))

    inputFilePath = os.path.dirname(args.filePath)
    inputFileName = os.path.splitext(os.path.basename(args.filePath))[0]
    inputFileExt = os.path.splitext(os.path.basename(args.filePath))[1]

    outputFilePath = f'{inputFilePath}/{inputFileName}_cutted{inputFileExt}'

    with open(outputFilePath, 'wb') as f:
        f.write(partialData)


if __name__ == '__main__':
    main()
