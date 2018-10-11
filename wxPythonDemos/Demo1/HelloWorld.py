import wx
from Demo1.LoginFrame import LoginFrame

app = wx.App()
loginWindow = LoginFrame(None, title="Hello World!", size=(400, 200))
loginWindow.Show(True)
app.MainLoop()
