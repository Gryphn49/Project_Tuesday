import wx #Adds wx
import wikipedia #Adds wikipedia
import wolframalpha #Adds wolfram alpha

class MyFrame(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Tuesday")

        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hi. I'm Tuesday. How can I help?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        
        #answer stage
		try:
			#WOLFRAM ALPHA
			app_id = "G58JY9-WQ963T9EQV" #to get the info

			client = wolframalpha.Client(app_id) #connecting to info

			result = client.query(input) #collecting result
			answer = next(result.results).text #processing answer

			print answer #answering with answer

		except:
			#WIKIPEDIA
			#wikipedia.set_lang("en") #Language!

			print wikipedia.summary(input)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

"""import wikipedia #Adds wikipedia
import wolframalpha #Adds wolfram alpha

while True:
	input = raw_input("Hi. What do you want? ") #Asking stage

	#answer stage
	try:
		#WOLFRAM ALPHA
		app_id = "G58JY9-WQ963T9EQV" #to get the info

		client = wolframalpha.Client(app_id) #connecting to info

		result = client.query(input) #collecting result
		answer = next(result.results).text #processing answer

		print answer #answering with answer

	except:
		#WIKIPEDIA
		#wikipedia.set_lang("en") #Language!

		print wikipedia.summary(input)"""