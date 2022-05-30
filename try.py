import ADS
import time

ads = ADS.ADS1115()

while True:
    volt = ads.readADCSingleEnded(channel=1)
    
    print("{:.0f}".format(volt))
    
    time.sleep(0.1)


