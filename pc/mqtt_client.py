import paho.mqtt.client as mqtt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

topic="/raspi/raspi_temperature"
mqtt_server="mqtt.wangyaomin.com"
mqtt_port=1883
mqtt_keepalive=60

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def subscribe_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_server, mqtt_port, mqtt_keepalive)
    client.loop_forever()



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("串口助手")
        Form.resize(640, 400)
        self.subButton = QtWidgets.QPushButton(Form)
        self.subButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.subButton.setObjectName("subButton")
        self.subButton.setText("订阅")
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "串口助手"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())