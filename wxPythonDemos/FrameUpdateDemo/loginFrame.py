import wx
import wx.lib.buttons as wxButton

from FrameUpdateDemo.utils import load_image
import FrameUpdateDemo.xDialog as xDialog


class LoginFrame(wx.Frame):

    def __init__(self, parent=None, id=-1, UpdateUI=None):
        super(LoginFrame, self).__init__(parent, id, title='登陆', size=(280, 400))

        self.UpdateUI = UpdateUI
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        logo_sys = wx.Image(load_image('icon1.jpg'), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(panel, id=-1, bitmap=logo_sys, pos=(90, 90), size=(100, 100))

        logo_title = wx.StaticText(panel, id=-1, label='iShavanti', pos=(90, 210))
        logo_title.SetForegroundColour('#0a74f7')
        title_font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        logo_title.SetFont(title_font)

        button_login = wxButton.GenButton(panel, id=-1, label='登陆', pos=(40, 270), size=(200, 40), style=wx.BORDER_NONE)
        button_login.SetBackgroundColour('#0a74f7')
        button_login.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.loginSys, button_login)

    def loginSys(self, event):
        lgDialog = LoginDialog(self.loginFunction, '#0a74f7')
        lgDialog.Show()

    def loginFunction(self, account, password):
        print('接收到用户输入：', account, password)
        # 更新UI-Frame
        self.UpdateUI(1)


class LoginDialog(xDialog.InputDialog):

    def __init__(self, func_callback, themeColor):
        xDialog.InputDialog.__init__(self, '登录系统', func_callback, themeColor)
