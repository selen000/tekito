# 文字列とか前処理用
import pandas as pd
import MeCab

# 抽象クラス用
from abc import ABCMeta, abstractmethod

wakati=MeCab.Tagger("-Owakati")

# baseとなるクラスを作る
class base_translate(metaclass=ABCMeta):

    def kanzi_to_number(self, word):
        """
        漢字文字列を、数字に変換する
        Todo 問題点　十五　を変換すると105になってしまう。十は後続の文字を見て判断した方が良い
        word : str
        変換対象の文字列
        """
        word = word.translate(str.maketrans({'零': 'O', '一': '1', '二': '2',
                                             '三': '3', '四': '4', '五': '5',
                                             '六': '6', '七': '7', '八': '8',
                                             '九': '9', '十': '10'}))
        return word


    def number_to_kanzi(self, word):
        """
        数字文字列を漢字に変換する
        word : str
        """
        word = word.translate(str.maketrans({'0': '零', '1': '一', '2': '二',
                                             '3': '三', '4': '四', '5': '五',
                                             '6': '六', '7': '七', '8': '八',
                                             '9': '九', '10': '十'}))

        return word

    @abstractmethod
    def dialect_replace(self):
        """
        方便を標準語に修正する
        各翻訳用のクラスで必ず実装する
        """
        pass


class translate_kansai(base_translate):
    def __init__(self):
        self.origin_word_col = "関西弁"
        self.replace_word_col = "標準語"

    def dialect_replace(self, word, df, base_word_col= None):
        """
        word : 変換したい文字列
        df : 変換用対応データフレーム
        base_word_col : 変換前の方便のカラム名

        方便を置換する
        """
        df = df[[self.origin_word_col, self.replace_word_col]]
        df = df.dropna()

        # 塊で処理した方が翻訳ミスが減ると仮定して、辞書の単語の長さでソートする
        df["len_"] = df[self.origin_word_col].apply(lambda x: len(x))
        df = df.sort_values("len_", ascending=False)


        if base_word_col == None:
            base_word_col = self.origin_word_col

        for k, v in zip(df[base_word_col], df[self.replace_word_col]):
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


class translate_hokkaido(base_translate):

    def dialect_replace(self):
        pass

class translate_kogo(base_translate):
    def __init__(self):
        self.origin_word_col = "古語"
        self.replace_word_col = "標準語"

    def dialect_replace(self, word, df, base_word_col= None):
        """
        word : 変換したい文字列
        df : 変換用対応データフレーム
        base_word_col : 変換前の方便のカラム名

        方便を置換する
        """
        df = df[[self.origin_word_col, self.replace_word_col]]
        df = df.dropna()

        # 塊で処理した方が翻訳ミスが減ると仮定して、辞書の単語の長さでソートする
        df["len_"] = df[self.origin_word_col].apply(lambda x: len(x))
        df = df.sort_values("len_", ascending=False)



        if base_word_col == None:
            base_word_col = self.origin_word_col

        for k, v in zip(df[base_word_col], df[self.replace_word_col]):
            word = word.replace(k, v)
        return word




if __name__ == '__main__':
    osaka_df = pd.read_csv("osaka_dict.csv", encoding="sjis")


    #a = translate_kansai()

    #word = "ほんまおもろいわ,せやはよ行こう十五"
    #word = a.kanzi_to_number(word)


    #word = a.dialect_replace(word, osaka_df, base_word_col="関西弁")
    #word = a.wakatigaki(word)

    #a = translate_hokkaido()

    word = "春はあけぼの。やうやうしろくなりゆく山ぎは、すこしあかりて、紫だちたる雲のほそくたなびきたる。夏は夜。\
    月の頃はさらなり、闇もなほ、蛍のおほく飛びちがひたる。また、ただ一つ二つなど、ほのかにうち光りて行くも、をかし。雨など降るも、をかし。\
    秋は夕暮れ。夕日のさして、山の端いと近くなりたるに、烏（からす）の、寝所（ねどころ）へ行くとて、三つ四つ、二つ三つなど、飛び急ぐさへ、あはれなり。\
    まいて、雁（かり）などのつらねたるが、いと小さく見ゆるは、いとをかし。\
    日入りはてて、風の音、虫の音など、はた、言ふべきにあらず。\
    冬はつとめて。雪の降りたるは、言ふべきにもあらず。\
    霜のいと白きも、またさらでも、いと寒きに、火など急ぎおこして、炭持てわたるも、いとつきづきし。\
    昼になりて、ぬるくゆるびもていけば、火桶（ひおけ）の火も、白き灰がちになりて、わろし。"
    a = translate_kogo()

    print(word)
    print("="*40)

    word = a.dialect_replace(word, osaka_df, base_word_col="古語")

    print(word)

