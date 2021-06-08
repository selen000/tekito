# 文字列とか前処理用
import pandas as pd
import MeCab

wakati=MeCab.Tagger("-Owakati")



class translate_kansai():

    def kanzi_to_number(self, word):
        """
        漢字文字列を、数字に変換する
        """
        word = word.translate(str.maketrans({'零': 'O', '一': '1', '二': '2',
                                             '三': '3', '四': '4', '五': '5',
                                             '六': '6', '七': '7', '八': '8',
                                             '九': '9', '十': '10'}))
        return word


    def number_to_kanzi(self, word):
        """
        数字文字列を漢字に変換する
        """
        word = word.translate(str.maketrans({'0': '零', '1': '一', '2': '二',
                                             '3': '三', '4': '四', '5': '五',
                                             '6': '六', '7': '七', '8': '八',
                                             '9': '九', '10': '十'}))

        return word


    def osaka_replace(self, word, df, base_word_col):
        """
        word : 変換したい文字列
        df : 変換用対応データフレーム
        base_word_col : 変換前の方便のカラム名

        方便を置換する
        """
        for k, v in zip(df[base_word_col], df["標準語"]):
            word = word.replace(k, v)
        return word


    def remove_kigou(self, word):
        """
        句読点の除去処理
        """
        punctuations = '''!()-[]{};:'",、！？<>./?@#$%^&*_~'''
        no_punct = ""
        for char in word:
            if char not in punctuations:
                no_punct = no_punct + char
        return no_punct


    def wakatigaki(self, word):
        word_list = wakati.parse(word).split()
        return word_list


if __name__ == '__main__':
    osaka_df = pd.read_csv("osaka_dict.csv", encoding="sjis")
    origin_word_col = "関西弁"
    replace_word_col = "標準語"

    a = translate_kansai()

    word = "ほんまおもろいわ,せやはよ行こう"

    word = a.osaka_replace(word, osaka_df, origin_word_col)
    word = a.wakatigaki(word)
    print(word)
