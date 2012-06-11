#! /bin/python

class ColorUtil:
    def __init__ (self):
        pass

    def getColorByName (self, colorString):

        r = 0
        g = 0
        b = 0

        if colorString == "navy":
            r = 0
            g = 0
            b = 128

        if colorString == "peru":
            r = 205
            g = 133
            b = 63

        if colorString == "gray":
            r = 190
            g = 190
            b = 190

        if colorString == "green":
            r = 0
            g = 205
            b = 0

        if colorString == "maroon":
            r = 176
            g = 48
            b = 96

        if colorString == "wheat":
            r = 245
            g = 222
            b = 179

        if colorString == "gold":
            r = 255
            g = 86
            b = 0

        if r == 0 and g == 0 and b == 0: print "ERROR: No definition for color %s found." % colorString

        print "setColor(%s, %s, %s)" % (str(r), str(g), str(b))
        return r, g, b