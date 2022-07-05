# This code was made for the Robocup 2022 - Onstage.
# Team MXNSTERS - Mexico.
# Platform trolley bot. Made by Jaasiel Neftali Vazquez Rodriguez


import sensor, image, time
from pyb import LED, UART

# UART 3, and baudrate for the communication Open MV and Arduino
uart = UART(3, 19200)

red_led   = LED(1)
green_led = LED(2)
blue_led  = LED(3)


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must turn this off to prevent image washout...
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
    for code in img.find_qrcodes(): #  repeat the img.find_qrcodes the for until it finds those qrs
        img.draw_rectangle(code.rect(), color = (255, 0, 0))
        qr=code.payload()
        print(qr)   # and if it finds a code it sends a letter by serial to the Arduino.
        if(qr=="FORWARD"):
            green_led.on()
            print("FORWARD")
            uart.write("F")
            time.sleep (3)

        if(qr=="BACK_TO"):
            green_led.on()
            print("BACK_TO")
            uart.write("B")
            time.sleep (3)

        if(qr=="TO_THE_RIGHT"):
            green_led.on()
            print("TO_THE_RIGHT")
            uart.write("R")
            time.sleep (3)

        if(qr=="TO_THE_LEFT"):
            green_led.on()
            print("TO_THE_LEFT")
            uart.write("L")
            time.sleep (3)

        if(qr=="STOP"):
            green_led.on()
            print("STOP")
            uart.write("S")
            time.sleep (3)