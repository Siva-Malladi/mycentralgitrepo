#!/bin/env python

import math
import random


def generateotp(size_of_otp):
	alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	otp = ""
	alpnum_size = len(alphanumeric)

	for i in range(size_of_otp):
		otp += alphanumeric[math.floor(random.random() * alpnum_size)] 

	print(otp)


#Adding few lines to check how git is working

if __name__ == "__main__":
	size_of_otp = int(input())
	generateotp(size_of_otp)
