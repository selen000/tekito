# ガチャの確率計算様モジュール
import matplotlib.pyplot as plt
import configparser

def calc_rate(proba, try_num):
    """
    試行回数に応じた期待値の算出
    :param proba:
    :param try_num:
    :return:
    """
    print("当たりの確率:", proba)
    print("試行回数:", try_num)
    print("期待値:", proba * try_num)

def plot_rate(proba, set_num):
    """

    ある確率の試行回数に応じたN回目までの正規確率の可視化
    proba : 生起確率、当たりの確率
    set_num : 1回目から何回目までを可視化するか
    :return:
    """
    #ToDo リストでやらないように書き直す、とりあえず
    rate_list = []
    i_list = []
    for i in range(set_num):
        rate = proba * (i)
        i_list.append(i)
        rate_list.append(rate)

    fig, ax = plt.subplots()
    # ヒストグラムを描画する。
    ax.plot(i_list, rate_list)

    # 軸ラベルとタイトル
    ax.set_xlabel("Number of trials")
    ax.set_ylabel("Probability of occurrence")
    ax.set_title("rate")

    plt.show()


def main(proba, try_num, set_num):
    # 期待値計算
    calc_rate(proba, try_num)
    # 可視化
    plot_rate(proba, set_num)

def startup():
    # config取得
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    proba = float(config_ini['CALC_STATE']['Proba'])    # 生起確率
    try_num = int(config_ini['CALC_STATE']['TryNum'])   # 試行回数
    set_num = int(config_ini['CALC_STATE']['SetNum'])   # 回数
    main(proba,try_num,set_num)


if __name__ == '__main__':
    startup()


