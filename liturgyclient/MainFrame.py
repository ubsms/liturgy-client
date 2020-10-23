import wx
import logging
from .LiturgyFile import LiturgyFile

class MainFrame(wx.Frame):
    """
    Main application frame
    """

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_CLOSE, self.onClose, self)

        self._liturgyFile = None

        self._pnlMain = wx.Panel(self)

        self._lblLoaded = DataLabel(self._pnlMain)
        szrLoaded = self._lblLoaded.getBoxSizer()
        self._lblLoaded.setLabel("Loaded:")
        self._lblLoaded.setData("none")

        self._lblCurrent = DataLabel(self._pnlMain)
        szrCurrent = self._lblCurrent.getBoxSizer()
        self._lblCurrent.setLabel("Current:")
        self._lblCurrent.setData("")

        self._lblNext = DataLabel(self._pnlMain)
        szrNext = self._lblNext.getBoxSizer()
        self._lblNext.setLabel("Next:")
        self._lblNext.setData("")

        szrButtons = wx.BoxSizer(wx.HORIZONTAL)
        szButton = wx.Size(100, 100)
        btnLoad = wx.Button(self._pnlMain, label="LOAD", size=szButton)
        self.Bind(wx.EVT_BUTTON, self.onLoad, btnLoad)
        btnNext = wx.Button(self._pnlMain, label="NEXT", size=szButton)
        self.Bind(wx.EVT_BUTTON, self.onNext, btnNext)
        szrButtons.Add(btnLoad)
        szrButtons.Add(btnNext, wx.SizerFlags().Border(wx.LEFT, 10))

        szrMain = wx.BoxSizer(wx.VERTICAL)
        szrMain.Add(szrLoaded)
        szrMain.Add(szrCurrent)
        szrMain.Add(szrNext)
        szrMain.Add(szrButtons, wx.SizerFlags().Border(wx.LEFT, 10))
        self._pnlMain.SetSizerAndFit(szrMain)
    
    def onLoad(self, event):
        fdgFileDialog = wx.FileDialog(self._pnlMain, message="Please select a liturgy file", wildcard="Liturgy files|*.yml", style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        if fdgFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self._liturgyFile = LiturgyFile(fdgFileDialog.GetPath())

        self._lblLoaded.setData(self._liturgyFile.name())
        self._lblCurrent.setData(self._liturgyFile.currentSlideName())
        self._lblNext.setData(self._liturgyFile.nextSlideName())

    def onNext(self, event):
        if self._liturgyFile is None:
            return
        
        self._liturgyFile.next()
        self._lblCurrent.setData(self._liturgyFile.currentSlideName())
        self._lblNext.setData(self._liturgyFile.nextSlideName())
    
    def onClose(self, event):
        if self._liturgyFile is not None:
            self._liturgyFile.clear()

        self.Destroy()

class DataLabel():
    def __init__(self, parent, width=200, height=40, label="Label:", data="data"):
        szLabel = wx.Size(200, height)

        self._stLabel = wx.StaticText(parent, label=label, style=wx.ALIGN_RIGHT, size=szLabel)
        font = self._stLabel.GetFont()
        font.PointSize += 5
        font = font.Bold()
        self._stLabel.SetFont(font)

        szData = wx.Size(500, height)

        self._stData = wx.StaticText(parent, label=data, size=szData)
        font = self._stData.GetFont()
        font.PointSize += 5
        self._stData.SetFont(font)

        self._szrMain = wx.BoxSizer(wx.HORIZONTAL)

        self._szrMain.Add(self._stLabel)
        self._szrMain.Add(self._stData, wx.SizerFlags().Border(wx.LEFT, 10))
        
    def getBoxSizer(self):
        return self._szrMain
    
    def setLabel(self, label):
        self._stLabel.SetLabel(label)

    def setData(self, label):
        self._stData.SetLabel(label)