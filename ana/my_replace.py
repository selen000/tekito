# 文字列とか前処理用
import pandas as pd


def kanzi_to_number(word):
    """
    漢字文字列を、数字に変換する
    """
    word = word.translate(str.maketrans({'零': 'O', '一': '1', '二': '2',
                                         '三': '3', '四': '4', '五': '5',
                                         '六': '6', '七': '7', '八': '8',
                                         '九': '9', '十': '10'}))
    return word


def number_to_kanzi(word):
    """
    数字文字列を漢字に変換する
    """
    word = word.translate(str.maketrans({'0': '零', '1': '一', '2': '二',
                                         '3': '三', '4': '四', '5': '五',
                                         '6': '六', '7': '七', '8': '八',
                                         '9': '九', '10': '十'}))

    return word


def osaka_replace(word):
    """
    方便を置換する
    とりあえず辞書渡してfor文で1文字ずつ置換する感じで
    """

    # Todo 外部ファイルで管理できるようにする
    osakadict = {"おもろい": "面白い",
                 "ほんま": "本当に",
                 "ちゃう": "違う",
                 "せや": "そうだ",
                 "はよ": "早く",
                 "かまへん": "構わない",
                 "突き出し": "お通し"}

    for k, v in osakadict.items():
        word = word.replace(k, v)
    return word


def remove_kigou(word):
    """
    句読点の除去処理
    """
    punctuations = '''!()-[]{};:'",、！？<>./?@#$%^&*_~'''
    no_punct = ""
    for char in word:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


if __name__ == '__main__':
    osaka_df = pd.read_csv("osaka_dict.csv", encoding="sjis")
    print(osaka_df)

    # word = osaka_replace("ほんま面白いわ,せやはよ行こう")
    word = remove_kigou("ほんま面白いわ,せ、やはよ行こう")
    print(word)
