#-*-coding:utf-8-*-
#基于mqtt的client程序，可以发送本机的ping百度的时间（时间没有分开，如果需要也可自己分离）
import paho.mqtt.client as mqtt

def mqtt_client_send(topic,payload):
	payload=str(payload)
	client = mqtt.Client()
	client.username_pw_set(username="test", password="test")
	client.connect("mqtt.wangyaomin.com", 1883, 60)
	client.publish(topic, payload , qos=1, retain=False)