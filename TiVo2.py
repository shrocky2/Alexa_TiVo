""" 
   Author: Originally Surendra Kane
   Edited by: shrocky2
  Script to control your TiVo using a Amazon Echo.
  This script originally was used to control the gpio ports on the raspberry pi, so you will see remnants of that code. 
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
gpio_ports = {'TiVo Pause':1,'A.B.C.':786,'N.B.C.':782,'C.B.S.':784,'Fox':5,'Comedy Central':754,'T.B.S.':767,'HGTV':8,'ESPN':9,'Netflix':10,'Hulu':11,'YouTube':12,'The CW':13,'A and E':14,'Cartoon Network':15,'FX':16,'History Channel':17,'T.L.C.':18,'T.N.T.':19,'TV Land':20,'USA':21,'VH One':22,'WGN':23,'Travel Channel':24}

class device_handler(debounce_handler):
    """Triggers on/off based on 'device' selected.
       Publishes the IP address of the Echo making the request.
    """

    TRIGGERS = {"TiVo Pause":50001,
                "A.B.C.":50002,
                "N.B.C.":50003,
                "C.B.S.":50004,
                "Fox":50005,
                "Comedy Central":50006,
                "T.B.S.":50007,
                "HGTV":50008,
                "ESPN":50009,
                "Netflix":50010,
                "Hulu":50011,
                "YouTube":50012,
                "The CW":50013,
                "A and E":50014,
                "Cartoon Network":50015,
                "FX":50016,
                "History Channel":50017,
                "T.L.C.":50018,
                "T.N.T.":50019,
                "TV Land":50020,
                "USA":50021,
                "VH One":50022,
                "WGN":50023,
                "Travel Channel":50024}

    def trigger(self,port,state):
      TiVo_IP_Address = "192.168.0.47"
      print 'port:',  port,  "   state:", state
      if state == True:
        #Find what port was triggered, change the channel accordingly
         try:
             tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
             tn.write("IRCODE PAUSE\r")
             tn.close()
             print "Channel Changed to " port
          except:
             print "Telnet Error, Check TiVo IP Address"
        if port == 1: #TiVo Paused
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE PAUSE\r")
                        tn.close()
                        print "TiVo Paused"
                except:
                        print "Telnet Error, Check TiVo IP Address"
                          
        if port == 10: #Netflix
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
        
        if port == 11: #Hulu
                print "Hulu Code Needed"
        if port == 12: #YouTube
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
        if port == 10 or port == 12: #Netflix or YoutTube turn OFF
                try:
                        tn = telnetlib.Telnet(TiVo_IP_Address, "31339")
                        tn.write("IRCODE LIVETV\r")
                        tn.close()
                        print "TiVo LiveTv Pressed"
                except:
                        print "Telnet Error, Check TiVo IP Address"
        print " "

    def act(self, client_address, state, name):
        print "State", state, "on", name, "from client @", client_address, "port:",gpio_ports[str(name)]
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
