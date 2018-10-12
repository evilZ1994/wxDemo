import wx

class MainApp(wx.App):

    def OnInit(self):

        return True

    def UpdateUI(self, type):
        pass

def main():
    app = MainApp()
    app.MainLoop()

if __name__ == '__main__':
    main()