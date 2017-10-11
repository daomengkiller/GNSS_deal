import struct
import socket


def deal_string(string):
    s = '000000'
    string_data = float(string) / 100
    string_du = int(string_data)
    string_miao = float(string) - string_du * 100
    string_xiao = string_miao / 60
    string_xiao_string = str(string_xiao)
    print(string_du, string_miao, type(string_xiao_string))
    s1, s2 = string.split('.')
    s1 = s[0:6 - len(s1)] + s1
    s3, s4 = string_xiao_string.split('.')
    print(s3, s4)

    s2 = s2 + '0'

    d1 = s1[0:2]
    d2 = s1[2:4]
    d3 = s4[0:2]
    d4 = s4[2:4]
    d5 = s4[4:6]
    d6 = s4[6:8]
    d7=s4[8:10]
    d8=s4[10:12]
    return s1, s2, d1, d2, d3, d4, d5, d6, d7,d8


def get_data():
    data = "$GPGGA,031850.00,2813.6484749,N,11305.4159409,E,4,20,0.7,78.371,M,-15.56,M,01,0000*4C"
    d = data.split(',')
    s1 = d[2]
    s2 = d[4]
    return s1, s2


def send_can_N():
    my_N, my_E = get_data()
    my_data = deal_string(my_N)
    print(my_data, my_data[4], type(my_data[4]))
    send_format = '20B'
    device = 0  # 无符号1字节B
    CAN_ID_H = 20  # 无符号2字节H
    CAN_ID_L = 1  # 无符号2字节H
    default_H = 0  # 无符号2字节H
    default_L = 0
    length = 8  # 无符号1字节B
    CAN_DATA1 = int(my_data[2])  # 无符号8字节Q
    CAN_DATA2 = int(my_data[3])
    CAN_DATA3 = int(my_data[4])
    CAN_DATA4 = int(my_data[5])
    CAN_DATA5 = int(my_data[6])
    CAN_DATA6 = int(my_data[7])
    CAN_DATA7 = int(my_data[8])
    CAN_DATA8 = int(my_data[9])
    standard_frame = 1  # 无符号1字节B
    remote_frame = 0  # 无符号1字节B
    str = struct.pack(send_format, device, CAN_ID_L, CAN_ID_H
                      , default_L, default_H, length,
                      CAN_DATA1, CAN_DATA2, CAN_DATA3,
                      CAN_DATA4, CAN_DATA5, CAN_DATA6,
                      CAN_DATA7, CAN_DATA8,
                      standard_frame, remote_frame, 0, 0, 0, 0)
    return str


def send_can_E():
    my_N, my_E = get_data()
    send_format = '20B'
    device = 0  # 无符号1字节B
    CAN_ID_H = 20  # 无符号2字节H
    CAN_ID_L = 1  # 无符号2字节H
    default_H = 0  # 无符号2字节H
    default_L = 0
    length = 8  # 无符号1字节B
    CAN_DATA1 = 1  # 无符号8字节Q
    CAN_DATA2 = 28
    CAN_DATA3 = 13
    CAN_DATA4 = 1
    CAN_DATA5 = 1
    CAN_DATA6 = 1
    CAN_DATA7 = 1
    CAN_DATA8 = 1
    standard_frame = 1  # 无符号1字节B
    remote_frame = 0  # 无符号1字节B
    str = struct.pack(send_format, device, CAN_ID_L, CAN_ID_H
                      , default_L, default_H, length,
                      CAN_DATA1, CAN_DATA2, CAN_DATA3,
                      CAN_DATA4, CAN_DATA5, CAN_DATA6,
                      CAN_DATA7, CAN_DATA8,
                      standard_frame, remote_frame, 0, 0, 0, 0)
    return str


print(struct.unpack('20B', send_can_N()))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.150', 6020))
while 1:
    print('--')
    s.send(send_can_N())

print(len(str))
print(str)

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.0.150',6020))
# while 1:
#     print('--')
#     s.send(send_can())
