# -*- coding: utf-8 -*-

import serial_local
import mqtt_client
import json
import threading



threading.Thread(target=mqtt_client.mqtt_sub("serlist")).start()
