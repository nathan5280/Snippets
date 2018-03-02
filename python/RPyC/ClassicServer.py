#!/home/nathan/.virtualenvs/dl/bin/python3.6
"""
classic rpyc server (threaded, forking or std) running a SlaveService
usage:
    rpyc_classic.py                         # default settings
    rpyc_classic.py -m forking -p 12345     # custom settings

    # ssl-authenticated server (keyfile and certfile are required)
    rpyc_classic.py --ssl-keyfile keyfile.pem --ssl-certfile certfile.pem --ssl-cafile cafile.pem
"""
from rpyc.utils.server import ThreadedServer
from rpyc.core import SlaveService
import threading

if __name__ == "__main__":
    # ClassicServer.run()
    print('Main: ', threading.current_thread())

    t = ThreadedServer(SlaveService, hostname='127.0.0.1', port=18812)
    t.start()
