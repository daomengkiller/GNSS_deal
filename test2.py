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
                du = 180 +atan(dlat / dlon) / 3.1415926 * 180
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


a, b = haversine(113.0902656, 28.2274745, 113.0902657, 28.2274744)
print(a, b)
