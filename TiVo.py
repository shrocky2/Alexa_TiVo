""" 
   Author: Originally Surendra Kane
   Edited by: shrocky2

  Script to control your TiVo using a Amazon Echo.
"""

import fauxmo
import logging
import time
#Telnet Added Information
import getpass
import sys
import telnetlib
#End Telnet Added Information

from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

print " Control+C to exit program"
gpio_ports = {'TiVo Pause':15,'A.B.C.':16,'N.B.C.':17,'C.B.S.':18,'Fox':19,'Comedy Central':20,'T.B.S.':21,'HGTV':22,'ESPN':23,'Netflix':24,'Hulu':25,'YouTube':26}

class device_handler(debounce_handler):
    """Triggers on/off based on 'device' selected.
       Publishes the IP address of the Echo making the request.
    """

    TRIGGERS = {"TiVo Pause":50015,
                "A.B.C.":50016,
                "N.B.C.":50017,
                "C.B.S.":50018,
                "Fox":50019,
                "Comedy Central":50020,
                "T.B.S.":50021,
                "HGTV":50022,
                "ESPN":50023,
                "Netflix":50024,
                "Hulu":50025,
                "YouTube":50026}

    def trigger(self,port,state):
      TiVo_IP_Address = "192.168.0.47”
      print 'port:',  port,  "   state:", state
      if state == True:
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
        if port == 22: #HGTV
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 762\r")
                        tn.close()
                        print "TiVo Channel Changed to TBS"
                except:
                        print "Telnet Error, Check TiVo IP Address"                     
        if port == 23: #ESPN
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("SETCH 800\r")
                        tn.close()
                        print "TiVo Channel Changed to TBS"
                except:
                        print "Telnet Error, Check TiVo IP Address"                     
        if port == 24: #Netflix
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
        
        if port == 25: #Hulu
            
        if port == 26: #YouTube
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
        
                
      else:
        if port == 24 or 25 or 26: #Netflix or YoutTube turn OFF
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE LIVETV\r")
                        tn.close()
                        print "TiVo LiveTv Pressed"
                except:
                        print "Telnet Error, Check TiVo IP Address"
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
