#-*-coding:utf-8-*-

# 导入 paho-mqtt 的 Client：
import paho.mqtt.client as mqtt
import time
unacked_sub = [] #未获得服务器响应的订阅消息 id 列表

# 用于响应服务器端 CONNACK 的 callback，如果连接正常建立，rc 值为 0
def on_connect(client, userdata, flags, rc):
    print("Connection returned with result code:" + str(rc))


# 用于响应服务器端 PUBLISH 消息的 callback，打印消息主题和内容
def on_message(client, userdata, msg):
    print("Received message, topic:" + msg.topic + "payload:" + str(msg.payload))

# 在连接断开时的 callback，打印 result code
def on_disconnect(client, userdata, rc):
    print("Disconnection returned result:"+ str(rc))

# 在订阅获得服务器响应后，从为响应列表中删除该消息 id
def on_subscribe(client, userdata, mid, granted_qos):
    unacked_sub.remove(mid)


# 构造一个 Client 实例
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect= on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe

# 连接 broker
# connect() 函数是阻塞的，在连接成功或失败后返回。如果想使用异步非阻塞方式，可以使用 connect_async() 函数。



def send():
    try:
        while 1:
            client.connect("192.168.0.2", 1883, 60)
            client.loop_start()

            client.publish("/cmd_rec_tem", payload = b"received")

            
            client.loop_stop()
            client.disconnect()
            time.sleep(60) #等待消息处理结束
    except Exception as e:
        print(e)
        send()
        

send()