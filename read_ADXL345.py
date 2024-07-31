# -*- coding: utf-8 -*-
import smbus
import time

# Địa chỉ I2C của ADXL345
ADXL345_I2C_ADDR = 0x53

# Các thanh ghi quan trọng của ADXL345
POWER_CTL = 0x2D
DATA_FORMAT = 0x31
DATAX0 = 0x32
DATAX1 = 0x33
DATAY0 = 0x34
DATAY1 = 0x35
DATAZ0 = 0x36
DATAZ1 = 0x37

# Hàm khởi tạo ADXL345
def init_adxl345(bus):
    # Đặt chế độ đo
    bus.write_byte_data(ADXL345_I2C_ADDR, POWER_CTL, 0x08)
    # Đặt định dạng dữ liệu - full resolution, ±16g
    bus.write_byte_data(ADXL345_I2C_ADDR, DATA_FORMAT, 0x0B)

# Hàm đọc dữ liệu từ các thanh ghi
def read_adxl345(bus):
    data = bus.read_i2c_block_data(ADXL345_I2C_ADDR, DATAX0, 6)
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]
    return x, y, z

# Khởi tạo bus I2C
bus = smbus.SMBus(2)#tìm thấy cảm biến trên kênh số 2

# Khởi tạo cảm biến ADXL345
init_adxl345(bus)

while True:
    x, y, z = read_adxl345(bus)
    print(f'X: {x}, Y: {y}, Z: {z}')
    time.sleep(0.5)
