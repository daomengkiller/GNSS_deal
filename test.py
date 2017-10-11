import struct
import socket
send_format='20B'
device=0#无符号1字节B
CAN_ID_H=20#无符号2字节H
CAN_ID_L=1#无符号2字节H
default_H=0#无符号2字节H
default_L=0
length=8#无符号1字节B
CAN_DATA1=1#无符号8字节Q
CAN_DATA2=1
CAN_DATA3=1
CAN_DATA4=1
CAN_DATA5=1
CAN_DATA6=1
CAN_DATA7=1
CAN_DATA8=1
standard_frame=1#无符号1字节B
remote_frame=0#无符号1字节B
str=struct.pack(send_format,device,CAN_ID_L,CAN_ID_H
                ,default_L,default_H,length,
                CAN_DATA1,CAN_DATA2,CAN_DATA3,
                CAN_DATA4,CAN_DATA5,CAN_DATA6,
                CAN_DATA7,CAN_DATA8,
                standard_frame,remote_frame,0,0,0,0)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.150',6020))
while 1:
    print('--')
    s.send(str)


print(len(str))
print(str)
