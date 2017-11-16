""" 
   Author: Surendra Kane

  Script to control individual Raspberry Pi GPIO's.
  Applicable ONLY for Raspberry PI 3, based on schematics.
  Please modify for other board versions to control correct GPIO's.
"""

import fauxmo
import logging
import time
import RPi.GPIO as GPIO
#Telnet Added Information
import getpass
import sys
import telnetlib
#End Telnet Added Information

from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

print " Control+C to exit program"

#gpio_ports = {'gpio1':1,'gpio2':2,'gpio3':3,'gpio4':4,'gpio5':5,'gpio6':6,'gpi$
gpio_ports = {'TiVo Pause':15,'A.B.C.':16,'N.B.C.':17,'C.B.S.':18,'Fox':19,'Comedy Central':20,'T.B.S.'$

class device_handler(debounce_handler):
    """Triggers on/off based on GPIO 'device' selected.
       Publishes the IP address of the Echo making the request.
    """
    """
    TRIGGERS = {"gpio1":50001,
                "gpio2":50002,
                "gpio3":50003,
                "gpio4":50004,
                "gpio5":50005,
                "gpio6":50006,
                "gpio7":50007,
                "gpio8":50008,
                "gpio9":50009,
                "gpio10":50010,
                "gpio11":50011,
                "gpio12":50012,
                "gpio13":50013,
                "gpio14":50014,
    """
    TRIGGERS = {"TiVo Pause":50015,
                "A.B.C.":50016,
                "N.B.C.":50017,
                "C.B.S.":50018,
                "Fox":50019,
                "Comedy Central":50020,
                "T.B.S.":50021,
                "Netflix":50022,
                "YouTube":50023,
                "relay":50024,
                "gpio25":50025,
                "gpio26":50026}

    def trigger(self,port,state):
      TiVo_IP_Address = "192.168.0.47”
      print 'port:',  port,  "   state:", state
      if state == True:
#Temp Removed for Telnet Info
#        GPIO.setup(port, GPIO.OUT)
#        GPIO.output(port,GPIO.HIGH)

#Find what port was triggered, change the channel accordingly
        if port == 15: #TiVo Paused
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE PAUSE\r")
                        tn.close()
                        print "TiVo Paused"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 16: #ABC
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 786\r")
                        tn.close()
                        print "TiVo Channel Changed to ABC"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 17: #NBC
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 782\r")
                        tn.close()
                        print "TiVo Channel Changed to NBC"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 18: #CBS
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 784\r")
                        tn.close()
                        print "TiVo Channel Changed to CBS"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 19: #Fox
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 788\r")
                        tn.close()
                        print "TiVo Channel Changed to Fox"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 20: #Comedy Central
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 754\r")
                        tn.close()
                        print "TiVo Channel Changed to Comedy Central"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 21: #TBS
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 767\r")
                        tn.close()
                        print "TiVo Channel Changed to TBS"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 22: #Netflix
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE TIVO\r")
                        time.sleep(.4)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(.4)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(.4)
                        tn.write("IRCODE RIGHT\r")
                        time.sleep(1)
                        tn.write("IRCODE SELECT\r")
                        tn.close()
                        print "TiVo App Netflix is Starting"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 23: #YouTube
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE TIVO\r")
                        time.sleep(.4)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(.4)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(1)
                        tn.write("IRCODE RIGHT\r")
                        time.sleep(1)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(.4)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(.4)
                        tn.write("IRCODE DOWN\r")
                        time.sleep(.4)
                        tn.write("IRCODE SELECT\r")
                        tn.close()
                        print "TiVo App YouTube is Starting"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        if port == 24: #relay
                pinList = [7, 11, 13, 15]

                for i in pinList:
                        GPIO.setup(i, GPIO.OUT)
                        GPIO.output(i, GPIO.HIGH)

                GPIO.output(7, 0)
                GPIO.output(11, 0)
                GPIO.output(13, 0)
                GPIO.output(15, 0)
                time.sleep(.5)
                GPIO.output(7, 0)
                GPIO.output(11, 1)
                GPIO.output(13, 0)
                GPIO.output(15, 1)
                time.sleep(.5)
                GPIO.output(7, 1)
                GPIO.output(11, 0)
                GPIO.output(13, 1)
                GPIO.output(15, 0)
                time.sleep(.5)
                GPIO.output(7, 0)
                GPIO.output(11, 1)
                GPIO.output(13, 0)
                GPIO.output(15, 1)
                time.sleep(.5)
                GPIO.output(7, 1)
                GPIO.output(11, 0)
                GPIO.output(13, 0)
                GPIO.output(15, 1)
                time.sleep(.5)
                GPIO.output(7, 0)
                GPIO.output(11, 1)
                GPIO.output(13, 1)
                GPIO.output(15, 0)
                time.sleep(.5)
                GPIO.output(7, 1)
                GPIO.output(11, 1)
                GPIO.output(13, 1)
                GPIO.output(15, 1)
                time.sleep(.5)

#               GPIO.cleanup()
        print " "
      else:
#        GPIO.setup(port, GPIO.OUT)
#        GPIO.output(port,GPIO.LOW)
        if port == 22 or 23: #Netflix or YoutTube turn OFF
                try:
                        #Telnet Shit
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE LIVETV\r")
                        tn.close()
                        print "TiVo LiveTv Pressed"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        print "ELSE LOW OUTPUT"
        print " "

    def act(self, client_address, state, name):
        print "State", state, "on", name, "from client @", client_address, "gpio port:",gpio_ports[str(name)]
        self.trigger(gpio_ports[str(name)],state)
        return True

if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    print " "
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
            break
