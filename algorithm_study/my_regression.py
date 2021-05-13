# 回帰
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston

def _preprocess(dataset):
    x = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['target'])
    return x, y

def _train():
    pass

def _predict():
    pass

def main(df):

    # 前処理
    x, y = _preprocess(data_set)

    # 説明変数の数を取得する
    coef_num = x.shape[1]
    decimal_p = 2 # 小数点以下n桁

    ridge = Ridge().fit(x,y)
    print(ridge.coef_.round(decimal_p))

if __name__ == '__main__':
    data_set = load_boston()
    # 練習用のデータ取得
    main(data_set)