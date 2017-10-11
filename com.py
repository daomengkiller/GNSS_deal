import serial
import struct

print(serial.PARITY_ODD, serial.STOPBITS_TWO, serial.SEVENBITS, )
ser = serial.Serial(  # 下面这些参数根据情况修改
    port='COM14',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=7
)

# def deal_string(string):
#     s = '000000'
#     s1, s2 = string.split('.')
#     s1=s[0:6 - len(s1) ]+s1
#     s2=s2+'0'
#     d1=s1[0:2];d2=s1[2:4];d3=s1[4:6]
#     d4=s2[0:2];d5=s2[2:4];d6=s2[4:6];d7=s2[6:8]
#     return s1, s2,d1,d2,d3,d4,d5,d6,d7
while 1:
    # data = str(ser.readline(), encoding="utf-8")
    data1 = ser.read(87)

    # data = "$GPGGA,031850.00,2813.6484749,N,11305.4159409,E,4,20,0.7,78.371,M,-15.56,M,01,0000*4C"
    # d = data.split(',')
    print(data1)

    # s1 = d[2]
    # s2 = d[4]
    # print(deal_string(s1))
    # print(type(s1), len(s1), type(s2), len(s2))
