import notepad
import wx
import codecs

class myframe4(notepad.MyFrame4):
	def my_click( self, event ):
		#self.SetTitle("My New Title")
		#wx.MessageBox("Hello~~")
		#wx.MessageBox(self.m_textCtrl2.GetValue())
		wx.Exit()

	def sel_close_window( self, event ):
		wx.Exit()

	def sel_about( self, event ):
		w2=About_me(None)
		w2.Show()
		#self.Hide()

	def sel_open_file(self, event):
		r = wx.FileSelector(
			"請選擇要開啟的檔案",
			wildcard="file|*.*",
			flags=wx.FD_OPEN
		)
		# 寫入輸入框
		with codecs.open(r, 'r', 'utf-8') as f:
			self.m_textCtrl2.SetValue(f.read())
	
	def sel_save_file(self, event):
		w = wx.FileSelector(
			"請選擇要儲存的檔名",
			wildcard="file|*.*",
			flags=wx.FD_SAVE
		)
		text_to_save = self.m_textCtrl2.GetValue()
		with codecs.open(w, 'w', 'utf-8') as f:
			f.write(text_to_save)


class About_me(notepad.MyDialog5):
	pass


a=wx.App()
w=myframe4(None)
w.Show()
a.MainLoop()
