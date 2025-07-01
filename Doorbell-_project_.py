from engi1020.arduino.api import *
from time import sleep

#detect motion and print "Motion detected"

def motion_sensor(pin):
    
    if digital_read(pin):
        oled_clear()
        a=True
        oled_print("MOTION DETECTED")
          
    else:
        oled_clear()
        a=False
        digital_write(4,False)
        buzzer_stop(5)
        oled_print("No Motion Detected")
    
    if a==True:
        digital_write(4,True)
        buzzer_frequency(5,700)
        sleep(0.15)
        digital_write(4,False)
        buzzer_stop(5)
            
#----------------------------------------------------            MAIN          --------------------------------------------------------------------------------------------------------------------
    
while True:
    rgb_lcd_clear()
    servo_set_angle(7,0)
    
    if digital_read(6)==False:
        
        motion_sensor(2)
        
#press button to turn on the buzzer
        
    else:
        oled_clear()
        oled_print("Knock Knock :)")
        oled_print('             ')
        oled_print('    ^     ^')
        oled_print('     _____  ')
        
        
        for i in range(3):
            buzzer_frequency(5,1000)
            sleep(0.5)
            buzzer_frequency(5,600)
            sleep(1.5)
  
        buzzer_stop(5)
        oled_clear()
        
#ask user yes or no to open the door
        
        rgb_lcd_clear()
        rgb_lcd_print("Open the Door? : ")
        sleep(1)
        rgb_lcd_clear()
        rgb_lcd_print("Select YES/NO")
        sleep(1)
        rgb_lcd_clear()
        rgb_lcd_print("using")
        sleep(1)
        rgb_lcd_clear()
        rgb_lcd_print("ROTATRY DIAL")
        sleep(1)
        rgb_lcd_clear()


        while digital_read(3) != True:
                a = 0
                l = 511.5
                for i in range(2):
                    if (0 + l * (i)) < analog_read(0) < l * (i + 1):
                        if i == 0:
                            rgb_lcd_print("YES")
                            
                            ans=0
                        else:
                            ans=1
                            rgb_lcd_print("NO ")
        if ans==0:
            servo_set_angle(7,90)
            rgb_lcd_print("Door is Open")
            sleep(6)
                
        elif ans==1:
            servo_set_angle(7,0)
            rgb_lcd_print("OK")

        else:
            rgb_lcd_print("Wrong Input")
        
        
        
      
    