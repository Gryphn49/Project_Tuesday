import wx

class MyFrame(wx.Frame):
	def __init__ (self):
		
		wx.Frame.__init__(self, None,
			
			pos=wx.DefaultPosition, #position

			size=wx.Size(450, 100),
			
			style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			
			title="Tuesday")
		
		panel = wx.Panel(self)
		my_sizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
		label="Hello, I am Tuesday. How can I help?"
		my_sizer.Add(lbl, 0, wx.ALL, 5)
		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
		self.txt.SetFocus() #focus text
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.ADD(self.txt, 0, wx.ALL, 5)
		panel.SetSizer(my_sizer)
		self.Show()
