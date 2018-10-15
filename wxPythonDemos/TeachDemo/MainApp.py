import wx
from TeachDemo.LoginWindow import LoginFrame

app = wx.App()
frame = LoginFrame(None, '登陆', (350, 280))
app.MainLoop()