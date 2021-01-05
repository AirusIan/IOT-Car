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




  # 建立事件處理函式（event handler），透過元件 command 參數存取


  # 以下為 top 群組
  left_button = tk.Button(top_frame, text='GoLeft', fg='red',command= right)
  # 讓系統自動擺放元件，預設為由上而下（靠左）
  left_button.pack(side=tk.LEFT)

  middle_button = tk.Button(top_frame, text='Forward', fg='green',command=forward)
  middle_button.pack(side=tk.LEFT)

  right_button = tk.Button(top_frame, text='GoRight', fg='blue',command=left)
  right_button.pack(side=tk.LEFT)

  stop_button = tk.Button(top_frame, text='Stop', fg='yellow',command=stop)
  stop_button.pack(side=tk.BOTTOM)

  # 以下為 bottom 群組
  # bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)
  bottom_button = tk.Button(bottom_frame, text='Back', fg='black', command=backward)
  # 讓系統自動擺放元件（靠下方）
  bottom_button.pack(side=tk.TOP)

  # 運行主程式

  window.mainloop()
  
