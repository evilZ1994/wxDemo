import wx


class ContentFrame(wx.Frame):

    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='iShavanti', size=(400, 400))
        self.UpdateUI = UpdateUI
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, u'Welcome!', pos=(30, 30))
