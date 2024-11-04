from gpiozero import LED
from time import sleep

makerobo_LaserPin = LED(17)

def makerobo_setup():
    makerobo_LaserPin.off() # 关闭激光传感器

# 循环函数
def makerobo_loop():
	while True:
		# 继电器打开
		makerobo_LaserPin.on()  # 打开激光模块
		sleep(0.5)              # 延时500ms
		# 继电器关闭
		makerobo_LaserPin.off() # 关闭激光模块
		sleep(0.5)         # 延时500ms

# 释放资源
def makerobo_destroy():
    makerobo_LaserPin.close()

# 程序入口
if __name__ == '__main__':
	makerobo_setup()           #  初始化
	try:
		makerobo_loop()        #  调用循环函数
	except KeyboardInterrupt:  #  当按下Ctrl+C时，将执行destroy()子程序。
		makerobo_destroy()     #  释放资源