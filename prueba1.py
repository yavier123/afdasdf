#!/usr/bin/env python

from SimpleCV import Image, Camera

cam = Camera()
img = cam.getImage()
img.binarize().save()
img.save("prueba.jpg")
