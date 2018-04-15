GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Button placed on GPIO23
GPIO.setup(24, GPIO.OUT)   #LED to GPIO24

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == True:
            GPIO.output(24, True)
            print('Button Pressed...')
            time.sleep(0.2)
        else:
            GPIO.output(24, True)
            time.sleep(0.5)
            print('LED Blinking...')
            GPIO.output(24, False)
            time.sleep(0.5)

except:
    GPIO.cleanup()
    
