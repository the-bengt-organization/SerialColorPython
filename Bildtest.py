#! /bin/python

import time

import ColorUtil
import SerialUtil

su = SerialUtil.SerialUtil()
cu = ColorUtil.ColorUtil()

color = cu.getColorByName("gold")
time.sleep(3)
color = cu.getColorByName("navy")
su.setColor(color[0], color[1], color[2])
