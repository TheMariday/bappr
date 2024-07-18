import sys
import time
import threading

sys.path.append("scripts/FC-Mega/examples")
sys.path.append("scripts/rs-power-supply")

import fcmega
import rspowersupply

def spin_fcmega(fc, until):
    while time.time() < until:
        fc.update()

power_supply = rspowersupply.PowerSupply(port="COM5")
mega = fcmega.FCMega()

test_voltages = [7, 10, 14, 17]

test_brightnesses = list(range(0, 255, 16)) + [255]

for voltage in test_voltages:
    power_supply.set_voltage(voltage)
    while power_supply.get_actual_voltage() != voltage:
        pass

    for brightness in test_brightnesses:
        buffer = [[brightness, brightness, brightness] for _ in range(400)]
        mega.set_pixels(buffer)

        t = threading.Thread(target=spin_fcmega, args=(mega, time.time()+2.5))
        # start the thread
        t.start()

        time.sleep(1)
        current = power_supply.get_actual_current()

        print(f"{voltage}, {brightness}, {current}")

        t.join()
