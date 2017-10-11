import serial
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from math import radians, cos, sin, asin, sqrt, atan, atan2, atanh


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    if lon1 == lon2:
        if lat2 == lat1:
            du = 0.0
        else:
            if lat2 > lat1:
                du = 90
            else:
                du = 270
    else:
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        # print(dlon,dlat)
        if dlon > 0:
            du = atan(dlat / dlon) / 3.1415926 * 180
        else:
            if dlat > 0:
                print()
                du = 180 + atan(dlat / dlon) / 3.1415926 * 180
            else:
                du = -180 + atan(dlat / dlon) / 3.1415926 * 180

    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000, du


def set_plot():
    plt.ion()
    plt.grid(True)
    plt.axis("equal")
    plt.xlim(28.22747450, 28.22747499)
    plt.ylim(113.09026550, 113.09026599)
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.8f'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.8f'))


def get_gnss():
    ser = serial.Serial(  # 下面这些参数根据情况修改
        port='COM14',
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=7
    )
    data = str(ser.read(87), encoding="utf-8")
    d = data.split(',')
    if int(d[6]) >= 4:
        s1 = d[2]
        s2 = d[4]
    else:
        s1 = str(2813.6484749)
        s2 = str(11305.4159409)

    return s1, s2  # s1为纬度，s2为经度，未处理的数据


def deal_data(string):
    s = '000000'
    string_data = float(string) / 100
    string_du = int(string_data)
    string_miao = float(string) - string_du * 100
    string_xiao = string_miao / 60
    data = string_du + string_xiao
    return data


def set_target():
    N = [0, 0, 0, 0]
    E = [0, 0, 0, 0]
    for i in range(4):
        N[i] = 28.22747458 + (-i) * (-i) * 0.00000002
        E[i] = 113.09026568 + (-i) * (-i) * 0.00000002
        # plt.scatter(N[i], E[i], c='b', marker='*')
    plt.plot(N, E, '-ok')

    return N, E


def show_data(x, y):
    plt.scatter(x, y, c='r', marker='.')
    plt.pause(0.001)


def send2can(x1, y1, x2, y2):
    L, D = haversine(x1, y1, x2, y2)
    return L, D


def main():
    set_target()
    set_plot()
    print(set_target())
    #plt.annotate('A', xy=(113.09026568, 28.22747458), xytext=(113.09026568, 28.22747458), \
                #arrowprops=dict(facecolor='black', shrink=0.1))
    j = 1
    num = 100
    X = np.random.normal(0, 3, num)
    Y = np.random.normal(0, 3, num)
    n = 28.22747458 + X * 0.00000001
    e = 113.09026568 + Y * 0.00000001
    while True:
        if j % 100 == 0:
            for t in range(num):
                # N, E=get_gnss()#得到串口数据
                # n=deal_data(N)#浮点型纬度
                # e=deal_data(E)#浮点型经度
                # n = 28.22747458 + X[t] * 0.00000001
                # e = 113.09026568 + Y[t] * 0.00000001
                show_data(n[t], e[t])
                L, D = send2can(e[t], n[t], 113.09026580, 28.22747480)
                print(L, D)
        j = j + 1
        plt.pause(0.01)


if __name__ == '__main__':
    main()
