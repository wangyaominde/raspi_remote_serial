import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.wangyaomin.com", 1883, 60)
client.publish("test", "hello world")
client.disconnect()