import tkinter as tk
import RPi.GPIO as GPIO
# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
pin_right_f = 31
pin_right_b = 33
pin_left_f = 35
pin_left_b = 37
GPIO.setmode(GPIO.BOARD)
gpio_pin = [pin_right_f, pin_right_b, pin_left_f, pin_left_b]
for i in gpio_pin:
    GPIO.setup(i, GPIO.OUT)

def forward():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.HIGH)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.LOW)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.HIGH)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.LOW)
    print("forward!")

def backward():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.LOW)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.HIGH)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.LOW)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.HIGH)
    print("backward!")

def left():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.HIGH)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.LOW)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.LOW)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.HIGH)
    print("left!")

def right():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.LOW)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.HIGH)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.HIGH)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.LOW)
    print("right!")

def stop():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.LOW)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.LOW)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.LOW)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.LOW)
    print("stop!")

def closeGPIO(gpio_pin):
    for i in gpio_pin:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()




while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()

    if gaze.is_right():
        right()
    elif gaze.is_left():
        left()
    elif gaze.is_center():
        forward()
    else
        stop()




# 運行主程式

window.mainloop()
