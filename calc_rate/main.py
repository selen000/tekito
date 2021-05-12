# ガチャの確率計算様モジュール

def calc_rate(proba, try_num):
    print("当たりの確率:", proba)
    print("試行回数:", try_num)
    print("期待値:", proba * try_num)

def main():

    # 引数として数値を受け取る
    # 最終的にはtkinterかなんかで記載する

    # 当たりの生起確率
    proba = 0.1

    # 試行回数
    try_num = 5

    calc_rate(proba, try_num)


if __name__ == '__main__':
    main()

