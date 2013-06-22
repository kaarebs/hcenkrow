import wx
class Beautiful:
  def __init__(self, obj):
    self.obj = obj

  def render(self):
    app = wx.App(False)
    frame = MyFrame(None, self.obj.getName(), self.obj)
    app.MainLoop()

class MyFrame(wx.Frame):
  def __init__(self, parent, title, obj):
    wx.Frame.__init__(self, parent, title=title, size=(500,250))
    res = ""
    for row in obj.list():
      res += ("" + str(row) + "\n")

    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE).AppendText(res)
    self.Show(True)
