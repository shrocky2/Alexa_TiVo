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
gpio_ports = {'TiVo Pause':10000,
              'Netflix':10001,
              'Hulu':10002,
              'YouTube':10003,
              'A.B.C.':786,
              'N.B.C.':782,
              'C.B.S.':784,
              'Fox':788,
              'Comedy Central':754,
              'T.B.S.':767,
              'HGTV':762,
              'ESPN':800}

class device_handler(debounce_handler):
    """Triggers on/off based on 'device' selected.
       Publishes the IP address of the Echo making the request.
    """

    TRIGGERS = {"TiVo Pause":50001,
                "Netflix":50002,
                "Hulu":50003,
                "YouTube":50004,
                "A.B.C.":50005,
                "N.B.C.":50006,
                "C.B.S.":50007,
                "Fox":50008,
                "Comedy Central":50009,
                "T.B.S.":50010,
                "HGTV":50011,
                "ESPN":50012}

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
