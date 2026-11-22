# this app reads data from modbus tcp and transmits it to mqtt broker
import os
import pprint
import time
from pyModbusTCP.client import ModbusClient
import paho.mqtt.client as mqtt
from solax import InputRegistersMap, HoldingRegistersMap, proccessingMap
import json
# from solax import testRegisterMap as InputRegistersMap


# Set ENABLE_LOGS=true to print decoded readings (fills docker logs if left on)
ENABLE_LOGS = os.environ.get("ENABLE_LOGS", "false").lower() in ("1", "true", "yes")

def env_int(name, default):
    value = os.environ.get(name, "").strip()
    if not value:
        return default
    try:
        return int(value, 0)
    except ValueError:
        raise SystemExit(f"{name} must be a whole number, got {value!r}")


# Every setting below can be overridden with an environment variable of the same name.
# Modbus TCP host IP or DNS name
MODBUS_HOST = os.environ.get("MODBUS_HOST") or "192.168.88.242"
# MODBUS_HOST = "192.168.8.176"
# Modbus TCP port
MODBUS_PORT = env_int("MODBUS_PORT", 502)
# Modbus TCP slave unit ID
MODBUS_UNIT_ID = env_int("MODBUS_UNIT_ID", 1)
# Modbus TCP register address
MODBUS_REG_ADDR = env_int("MODBUS_REG_ADDR", 0)
# Modbus TCP register number
MODBUS_REG_NB = env_int("MODBUS_REG_NB", 300)
# Modbus Batch size
MODBUS_BATCH_SIZE = env_int("MODBUS_BATCH_SIZE", 100)
# MQTT broker host
MQTT_HOST = os.environ.get("MQTT_HOST") or "192.168.8.200"
# MQTT broker port
MQTT_PORT = env_int("MQTT_PORT", 1883)
# MQTT topic
MQTT_TOPIC = os.environ.get("MQTT_TOPIC") or "solax/metrics"
# Seconds to wait between readings
POLL_INTERVAL = env_int("POLL_INTERVAL", 10)

pp = pprint.PrettyPrinter(width=41, compact=True)

# create modbus client
try:
    c = ModbusClient(MODBUS_HOST, MODBUS_PORT, unit_id=MODBUS_UNIT_ID, auto_open=True, auto_close=True, debug=False)
except ValueError:
    print("Error with host or port params")

# create mqtt client
mqttc = mqtt.Client()

def read_input_registers():
    num=MODBUS_REG_NB
    start=MODBUS_REG_ADDR
    regs = []
    while num > 0:
        if num > MODBUS_BATCH_SIZE:
            inputlist = c.read_input_registers(start, MODBUS_BATCH_SIZE)
            if inputlist is not None:
                regs = regs + inputlist
                num -= MODBUS_BATCH_SIZE
                start += MODBUS_BATCH_SIZE
            else :
                num = 0
        else:
            regs = regs + c.read_input_registers(start, num)
            num = 0

    # convert to json
    json = {}
    for i in range(len(regs)):
        json[i] = regs[i]

    return json

def read_holding_registers():
    num=MODBUS_REG_NB
    start=MODBUS_REG_ADDR
    regs = []
    while num > 0:
        if num > MODBUS_BATCH_SIZE:
            inputlist = c.read_holding_registers(start, MODBUS_BATCH_SIZE)
            if inputlist is not None:
                regs = regs + inputlist
                num -= MODBUS_BATCH_SIZE
                start += MODBUS_BATCH_SIZE
            else :
                num = 0
        else:
            regs = regs + c.read_holding_registers(start, num)
            num = 0

    # convert to json
    json = {}
    for i in range(len(regs)):
        json[i] = regs[i]

    return json

def get_register_value(regs, element):
    value = regs[int(element['address'],0)]
    if element['length'] == 1:
        if element['type'] == 'int16' and value > 32767:
            value = value - 65536
    
    elif element['length'] == 2:
        value = regs[int(element['address'],0)] + regs[int(element['address'],0)+1] * 65536
        if element['type'] == 'int32' and value > 2147483647:
            value = value - 4294967296

    value = value * float(element['scale'])

    return round(value,2)

def process_results(results, proccessingMap):
    for element in proccessingMap:
        if element['type'] == 'sum':
            value = 0
            for reg in element['registers']:
                value += results[reg]
            results[element['name']] = value
        elif element['type'] == 'diff':
            value = results[element['registers'][0]] - results[element['registers'][1]]
            results[element['name']] = value
        elif element['type'] == 'div':
            value = results[element['registers'][0]] / results[element['registers'][1]]
            results[element['name']] = value
        elif element['type'] == 'mul':
            value = results[element['registers'][0]] * results[element['registers'][1]]
            results[element['name']] = value
    
    return results

def decode_registers(regs, input_registers_map):
    results = {}
    for element in input_registers_map:
        if int(element['address'],0) in regs:
            value = get_register_value(regs, element)
            results[element['name']] = value
    if ENABLE_LOGS:
        pp.pprint(results)
    return process_results(results, proccessingMap) 

def write_holding_register(register, value):
    c.write_single_register(register, value)
    

# result = write_holding_register(0x0088, 25)
# print(result)
def main():
    # connect to mqtt broker
    mqttc.connect(MQTT_HOST, MQTT_PORT, 60)
# infinite loop
    while True:
        regs = read_input_registers()
        results = decode_registers(regs, InputRegistersMap)
        
        # publish to mqtt broker
        mqttc.publish(MQTT_TOPIC, json.dumps(results))

        # regs = read_holding_registers()
        # results = decode_registers(regs, HoldingRegistersMap)
        # pp.pprint(results)

        # print("")


        # wait before the next reading
        time.sleep(POLL_INTERVAL)

    c.close()

# run the app
if __name__ == "__main__":
    main()