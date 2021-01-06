# IOT-Tkinter-Button-Car
⚫Oerview

  You can control the car with Tkinter Button
  
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
  
  # 建立主視窗和 Frame（把元件變成群組的容器）
  
  window = tk.Tk()
  
  top_frame = tk.Frame(window)

  # 將元件分為 top/bottom 兩群並加入主視窗
  
  top_frame.pack()
  
  bottom_frame = tk.Frame(window)
  
  bottom_frame.pack(side=tk.BOTTOM)


  pin_right_f = 31
  
  pin_right_b = 33
  
  pin_left_f = 35
  
  pin_left_b = 37
  
  GPIO.setmode(GPIO.BOARD)
  
  gpio_pin = [pin_right_f, pin_right_b, pin_left_f, pin_left_b]
  for i in gpio_pin:
  
      GPIO.setup(i, GPIO.OUT)

  def forward():
  
      
      
      GPIO.output(pin_right_f, GPIO.HIGH)
      
      
      
      GPIO.output(pin_right_b, GPIO.LOW)
      
     
      
      GPIO.output(pin_left_f, GPIO.HIGH)
      
      
      
      GPIO.output(pin_left_b, GPIO.LOW)
      
      print("forward!")

  def backward():
  
    
     
     GPIO.output(pin_right_f, GPIO.LOW)
     
    
     
     GPIO.output(pin_right_b, GPIO.HIGH)
     
  
     
     GPIO.output(pin_left_f, GPIO.LOW)
     
    
     
     GPIO.output(pin_left_b, GPIO.HIGH)
     
     print("backward!")

  def left():
  
     
     
     GPIO.output(pin_right_f, GPIO.HIGH)
     
    
     
     GPIO.output(pin_right_b, GPIO.LOW)
     
    
     
     GPIO.output(pin_left_f, GPIO.LOW)
     
     
    
     GPIO.output(pin_left_b, GPIO.HIGH)
     
     print("left!")

  def right():
  
      
      
      GPIO.output(pin_right_f, GPIO.LOW)
      
      
      
     GPIO.output(pin_right_b, GPIO.HIGH)
     
      
      
      GPIO.output(pin_left_f, GPIO.HIGH)
      
     
      
      GPIO.output(pin_left_b, GPIO.LOW)
      
      print("right!")

def stop():

    
    
    GPIO.output(pin_right_f, GPIO.LOW)
    
    
    
    GPIO.output(pin_right_b, GPIO.LOW)
    
   
    
    GPIO.output(pin_left_f, GPIO.LOW)
    
    
    
    GPIO.output(pin_left_b, GPIO.LOW)
    
    print("stop!")

  def closeGPIO(gpio_pin):
  
      for i in gpio_pin:
      
          GPIO.output(i, GPIO.LOW)
          
      GPIO.cleanup()

  left_button = tk.Button(top_frame, text='GoLeft', fg='red',command= right)
  
  
  left_button.pack(side=tk.LEFT)

  middle_button = tk.Button(top_frame, text='Forward', fg='green',command=forward)
  
  middle_button.pack(side=tk.LEFT)

  right_button = tk.Button(top_frame, text='GoRight', fg='blue',command=left)
  
  right_button.pack(side=tk.LEFT)

  stop_button = tk.Button(top_frame, text='Stop', fg='yellow',command=stop)
  
  stop_button.pack(side=tk.BOTTOM)

  
  bottom_button = tk.Button(bottom_frame, text='Back', fg='black', command=backward)
  
  
  bottom_button.pack(side=tk.TOP)


  window.mainloop()
 
⚫Final Project

![image](https://github.com/AirusIan/IOT-Tkinter-Button-Car/blob/main/S__14319686.jpg)

⚫Demo
https://github.com/AirusIan/IOT-Tkinter-Button-Car/blob/main/631602801.347430.mp4
  
