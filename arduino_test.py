# import serial


# port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
# portList = []
# ports = serial.availablePorts()
# for port in ports:
#     portList.append(port.portName())



import serial

ser=serial.Serial(port='/dev/ttyUSB0',baudrate=115200)

while True:
    rx = ser.readline()
    rxs = str(rx, 'utf-8').strip()
    data = rxs.split(',')
    print (data)








# def onRead():
    # if not serial.canReadLine(): return     # выходим если нечего читать
    # rx = port.readline()
    # rxs = str(rx, 'utf-8').strip()
    # data = rxs.split(',')
    # print(data)
    # if data[0] == '0':
    #     ui.lcdN.display(data[1])
    #     ui.tempB.setValue(int(float(data[3]) * 10))
    #     ui.tempL.setText(data[3])
    #     global listX
    #     global listY
    #     listY = listY[1:]
    #     listY.append(int(data[2]))
    #     ui.graph.clear()
    #     ui.graph.plot(listX, listY)
    #
    # if data[0] == '1':
    #     if data[1] == '0':
    #         ui.circle.setChecked(True)
    #     else:
    #         ui.circle.setChecked(False)
    #
    # if data[0] == '2':
    #     global posX
    #     global posY
    #     posX += int((int(data[1]) - 512) / 100)
    #     posY += int((int(data[2]) - 512) / 100)
    #     ui.circle.setGeometry(posX, posY, 20, 20)

# onRead()

# def onOpen():
#     serial.setPortName(ui.comL.currentText())
#     serial.open(QIODevice.ReadWrite)

#
# def serialSend(data):
#     txs = ""
#     for val in data:
#         txs += str(val)
#         txs += ','
#     txs = txs[:-1]
#     txs += ';'
#     serial.write(txs.encode())
#
#
# def onClose():
#     serial.close()
#
#
# def ledControl(val):
#     if val == 2: val = 1;
#     serialSend([0, val])
#
#
# def fanControl(val):
#     if val == 2: val = 1;
#     serialSend([3, val])
#
#
# def bulbControl(val):
#     if val == 2: val = 1;
#     serialSend([4, val])
#
#
# def servoControl(val):
#     serialSend([2, val])
#
#
#
# serial.readyRead.connect(onRead)
