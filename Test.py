#! /bin/python

import serial

import ColorUtil
import SerialUtil

try:
    su = SerialUtil.SerialUtil()
    su.setColor("228", "128", "64")
except serial.serialutil.SerialException:
    print "Initializing SerialUtil failed. Is /dev/ttyUSB0 connected?"

cu = ColorUtil.ColorUtil()
gold = cu.getColorByName("gold")
print "Gold is rgb%s." % (str(gold))
navy = cu.getColorByName("navy")
print "Navy is rgb%s." % (str(navy))