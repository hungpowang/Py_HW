# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jun 29 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.notebook = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"關閉檔程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem4 )

		self.notebook.Append( self.m_menu3, u"檔案" )

		self.m_menu4 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem5 )

		self.notebook.Append( self.m_menu4, u"關於" )

		self.SetMenuBar( self.notebook )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 2000,2000 ), wx.TE_MULTILINE )
		bSizer10.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		self.m_panel16.SetSizer( bSizer10 )
		self.m_panel16.Layout()
		bSizer10.Fit( self.m_panel16 )
		bSizer9.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.sel_open_file, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.sel_save_file, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.sel_close_window, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.sel_about, id = self.m_menuItem5.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def sel_open_file( self, event ):
		event.Skip()

	def sel_save_file( self, event ):
		event.Skip()

	def sel_close_window( self, event ):
		event.Skip()

	def sel_about( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog5
###########################################################################

class MyDialog5 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"關於作者", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"作者: Robert\nMail: muffinwang@g.ntu.edu.tw\nWebsite: www.XXX.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer14.Add( self.m_staticText4, 0, wx.ALL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


