from gps import GPS
gps=GPS(rx=8,tx=7,en=2,baudrate=9600,bus=1,time_zone=8,stop=0)#RX,TX,使能引脚，波特率，总线编号，时区，模块停止工作时使能引脚值
gps.on()                                                       #你可以在GPS模块的VCC中放置PMOS开关，关断时电流低至1ua
while 1:
    if gps.mode==0:
        print('gps is off')
    else:
        print(
            gps.getinf(),
            gps.getlongitude(),
            gps.getlatitude(),
            gps.getplace(),
            gps.getspeed())
