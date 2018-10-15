import wx
import FrameUpdateDemo.guiManager as guiManager

class MainApp(wx.App):

    def OnInit(self):
        self.manager = guiManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(0)
        self.frame.Show(True)
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type)
        self.frame.Show(True)

def main():
    app = MainApp()
    app.MainLoop()

if __name__ == '__main__':
    main()