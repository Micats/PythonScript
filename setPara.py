# -*- coding:UTF-8 -*-

import xml.dom.minidom
import os
import sys
import xlwt
import xlrd
import xml.etree.ElementTree as ET
from xlwt import Workbook
import sqlite3
import copy
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class ParserXMLDB(object):
	"""for XML"""

	"""for DB"""

	def __init__(self, fileName='AndroidManifest.xml'):
		super(ParserXMLDB, self).__init__()
		self.fileName = fileName
		self.telecomChannalID=''	#电信的渠道号
		self.packageName=''			#包名
		self.umengKey=''			#友盟的key
		self.umengChannalID=''		#友盟的渠道号
		self.nodeSet={}				#保存需要读取和改变的节点
	#放弃这个函数 因为用minidom不可以修改原xml只可以创建和读 可以的 是我不会改而已~~
	def getInfo(self):
		self.dom = xml.dom.minidom.parse(self.fileName);
		root=self.dom.documentElement		#根
		self.packageName=root.getAttribute('package')
		#print self.packageName
		applications=root.getElementsByTagName('application')
		application=applications[0]
		metaDatas=application.getElementsByTagName('meta-data')
		for i in metaDatas:
			if i.getAttribute('android:name')=="umeng_appid":
				self.umengKey=i.getAttribute('android:value')
				self.nodeSet['umeng_appid']=i
				
			if i.getAttribute('android:name')=="UMENG_APPKEY":
				self.umengKey=i.getAttribute('android:value')
				self.nodeSet['UMENG_APPKEY']=i
				
			if i.getAttribute('android:name')=="EGAME_CHANNEL":
				self.telecomChannalID=i.getAttribute('android:value')
				self.nodeSet['EGAME_CHANNEL']=i
				
			if i.getAttribute('android:name')=="umeng_channel":
				self.umengChannalID=i.getAttribute('android:value')
				self.nodeSet['umeng_channel']=i		
		self.createExcel()
		return self.nodeSet
	
	def getInfo2(self):
		self.tree = ET.parse('AndroidManifest.xml')
		root = self.tree.getroot()
		self.packageName=root.attrib['package']
		applications=root.findall('application')
		application=applications[0]
		tags=application.findall('meta-data') 
		for tag in tags:
			if tag.attrib["{http://schemas.android.com/apk/res/android}name"]=="umeng_appid":#=
				self.umengKey=tag.attrib["{http://schemas.android.com/apk/res/android}value"]
				self.nodeSet['umengID']=tag
				#print self.nodeSet['umengKey'].attrib["{http://schemas.android.com/apk/res/android}value"]
			if tag.attrib["{http://schemas.android.com/apk/res/android}name"]=="UMENG_APPKEY":
				self.umengKey=tag.attrib["{http://schemas.android.com/apk/res/android}value"]
				self.nodeSet['umengKey']=tag
			if tag.attrib["{http://schemas.android.com/apk/res/android}name"]=="EGAME_CHANNEL":
				self.telecomChannalID=tag.attrib["{http://schemas.android.com/apk/res/android}value"]
				self.nodeSet["telecomChannalID"]=tag
			if tag.attrib["{http://schemas.android.com/apk/res/android}name"]=="umeng_channel":#=
				self.umengChannalID=tag.attrib["{http://schemas.android.com/apk/res/android}value"]
				self.nodeSet['umengChannalID']=tag
				
		self.createExcel()
		return self.nodeSet
				



	def createExcel(self):
		book=Workbook(encoding='utf-8')
		sheet=book.add_sheet("sheet1",cell_overwrite_ok=True)
		#sheet.write(0,0,"Manifest.xml")
		style = xlwt.XFStyle()
		font = xlwt.Font()
		fontOld=font
		font.bold=True
		font.colour_index=2
		#font.size=88
		style.font=font
		style1=copy.deepcopy(style)
		style1.font.colour_index=3
		sheet.col(0).width=3333*3 #3333为1个单位
		sheet.col(1).width=3333*3
		sheet.col(3).width=3333*3
		sheet.col(4).width=3333*3
		tall_style = xlwt.easyxf('font:height 360;')
		for h in xrange(0,20):
			sheet.row(h).set_style(tall_style)

		alignment = xlwt.Alignment()
		alignment.horz = xlwt.Alignment.HORZ_CENTER
		alignment.vert = xlwt.Alignment.VERT_CENTER
		style.alignment = alignment
		sheet.write_merge(0,0,0,1,"Manifest.xml",style)
		sheet.write_merge(0,0,3,4,"input needed value...",style)#前两个参数表示行数
		sheet.write(1,3,"友盟的key：")
		sheet.write(2,3,"友盟的渠道号：")
		sheet.write(3,3,"电信的渠道号：")
		sheet.write(4,3,"包名:")
		sheet.write(1,4,self.umengKey)
		sheet.write(2,4,self.umengChannalID[1:])
		sheet.write(3,4,self.telecomChannalID)
		sheet.write(4,4,self.packageName)
		row=2
		sheet.write(1,0,"packageName")
		sheet.write(1,1,self.packageName)
		for i in self.nodeSet:#索引值的遍历
			sheet.write(row,0,i)
			sheet.write(row,1,self.nodeSet[i].attrib['{http://schemas.android.com/apk/res/android}value'])
			row=row+1
			#print self.nodeSet[i]
		row=8
		sheet.write_merge(row,row,0,1,"xdlcDBUser.xdlc",style)
		#sheet.write_merge(row,row,3,4,"input needed value...",style)#前两个参数表示行数
		row=row+1
		dblist=self.readDB()
		col=0
		for record in dblist:
			for index in record:
				sheet.write(row,col,index,style1)
				sheet.write(row+1,col,record[index])
				row=row+2
			col=col+1
			row=9
		book.save('temp.xls')
		os.popen("temp.xls")
		str ="have opened xls file,needed override?(y/n)"
		#print str
		input = raw_input(str)
		if input=='y':
			self.readExel()
			self.setInfo()
			self.setDB()
		os.remove("temp.xls")

	def readExel(self):
		print "please wait for 2s..."
		time.sleep(2)
		Workbook=xlrd.open_workbook(r"temp.xls")
		sheet=Workbook.sheet_by_name('sheet1')
		self.tempUmengKey=sheet.cell_value(1,4).encode('utf-8')
		self.tempUmengChannelID=sheet.cell_value(2,4).encode('utf-8')
		self.tempTelecomID=sheet.cell_value(3,4).encode('utf-8')
		self.tempPackageName=sheet.cell_value(4,4).encode('utf-8')
		print self.tempUmengKey,self.tempPackageName,self.tempTelecomID,self.tempUmengChannelID
		
	def setInfo(self):
		self.nodeSet['umengKey'].attrib['{http://schemas.android.com/apk/res/android}value']=self.tempUmengKey
		self.nodeSet['umengID'].attrib['{http://schemas.android.com/apk/res/android}value']='='+self.tempUmengKey
		self.nodeSet['umengChannalID'].attrib['{http://schemas.android.com/apk/res/android}value']='='+self.tempUmengChannelID
		self.nodeSet['telecomChannalID'].attrib['{http://schemas.android.com/apk/res/android}value']=self.tempTelecomID
		self.tree.getroot().attrib['package']=self.tempPackageName
		self.tree.write("newAndroidManifest.xml")
		
		#os.remove("AndroidManifest.xml")
		#os.remove("xdlcDBUser.xdlc")
		pass
		
	def readDB(self):
		path='../Resources/xdlcDBUser.xdlc'
		cx = sqlite3.connect("xdlcDBUser.xdlc")
		cu=cx.cursor()
		cu.execute("select * from GM_Version")
		retValue=cu.fetchone()
		setdb={
			'AppVersion':retValue[0],
			'FrameworkVersion':retValue[1],
			'ChannalID':retValue[2],
			'GameAppName':retValue[3],
			'AppUpdateVersion':retValue[4]
		}
		recordDB=[]
		recordDB.append(setdb)

		cu.execute("select * from OptionS_ThirdParthInfo")
		retValue=cu.fetchone()
		setdb={
			'ThirdPathType':retValue[0],
			'AppName':retValue[2],
			'AppKey':retValue[3],
		}
		recordDB.append(setdb)
		cx.close()
		print recordDB
		return recordDB
		
	def setDB(self):
		cx = sqlite3.connect("xdlcDBUser.xdlc")
		cu=cx.cursor()
		cu.execute("select * from GM_Version")
		retValue=cu.fetchone()
		setdb={
			'AppVersion':retValue[0],
			'FrameworkVserion':retValue[1],
			'ChannalID':retValue[2],
			'GameAppName':retValue[3],
			'AppUpdateVersion':retValue[4]
		}
		versionEnd=self.tempUmengChannelID[2:4]
		versionPre=retValue[0][0:6]
		version=versionPre+versionEnd
		print version
		dup=(version,retValue[1],self.tempUmengChannelID,retValue[3],retValue[4])
		cu.execute("update GM_Version set AppVersion=?,FrameworkVserion=?,ChannelID=?,GameAppName=?,AppUpdateVersion=? ",dup)
		cu.execute("select * from OptionS_ThirdParthInfo")
		retValue=cu.fetchone()
		setdb={
			'ThirdPathType':retValue[0],
			'AppName':retValue[2],
			'AppKey':retValue[3],
			'APPCustom1':retValue[4]
		}
		dup=(self.tempUmengKey,self.tempUmengChannelID)
		cu.execute("update OptionS_ThirdParthInfo set AppKey=?,APPCustom1=?",dup)
		cx.commit()


def run():
	objXML=ParserXMLDB()
	objXML.getInfo2()
	print "already complete"


		
	
	

if __name__ == '__main__':
	run()
	os.system("pause")
	