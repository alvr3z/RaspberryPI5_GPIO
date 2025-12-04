from smbus2 import SMBus
import RPLCD.i2c as RP

# Default address 2x16 LCD
lcd_address = 0x27
lcd = RP.CharLCD('PCF8574', lcd_address)

lcd.write_string('Hello, World')
lcd.cursor_pos = (1,5)
lcd.write_string('Second Line')
