from amcp_pylib.core import Client
from amcp_pylib.module.query import VERSION
import logging

client = None

def init(ip="127.0.0.1", port=5250):
    logging.info("Connecting")
    global client
    if client is None:
        client = Client()
        client.connect(ip, port)

def getConnector():
    global client
    if client is None:
        logging.debug("Connector not initialised, init now")
        init()
    return client