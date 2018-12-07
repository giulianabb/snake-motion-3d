#!/usr/bin/python
import smbus
import math
from time import sleep

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def read_byte(address, reg):
    return bus.read_byte_data(address, reg)


def read_word(address, reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(address, reg):
    val = read_word(address, reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def dist(a,b):
    return math.sqrt((a*a)+(b*b))


def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)


def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def write_byte(address, adr, value):
    bus.write_byte_data(address, adr, value)

bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address_gyro = 0x68       # via i2cdetect
address_mag = 0x1e

scale = 0.92
x_offset = -10
y_offset = 10

# Aktivieren, um das Modul ansprechen zu koennen
write_byte(address_gyro, power_mgmt_1, 0)
write_byte(address_mag, 0, 0b01110000) # Set to 8 samples @ 15Hz
write_byte(address_mag, 1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
write_byte(address_mag, 2, 0b00000000) # Continuous sampling

while (True):

    # gyro_xout = read_word_2c(address_gyro, 0x43)
    # gyro_yout = read_word_2c(address_gyro, 0x45)
    # gyro_zout = read_word_2c(address_gyro, 0x47)

    # print( "gyro_xout: ", ("%5d" % gyro_xout), " scaled: ", (gyro_xout / 131))
    # print( "gyro_yout: ", ("%5d" % gyro_yout), " scaled: ", (gyro_yout / 131))
    # print( "gyro_zout: ", ("%5d" % gyro_zout), " scaled: ", (gyro_zout / 131))

    accel_xout = read_word_2c(address_gyro, 0x3b)
    accel_yout = read_word_2c(address_gyro, 0x3d)
    accel_zout = read_word_2c(address_gyro, 0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    # print( "accel_xout: ", ("%6d" % accel_xout), " scaled: ", accel_xout_scaled)
    # print( "accel_yout: ", ("%6d" % accel_yout), " scaled: ", accel_yout_scaled)
    # print( "accel_zout: ", ("%6d" % accel_zout), " scaled: ", accel_zout_scaled)

    x_out = (read_word_2c(address_mag, 3) - x_offset) * scale
    y_out = (read_word_2c(address_mag, 7) - y_offset) * scale
    z_out = (read_word_2c(address_mag, 5)) * scale

    bearing  = math.atan2(y_out, x_out) 
    if (bearing < 0):
        bearing += 2 * math.pi

    print( "X Rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    print( "Y Rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    print( "Z Rotation: " , math.degrees(bearing))
    sleep(2)
