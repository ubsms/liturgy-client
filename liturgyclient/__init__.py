import logging

def run(ip="127.0.0.1", port=5250):
    import wx
    from .MainFrame import MainFrame
    from . import Connector

    logging.info("Booting")

    logging.info("Starting connector")
    Connector.init(ip, port)

    app = wx.App()

    frm = MainFrame(None, title="Liturgy", style=wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.CLOSE_BOX)

    frm.Show()

    app.MainLoop()