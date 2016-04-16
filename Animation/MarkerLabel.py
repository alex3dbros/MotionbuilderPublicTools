# tool used to label optical markers

from pyfbsdk import *
from pyfbsdk_additions import *
import pythonidelib
from PySide import QtCore, QtGui, shiboken
from PyQt4.QtCore import pyqtSignal
import sys
import inspect
import os

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8

	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class NativeWidgetHolder(FBWidgetHolder):

	def WidgetCreate(self, pWidgetParent):
		self.mNativeQtWidget = Ui_TabWidget(shiboken.wrapInstance(pWidgetParent, QtGui.QWidget))
		return shiboken.getCppPointer(self.mNativeQtWidget)[0]


class Ui_TabWidget(QtGui.QTabWidget):

	def __init__(self, parent=None):
		super(Ui_TabWidget, self).__init__(parent)
		self.setupUi(self)
		self.LabelsList = {}

	def set_button_action(self):
		mode = 1
		objectsList = FBModelList()
		FBGetSelectedModels(objectsList)
		actor_name = str(self.ActorName.text())
		object_name = str(self.sender().objectName())
		if len(actor_name) > 0:
			actor_name = actor_name + "_"
		if len(objectsList) > 0 and str(self.ToolMode.currentText()) == "Rename":
			objectsList[0].Name = actor_name + object_name
		else:
			try:
				for comp in FBSystem().Scene.Components:
					comp.Selected = False
				c3d_obj = FBFindModelByLabelName("C3D:" + actor_name + object_name)	
				c3d_obj.Selected = True
				pythonidelib.FlushOutput()
			except:
				pass

		pythonidelib.FlushOutput()

	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(1201, 772)

		self.HeadGroup = QtGui.QGroupBox(Form)
		self.HeadGroup.setGeometry(QtCore.QRect(480, 20, 241, 80))
		self.HeadGroup.setObjectName(_fromUtf8("HeadGroup"))
		self.HeadLeft = QtGui.QPushButton(self.HeadGroup)
		self.HeadLeft.setGeometry(QtCore.QRect(160, 20, 51, 23))
		self.HeadLeft.setObjectName(_fromUtf8("HeadLeft"))
		self.HeadRight = QtGui.QPushButton(self.HeadGroup)
		self.HeadRight.setGeometry(QtCore.QRect(30, 20, 51, 23))
		self.HeadRight.setObjectName(_fromUtf8("HeadRight"))
		self.HeadFront = QtGui.QPushButton(self.HeadGroup)
		self.HeadFront.setGeometry(QtCore.QRect(90, 50, 61, 23))
		self.HeadFront.setObjectName(_fromUtf8("HeadFront"))
		self.HeadTop = QtGui.QPushButton(self.HeadGroup)
		self.HeadTop.setGeometry(QtCore.QRect(90, 20, 61, 23))
		self.HeadTop.setObjectName(_fromUtf8("HeadTop"))
		self.ChestGroup = QtGui.QGroupBox(Form)
		self.ChestGroup.setGeometry(QtCore.QRect(550, 120, 101, 101))
		self.ChestGroup.setObjectName(_fromUtf8("ChestGroup"))
		self.ChestTop = QtGui.QPushButton(self.ChestGroup)
		self.ChestTop.setGeometry(QtCore.QRect(20, 30, 61, 23))
		self.ChestTop.setObjectName(_fromUtf8("ChestTop"))
		self.ChestLow = QtGui.QPushButton(self.ChestGroup)
		self.ChestLow.setGeometry(QtCore.QRect(20, 60, 61, 23))
		self.ChestLow.setObjectName(_fromUtf8("ChestLow"))
		self.BackGroup = QtGui.QGroupBox(Form)
		self.BackGroup.setGeometry(QtCore.QRect(480, 220, 241, 61))
		self.BackGroup.setObjectName(_fromUtf8("BackGroup"))
		self.BackRight = QtGui.QPushButton(self.BackGroup)
		self.BackRight.setGeometry(QtCore.QRect(20, 30, 61, 23))
		self.BackRight.setObjectName(_fromUtf8("BackRight"))
		self.BackTop = QtGui.QPushButton(self.BackGroup)
		self.BackTop.setGeometry(QtCore.QRect(90, 10, 61, 23))
		self.BackTop.setObjectName(_fromUtf8("BackTop"))
		self.BackLeft = QtGui.QPushButton(self.BackGroup)
		self.BackLeft.setGeometry(QtCore.QRect(160, 30, 61, 23))
		self.BackLeft.setObjectName(_fromUtf8("BackLeft"))
		self.LShoulderGroup = QtGui.QGroupBox(Form)
		self.LShoulderGroup.setGeometry(QtCore.QRect(670, 120, 111, 81))
		self.LShoulderGroup.setObjectName(_fromUtf8("LShoulderGroup"))
		self.LShoulderTop = QtGui.QPushButton(self.LShoulderGroup)
		self.LShoulderTop.setGeometry(QtCore.QRect(20, 20, 75, 23))
		self.LShoulderTop.setObjectName(_fromUtf8("LShoulderTop"))
		self.LShoulderBack = QtGui.QPushButton(self.LShoulderGroup)
		self.LShoulderBack.setGeometry(QtCore.QRect(20, 50, 75, 23))
		self.LShoulderBack.setObjectName(_fromUtf8("LShoulderBack"))
		self.RShoulderGroup = QtGui.QGroupBox(Form)
		self.RShoulderGroup.setGeometry(QtCore.QRect(410, 120, 111, 81))
		self.RShoulderGroup.setObjectName(_fromUtf8("RShoulderGroup"))
		self.RShoulderBack = QtGui.QPushButton(self.RShoulderGroup)
		self.RShoulderBack.setGeometry(QtCore.QRect(20, 50, 75, 23))
		self.RShoulderBack.setObjectName(_fromUtf8("RShoulderBack"))
		self.RShoulderTop = QtGui.QPushButton(self.RShoulderGroup)
		self.RShoulderTop.setGeometry(QtCore.QRect(20, 20, 75, 23))
		self.RShoulderTop.setObjectName(_fromUtf8("RShoulderTop"))
		self.LArmGroup = QtGui.QGroupBox(Form)
		self.LArmGroup.setGeometry(QtCore.QRect(790, 150, 211, 51))
		self.LArmGroup.setObjectName(_fromUtf8("LArmGroup"))
		self.LUArmHigh = QtGui.QPushButton(self.LArmGroup)
		self.LUArmHigh.setGeometry(QtCore.QRect(10, 20, 61, 23))
		self.LUArmHigh.setObjectName(_fromUtf8("LUArmHigh"))
		self.LElbowOut = QtGui.QPushButton(self.LArmGroup)
		self.LElbowOut.setGeometry(QtCore.QRect(80, 20, 61, 23))
		self.LElbowOut.setObjectName(_fromUtf8("LElbowOut"))
		self.LFArm = QtGui.QPushButton(self.LArmGroup)
		self.LFArm.setGeometry(QtCore.QRect(150, 20, 51, 23))
		self.LFArm.setObjectName(_fromUtf8("LFArm"))
		self.LHandGroup = QtGui.QGroupBox(Form)
		self.LHandGroup.setGeometry(QtCore.QRect(1010, 120, 151, 80))
		self.LHandGroup.setObjectName(_fromUtf8("LHandGroup"))
		self.LWristOut = QtGui.QPushButton(self.LHandGroup)
		self.LWristOut.setGeometry(QtCore.QRect(10, 20, 61, 23))
		self.LWristOut.setObjectName(_fromUtf8("LWristOut"))
		self.LHandOut = QtGui.QPushButton(self.LHandGroup)
		self.LHandOut.setGeometry(QtCore.QRect(80, 20, 61, 23))
		self.LHandOut.setObjectName(_fromUtf8("LHandOut"))
		self.LWristIn = QtGui.QPushButton(self.LHandGroup)
		self.LWristIn.setGeometry(QtCore.QRect(10, 50, 61, 23))
		self.LWristIn.setObjectName(_fromUtf8("LWristIn"))
		self.LHandIn = QtGui.QPushButton(self.LHandGroup)
		self.LHandIn.setGeometry(QtCore.QRect(80, 50, 61, 23))
		self.LHandIn.setObjectName(_fromUtf8("LHandIn"))
		self.HipsGroup = QtGui.QGroupBox(Form)
		self.HipsGroup.setGeometry(QtCore.QRect(430, 290, 341, 101))
		self.HipsGroup.setObjectName(_fromUtf8("HipsGroup"))
		self.WaistRFront = QtGui.QPushButton(self.HipsGroup)
		self.WaistRFront.setGeometry(QtCore.QRect(50, 60, 75, 23))
		self.WaistRFront.setObjectName(_fromUtf8("WaistRFront"))
		self.WaistLFront = QtGui.QPushButton(self.HipsGroup)
		self.WaistLFront.setGeometry(QtCore.QRect(200, 60, 75, 23))
		self.WaistLFront.setObjectName(_fromUtf8("WaistLFront"))
		self.WaistLBack = QtGui.QPushButton(self.HipsGroup)
		self.WaistLBack.setGeometry(QtCore.QRect(240, 30, 75, 23))
		self.WaistLBack.setObjectName(_fromUtf8("WaistLBack"))
		self.WaistCBack = QtGui.QPushButton(self.HipsGroup)
		self.WaistCBack.setGeometry(QtCore.QRect(90, 10, 75, 23))
		self.WaistCBack.setObjectName(_fromUtf8("WaistCBack"))
		self.WaistRBack = QtGui.QPushButton(self.HipsGroup)
		self.WaistRBack.setGeometry(QtCore.QRect(10, 30, 75, 23))
		self.WaistRBack.setObjectName(_fromUtf8("WaistRBack"))
		self.LLegGroup = QtGui.QGroupBox(Form)
		self.LLegGroup.setGeometry(QtCore.QRect(640, 400, 120, 171))
		self.LLegGroup.setObjectName(_fromUtf8("LLegGroup"))
		self.LThighSide = QtGui.QPushButton(self.LLegGroup)
		self.LThighSide.setGeometry(QtCore.QRect(44, 20, 61, 23))
		self.LThighSide.setObjectName(_fromUtf8("LThighSide"))
		self.LThighFront = QtGui.QPushButton(self.LLegGroup)
		self.LThighFront.setGeometry(QtCore.QRect(10, 60, 71, 23))
		self.LThighFront.setObjectName(_fromUtf8("LThighFront"))
		self.LKneeOut = QtGui.QPushButton(self.LLegGroup)
		self.LKneeOut.setGeometry(QtCore.QRect(40, 100, 61, 23))
		self.LKneeOut.setObjectName(_fromUtf8("LKneeOut"))
		self.LShin = QtGui.QPushButton(self.LLegGroup)
		self.LShin.setGeometry(QtCore.QRect(30, 140, 51, 23))
		self.LShin.setObjectName(_fromUtf8("LShin"))
		self.LFootGroup = QtGui.QGroupBox(Form)
		self.LFootGroup.setGeometry(QtCore.QRect(670, 570, 191, 151))
		self.LFootGroup.setObjectName(_fromUtf8("LFootGroup"))
		self.LToeTip = QtGui.QPushButton(self.LFootGroup)
		self.LToeTip.setGeometry(QtCore.QRect(60, 110, 75, 23))
		self.LToeTip.setObjectName(_fromUtf8("LToeTip"))
		self.LToeIn = QtGui.QPushButton(self.LFootGroup)
		self.LToeIn.setGeometry(QtCore.QRect(30, 80, 51, 23))
		self.LToeIn.setObjectName(_fromUtf8("LToeIn"))
		self.LToeOut = QtGui.QPushButton(self.LFootGroup)
		self.LToeOut.setGeometry(QtCore.QRect(110, 80, 51, 23))
		self.LToeOut.setObjectName(_fromUtf8("LToeOut"))
		self.LHeel = QtGui.QPushButton(self.LFootGroup)
		self.LHeel.setGeometry(QtCore.QRect(70, 10, 51, 23))
		self.LHeel.setObjectName(_fromUtf8("LHeel"))
		self.LAnkleOut = QtGui.QPushButton(self.LFootGroup)
		self.LAnkleOut.setGeometry(QtCore.QRect(100, 40, 61, 23))
		self.LAnkleOut.setObjectName(_fromUtf8("LAnkleOut"))
		self.RLegGroup = QtGui.QGroupBox(Form)
		self.RLegGroup.setGeometry(QtCore.QRect(440, 400, 120, 171))
		self.RLegGroup.setObjectName(_fromUtf8("RLegGroup"))
		self.RThighSide = QtGui.QPushButton(self.RLegGroup)
		self.RThighSide.setGeometry(QtCore.QRect(10, 20, 61, 23))
		self.RThighSide.setObjectName(_fromUtf8("RThighSide"))
		self.RThighFront = QtGui.QPushButton(self.RLegGroup)
		self.RThighFront.setGeometry(QtCore.QRect(40, 60, 71, 23))
		self.RThighFront.setObjectName(_fromUtf8("RThighFront"))
		self.RKneeOut = QtGui.QPushButton(self.RLegGroup)
		self.RKneeOut.setGeometry(QtCore.QRect(10, 100, 61, 23))
		self.RKneeOut.setObjectName(_fromUtf8("RKneeOut"))
		self.RShin = QtGui.QPushButton(self.RLegGroup)
		self.RShin.setGeometry(QtCore.QRect(30, 140, 51, 23))
		self.RShin.setObjectName(_fromUtf8("RShin"))
		self.RFootGroup = QtGui.QGroupBox(Form)
		self.RFootGroup.setGeometry(QtCore.QRect(340, 570, 191, 151))
		self.RFootGroup.setObjectName(_fromUtf8("RFootGroup"))
		self.RToeTip = QtGui.QPushButton(self.RFootGroup)
		self.RToeTip.setGeometry(QtCore.QRect(60, 110, 75, 23))
		self.RToeTip.setObjectName(_fromUtf8("RToeTip"))
		self.RToeIn = QtGui.QPushButton(self.RFootGroup)
		self.RToeIn.setGeometry(QtCore.QRect(110, 80, 51, 23))
		self.RToeIn.setObjectName(_fromUtf8("RToeIn"))
		self.RHeel = QtGui.QPushButton(self.RFootGroup)
		self.RHeel.setGeometry(QtCore.QRect(70, 10, 51, 23))
		self.RHeel.setObjectName(_fromUtf8("RHeel"))
		self.RAnkleOut = QtGui.QPushButton(self.RFootGroup)
		self.RAnkleOut.setGeometry(QtCore.QRect(10, 40, 61, 23))
		self.RAnkleOut.setObjectName(_fromUtf8("RAnkleOut"))
		self.RToeOut = QtGui.QPushButton(self.RFootGroup)
		self.RToeOut.setGeometry(QtCore.QRect(30, 80, 51, 23))
		self.RToeOut.setObjectName(_fromUtf8("RToeOut"))
		self.RArmGroup = QtGui.QGroupBox(Form)
		self.RArmGroup.setGeometry(QtCore.QRect(180, 150, 221, 51))
		self.RArmGroup.setObjectName(_fromUtf8("RArmGroup"))
		self.RUArmHigh = QtGui.QPushButton(self.RArmGroup)
		self.RUArmHigh.setGeometry(QtCore.QRect(140, 20, 71, 23))
		self.RUArmHigh.setObjectName(_fromUtf8("RUArmHigh"))
		self.RElbowOut = QtGui.QPushButton(self.RArmGroup)
		self.RElbowOut.setGeometry(QtCore.QRect(70, 20, 61, 23))
		self.RElbowOut.setObjectName(_fromUtf8("RElbowOut"))
		self.RFArm = QtGui.QPushButton(self.RArmGroup)
		self.RFArm.setGeometry(QtCore.QRect(10, 20, 51, 23))
		self.RFArm.setObjectName(_fromUtf8("RFArm"))
		self.RHandGroup = QtGui.QGroupBox(Form)
		self.RHandGroup.setGeometry(QtCore.QRect(30, 120, 151, 80))
		self.RHandGroup.setObjectName(_fromUtf8("RHandGroup"))
		self.RWristOut = QtGui.QPushButton(self.RHandGroup)
		self.RWristOut.setGeometry(QtCore.QRect(80, 20, 61, 23))
		self.RWristOut.setObjectName(_fromUtf8("RWristOut"))
		self.RWristIn = QtGui.QPushButton(self.RHandGroup)
		self.RWristIn.setGeometry(QtCore.QRect(80, 50, 61, 23))
		self.RWristIn.setObjectName(_fromUtf8("RWristIn"))
		self.RHandOut = QtGui.QPushButton(self.RHandGroup)
		self.RHandOut.setGeometry(QtCore.QRect(10, 20, 61, 23))
		self.RHandOut.setObjectName(_fromUtf8("RHandOut"))
		self.RHandIn = QtGui.QPushButton(self.RHandGroup)
		self.RHandIn.setGeometry(QtCore.QRect(10, 50, 61, 23))
		self.RHandIn.setObjectName(_fromUtf8("RHandIn"))
		
		self.ActorName = QtGui.QLineEdit(Form)
		self.ActorName.setGeometry(QtCore.QRect(20, 10, 113, 20))
		self.ActorName.setObjectName(_fromUtf8("ActorName"))
		self.ToolMode = QtGui.QComboBox(Form)
		self.ToolMode.setGeometry(QtCore.QRect(20, 40, 69, 22))
		self.ToolMode.setObjectName(_fromUtf8("ToolMode"))
		self.ToolMode.addItem(_fromUtf8(""))
		self.ToolMode.addItem(_fromUtf8(""))
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)


		buttonsList = Form.findChildren(QtGui.QPushButton)

		for button in buttonsList :
			button.clicked.connect(self.set_button_action)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Form", None))
		self.HeadGroup.setTitle(_translate("Form", "Head", None))
		self.HeadLeft.setText(_translate("Form", "Head L", None))
		self.HeadRight.setText(_translate("Form", "Head R", None))
		self.HeadFront.setText(_translate("Form", "Head F", None))
		self.HeadTop.setText(_translate("Form", "Head Top", None))
		self.ChestGroup.setTitle(_translate("Form", "Chest", None))
		self.ChestTop.setText(_translate("Form", "Chest Top", None))
		self.ChestLow.setText(_translate("Form", "Chest Low", None))
		self.BackGroup.setTitle(_translate("Form", "Back", None))
		self.BackRight.setText(_translate("Form", "Back Right", None))
		self.BackTop.setText(_translate("Form", "Back Top", None))
		self.BackLeft.setText(_translate("Form", "Back Left", None))
		self.LShoulderGroup.setTitle(_translate("Form", "LShoulder", None))
		self.LShoulderTop.setText(_translate("Form", "LShoulder T", None))
		self.LShoulderBack.setText(_translate("Form", "LShoulder B", None))
		self.RShoulderGroup.setTitle(_translate("Form", "RShoulder", None))
		self.RShoulderBack.setText(_translate("Form", "RShoulder B", None))
		self.RShoulderTop.setText(_translate("Form", "RShoulder T", None))
		self.LArmGroup.setTitle(_translate("Form", "LArm", None))
		self.LUArmHigh.setText(_translate("Form", "LUArmHigh", None))
		self.LElbowOut.setText(_translate("Form", "LElbowOut", None))
		self.LFArm.setText(_translate("Form", "LFArm", None))
		self.LHandGroup.setTitle(_translate("Form", "LHand", None))
		self.LWristOut.setText(_translate("Form", "LWristOut", None))
		self.LHandOut.setText(_translate("Form", "LHandOut", None))
		self.LWristIn.setText(_translate("Form", "LWristIn ", None))
		self.LHandIn.setText(_translate("Form", "LHandIn", None))
		self.HipsGroup.setTitle(_translate("Form", "Hips", None))
		self.WaistRFront.setText(_translate("Form", "WaistRFront", None))
		self.WaistLFront.setText(_translate("Form", "WaistLFront", None))
		self.WaistLBack.setText(_translate("Form", "WaistLBack", None))
		self.WaistCBack.setText(_translate("Form", "WaistCBack", None))
		self.WaistRBack.setText(_translate("Form", "WaistRBack", None))
		self.LLegGroup.setTitle(_translate("Form", "LLeg", None))
		self.LThighSide.setText(_translate("Form", "LThighSide", None))
		self.LThighFront.setText(_translate("Form", "LThighFront", None))
		self.LKneeOut.setText(_translate("Form", "LKneeOut", None))
		self.LShin.setText(_translate("Form", "LShin", None))
		self.LFootGroup.setTitle(_translate("Form", "LFoot", None))
		self.LToeTip.setText(_translate("Form", "LToeTip", None))
		self.LToeIn.setText(_translate("Form", "LToeIn", None))
		self.LToeOut.setText(_translate("Form", "LToeOut", None))
		self.LHeel.setText(_translate("Form", "LHeel", None))
		self.LAnkleOut.setText(_translate("Form", "LAnkleOut", None))
		self.RLegGroup.setTitle(_translate("Form", "RLeg", None))
		self.RThighSide.setText(_translate("Form", "RThighSide", None))
		self.RThighFront.setText(_translate("Form", "RThighFront", None))
		self.RKneeOut.setText(_translate("Form", "RKneeOut", None))
		self.RShin.setText(_translate("Form", "RShin", None))
		self.RFootGroup.setTitle(_translate("Form", "RFoot", None))
		self.RToeTip.setText(_translate("Form", "RToeTip", None))
		self.RToeIn.setText(_translate("Form", "RToeIn", None))
		self.RToeOut.setText(_translate("Form", "RToeOut", None))
		self.RHeel.setText(_translate("Form", "RHeel", None))
		self.RAnkleOut.setText(_translate("Form", "RAnkleOut", None))
		self.RArmGroup.setTitle(_translate("Form", "RArm", None))
		self.RUArmHigh.setText(_translate("Form", "RUArmHigh", None))
		self.RElbowOut.setText(_translate("Form", "RElbowOut", None))
		self.RFArm.setText(_translate("Form", "RFArm", None))
		self.RHandGroup.setTitle(_translate("Form", "RHand", None))
		self.RWristOut.setText(_translate("Form", "RWristOut", None))
		self.RHandOut.setText(_translate("Form", "RHandOut", None))
		self.RWristIn.setText(_translate("Form", "RWristIn ", None))
		self.RHandIn.setText(_translate("Form", "RHandIn", None))

		self.ToolMode.setItemText(0, _translate("Form", "Select", None))
		self.ToolMode.setItemText(1, _translate("Form", "Rename", None))

class FileReferenceTool(FBTool):

	def BuildLayout(self):
		x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft, "")
		y = FBAddRegionParam(0, FBAttachType.kFBAttachTop, "")
		w = FBAddRegionParam(0, FBAttachType.kFBAttachRight, "")
		h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom, "")
		self.AddRegion("main", "main", x, y, w, h)
		self.SetControl("main", self.mNativeWidgetHolder)

	def __init__(self, name):
		FBTool.__init__(self, name)
		self.mNativeWidgetHolder = NativeWidgetHolder()
		self.BuildLayout()
		self.StartSizeX = 1250
		self.StartSizeY = 750
		self.MinSizeX = 650
		self.MinSizeY = 425

gToolName = "MarkersLabel"

# Development? - need to recreate each time!!
gDEVELOPMENT = True

if gDEVELOPMENT:
	FBDestroyToolByName(gToolName)

if gToolName in FBToolList:
	tool = FBToolList[gToolName]
	ShowTool(tool)
else:
	tool = FileReferenceTool(gToolName)
	FBAddTool(tool)
	if gDEVELOPMENT:
		ShowTool(tool)
