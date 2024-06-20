#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:01:25 2023

@author: davidpine
"""


    def displacement(self, time):
        g = self.meta["gravity_acceleration_si"]  # [m/s^2]
        arg1 = g * time / self.vt
        arg2 = np.cosh(arg1) + (self.v0 / self.vt) * np.sinh(arg1)
        return (self.vt**2 / g) * np.log(arg2)
