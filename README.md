# IOT-Car
⚫Oerview

  You can control the car with your eyes
  
⚫What u need

  Raspberry Pi 4 x1
  
  l298 motor controller x1
  
  Battery case x2
 
  1.5V AA Battery x8
  
  Raspberry pi car x1
  
  Rasberry Pi NOIR/w CS x1
  
⚫Video Streaming

  Follow the instruction from this website https://www.instructables.com/Video-Streaming-Web-Server/
  
⚫Circuit Design

   ![image](https://github.com/AirusIan/IOT-Tkinter-Button-Car/blob/main/IOT.png)
   
⚫tkinter.py

  import tkinter as tk
  import RPi.GPIO as GPIO
   建立主視窗和 Frame（把元件變成群組的容器）
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
      
      GPIO.output(pin_right_f, GPIO.LOW)
     
      GPIO.output(pin_right_b, GPIO.HIGH)
      
      GPIO.output(pin_left_f, GPIO.HIGH)
      
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


window.mainloop()

⚫Final Project

![image](https://github.com/AirusIan/IOT-Tkinter-Button-Car/blob/main/S__14319686.jpg)

