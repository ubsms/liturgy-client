from ruamel.yaml import YAML
import json
from amcp_pylib.module.template import CG_ADD, CG_PLAY, CG_NEXT, CG_CLEAR
from . import Connector
import logging

class LiturgyFile:
    def __init__(self, filename):
        logging.debug("Opening File")
        with open(filename, "r") as fh:
            yml = fh.read()
        yaml=YAML(typ='safe')

        logging.debug("Parsing YAML")
        doc = yaml.load(yml)
        logging.debug("Dumping to JSON")
        jsn = json.dumps(doc)
        logging.debug("Sanitising")
        safejsn = jsn.replace("\\n","\\\\n")
        
        self._slides = doc['slides']
        self._name = doc['name']
        self._slide = 0
        self._client = Connector.getConnector()
        self.clear()
        logging.debug("Sending Command")
        response = self._client.send(CG_ADD(video_channel=1, layer=20, cg_layer=20, template="UBSMS/LITURGY", play_on_load=1, data=safejsn))
        logging.debug(response)
    
    def clear(self):
        logging.debug("Clearing")
        self._client.send(CG_CLEAR(video_channel=1, layer=20))

    def slideCount(self):
        return len(self._slides)
    
    def name(self):
        return self._name

    def slide(self):
        return self._slide
    
    def slides(self):
        return len(self._slides)

    def currentSlideName(self):
        name = self._slides[self._slide]['name']
        if self._slides[self._slide]['type'] == "blank":
            name = "Blank"
        return name

    def nextSlideName(self):
        if self._slide == self.slides() - 1:
            return "ENDED"

        name = self._slides[self._slide + 1]['name']
        if self._slides[self._slide + 1]['type'] == "blank":
            name = "Blank"
        return name
    
    def next(self):
        logging.debug("Cha Cha next slide please")
        if self._slide == self.slides() - 1:
            return
        self._slide += 1
        response = self._client.send(CG_NEXT(video_channel=1, cg_layer=20, layer=20))
        logging.debug(response)

    def __repr__(self):
        return "Liturgy File: {}".format(self._name)