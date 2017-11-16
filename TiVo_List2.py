""" 
   Original Author:  Surendra Kane
   Edited by: shrocky2
  Script to control your TiVo using a Amazon Echo.
"""

import fauxmo
import logging
import time

from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

print " Control+C to exit program"
gpio_ports = {'TiVo Pause':1,'A.B.C.':2,'N.B.C.':3,'C.B.S.':4,'Fox':5,'Comedy Central':6,'T.B.S.':7,'HGTV':8,'ESPN':9,'Netflix':10,'Hulu':11,'YouTube':12}

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
                "YouTube":50012}

    def trigger(self,port,state):
      TiVo_IP_Address = "192.168.0.47"
      print 'port:',  port,  "   state:", state
      if state == True:
        print ""
      else:
        print ""

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
