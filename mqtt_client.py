# -*- coding: utf-8 -*-
"""使用mqtt搭建远程透传"""
"""
    mqtt服务器：mqtt.wangyaomin.com
    日期：2021.8.1
    描述：使用mqtt协议进行透传
    作者：wangyaomin
    邮箱：wangyaominde@live.cn

"""

import paho.mqtt.client as mqtt
import time

def mqtt_sub():
    """mqtt订阅"""
    client = mqtt.Client()
    client.connect("mqtt.wangyaomin.com", 1883)
    client.subscribe("/test/test_topic")
    client.loop_start()
    while True:
        time.sleep(1)
    client.loop_stop()
    client.disconnect()

def mqtt_send(topic,message):
    """mqtt发布"""
    client = mqtt.Client()
    client.connect("mqtt.wangyaomin.com", 1883)
    client.publish(topic,message)
    client.loop_start()
    client.loop_stop()
    client.disconnect()




