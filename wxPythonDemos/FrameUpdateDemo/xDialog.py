import wx


class InputDialog(wx.Dialog):

    def __init__(self, title, func_callback, themeColor):
        wx.Dialog.__init__(self, None, -1, title, size=(300, 300))
        self.func_callback = func_callback
        self.themeColor = themeColor

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)

        accountLabel = wx.StaticText(panel, -1, '账号', pos=(20, 25))
        accountLabel.SetForegroundColour(self.themeColor)
        accountLabel.SetFont(font)

        self.accountInput = wx.TextCtrl(panel, -1, u'', pos=(80, 25), size=(180, -1))
        self.accountInput.SetForegroundColour('gray')
        self.accountInput.SetFont(font)

        passwordLabel = wx.StaticText(panel, -1, '密码', pos=(20, 70))
        passwordLabel.SetForegroundColour(self.themeColor)
        passwordLabel.SetFont(font)

        self.passwordInput = wx.TextCtrl(panel, -1, u'', pos=(80, 70), size=(180, -1), style=wx.TE_PASSWORD)
        self.passwordInput.SetForegroundColour(self.themeColor)
        self.passwordInput.SetFont(font)

        sureBtn = wx.Button(panel, -1, u'登陆', pos=(20, 130), size=(120, 40))
        sureBtn.SetForegroundColour('white')
        sureBtn.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.SureEvent, sureBtn)

        cancelBtn = wx.Button(panel, -1, u'取消', pos=(160, 130), size=(120, 40))
        cancelBtn.SetForegroundColour('white')
        cancelBtn.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.CancelEvent, cancelBtn)

    def SureEvent(self, event):
        account = self.accountInput.GetValue()
        password = self.passwordInput.GetValue()
        # 通过回调函数传递数值
        self.func_callback(account, password)
        # 销毁隐藏Dialog
        self.Destroy()

    def CancelEvent(self, event):
        self.Destroy()