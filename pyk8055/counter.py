#!/usr/bin/python3

import pyk8055
import time

def main():
    k = pyk8055.k8055(0)
    k.ResetCounter(1)
    k.ResetCounter(2)
    old_counter = -1
    new_counter = 0
    while True:
        new_counter = k.ReadCounter(1) - k.ReadCounter(2)
        # print("Digital counter 0" + str(new_counter))
        if old_counter < 0:
           old_counter = new_counter

        if new_counter != old_counter:
            print("Digital counter 1" + str(new_counter) )
            k.WriteAllDigital(new_counter)
            k.OutputAnalogChannel(1, new_counter)
            k.OutputAnalogChannel(2, 255 - new_counter)
            old_counter = new_counter
        time.sleep(0.2)

main()
