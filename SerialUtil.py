#! /bin/python

import serial

class SerialUtil:

    def __init__(self):
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=38400,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=None,
            xonxoff=False,
            rtscts=False,
            writeTimeout=None,
            dsrdtr=False,
            interCharTimeout=None
        )

    def setColor(self, red, green, blue):
        '''
        Set color

        @param red int 0 ... 255 for red channel
        @param green int 0 ... 255 for green channel
        @param blue int 0 .. 255 for blue channel
        '''

        # sanity checks
        if red not in range(0, 256): print "ERROR: Color red not in range."
        if green not in range(0, 256): print "ERROR: Color green not in range."
        if blue not in range(0, 256): print "ERROR: Color blue not in range."

        redBase = "C001L"
        greenBase = "C002L"
        blueBase = "C000L"

        redString = ""
        if 0 <= red and red < 10: redString = "00" + str(red)
        if 10 <= red and red < 100: redString = "0" + str(red)
        if 100 <= red and red <= 255: redString = str(red)

        greenString = ""
        if 0 <= green and green < 10: greenString = "00" + str(green)
        if 10 <= green and green < 100: greenString = "0" + str(green)
        if 100 <= green and green <= 255: greenString = str(green)

        blueString = ""
        if 0 <= blue and blue < 10: blueString = "00" + str(blue)
        if 10 <= blue and blue < 100: blueString = "0" + str(blue)
        if 100 <= blue and blue <= 255: blueString = str(blue)

        r = redBase + redString
        g = greenBase + greenString
        b = blueBase + blueString

        print r, g ,b

        self.ser.write(b)
        self.ser.write(r)
        self.ser.write(g)