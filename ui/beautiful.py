import wx
class Beautiful:
  def __init__(self, obj):
    self.obj = obj

  def render(self):
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, self.obj.getName())
    frame.Show(True)
    app.MainLoop()
