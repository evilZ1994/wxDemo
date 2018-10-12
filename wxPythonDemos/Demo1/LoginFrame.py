import wx
import requests
from requests.cookies import RequestsCookieJar


class LoginFrame(wx.Frame):

    def __init__(self, parent, title, size):
        super(LoginFrame, self).__init__(parent, title=title, size=size)
        self.nameInput = None
        self.passInput = None
        self.InitUI()
        self.Center()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.GridBagSizer(3, 2)

        nameTitle = wx.StaticText(panel, label='用户名')
        passTitle = wx.StaticText(panel, label='密码')

        self.nameInput = wx.TextCtrl(panel)
        self.passInput = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        loginBtn = wx.Button(panel, label='登陆')
        loginBtn.Bind(wx.EVT_BUTTON, self.onLogin)

        sizer.Add(nameTitle, pos=(0, 0), flag=wx.ALL, border=5)
        sizer.Add(self.nameInput, pos=(0, 1), flag=wx.EXPAND | wx.ALL)
        sizer.Add(passTitle, pos=(1, 0), flag=wx.ALL, border=5)
        sizer.Add(self.passInput, pos=(1, 1), flag=wx.EXPAND | wx.ALL)
        sizer.Add(loginBtn, span=(1, 2), pos=(2, 0), flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)
        sizer.AddGrowableCol(1, 1)

        vbox.Add(sizer, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(vbox)

    def onLogin(self, event):
        name = self.nameInput.GetLineText(0)
        password = self.passInput.GetLineText(0)

        base_url = 'http://127.0.0.1:8000/blog/login/'
        # 首次访问，获取csrf token
        page = requests.get('http://127.0.0.1:8000/blog/login_page/')
        csrf = page.cookies.get('csrftoken')
        data = {
            'csrfmiddlewaretoken': csrf,
            'username': name,
            'password': password
        }
        cookie = RequestsCookieJar()
        cookie.set('csrftoken', csrf)
        response = requests.post(base_url, data=data, cookies=cookie)
        if response.text == 'OK':
            self.onLoginSuccess()
        else:
            self.onLoginFail()
        event.Skip()

    def onLoginSuccess(self):
        wx.MessageBox('登陆成功！', 'Message', wx.OK | wx.ICON_INFORMATION)

    def onLoginFail(self):
        wx.MessageBox('用户名或密码错误！', 'Error', wx.OK | wx.ICON_INFORMATION)
