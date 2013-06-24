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

    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
    self.CreateStatusBar()
    filemenu= wx.Menu()
    menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
    filemenu.AppendSeparator()
    menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
    menuBar = wx.MenuBar()
    menuBar.Append(filemenu,"&File")
    self.SetMenuBar(menuBar)
    self.sizerH = wx.BoxSizer(wx.HORIZONTAL)
    clearButton = wx.Button(self, -1, "Execute query")
    self.sizerH.Add(clearButton, 1, wx.EXPAND)
    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.sizer.Add(self.control, 1, wx.EXPAND)
    self.sizer.Add(self.sizerH, 0, wx.EXPAND)
    self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
    self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
    self.SetSizer(self.sizer)
    self.SetAutoLayout(1)
    self.sizer.Fit(self)
    self.Show(True)

  def OnAbout(self,e):
    dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
    dlg.ShowModal() # Show it
    dlg.Destroy() # finally destroy it when finished.
    
  def OnExit(self,e):
    self.Close(True)  # Close the frame.
