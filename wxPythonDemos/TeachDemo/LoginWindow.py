import wx
import requests
from requests.cookies import RequestsCookieJar

class LoginFrame(wx.Frame):

    def __init__(self, parent, title, size):
        super(LoginFrame, self).__init__(parent, title=title, size=size)

        # 员工类型：普通员工0， 管理员1
        self.user_type = 0

        panel = wx.Panel(self)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        bgSizer = wx.GridBagSizer(2, 2)
        nameText = wx.StaticText(panel, label='用户名：')
        self.nameInput = wx.TextCtrl(panel)
        passText = wx.StaticText(panel, label='密码：')
        self.passInput = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        bgSizer.Add(nameText, pos=(0, 0), flag=wx.ALL, border=5)
        bgSizer.Add(self.nameInput, pos=(0, 1), flag=wx.EXPAND | wx.ALL)
        bgSizer.Add(passText, pos=(1, 0), flag=wx.ALL, border=5)
        bgSizer.Add(self.passInput, pos=(1, 1), flag=wx.EXPAND | wx.ALL)
        bgSizer.AddGrowableCol(1, 1)

        rList = ['员工', '管理员']
        rBox = wx.RadioBox(panel, label='用户类型', choices=rList, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        rBox.Bind(wx.EVT_RADIOBOX, self.UserChoose)

        loginBtn = wx.Button(panel, id=1, label='登陆')
        loginBtn.Bind(wx.EVT_BUTTON, self.LoginClick)

        bSizer.Add(bgSizer, flag=wx.ALL | wx.EXPAND, border=15)
        bSizer.Add(rBox, flag=wx.ALL | wx.EXPAND, border=15)
        bSizer.Add(loginBtn, flag=wx.ALIGN_CENTER_HORIZONTAL)
        panel.SetSizer(bSizer)
        self.Show(True)
        self.Center()

    def LoginClick(self, event):
        username = self.nameInput.GetValue()
        password = self.passInput.GetValue()

        base_url = 'http://127.0.0.1:8000/blog/login/'
        page = requests.get('http://127.0.0.1:8000/blog/login_page/')
        csrf = page.cookies.get('csrftoken')
        data = {
            'csrfmiddlewaretoken': csrf,
            'username': username,
            'password': password,
            'user_type': self.user_type
        }
        cookie = RequestsCookieJar()
        cookie.set('csrftoken', csrf)
        response = requests.post(base_url, data=data, cookies=cookie)
        if response.text == 'OK':
            wx.MessageBox('登陆成功！', '提示', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('登陆失败!', '提示', wx.OK | wx.ICON_INFORMATION)

    def UserChoose(self, event):
        rBox = event.GetEventObject()
        rbLabel = rBox.GetStringSelection()
        if rbLabel == '员工':
            self.user_type = 0
        else:
            self.user_type = 1
