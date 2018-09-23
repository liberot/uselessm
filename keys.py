#!/usr/bin/python
#coding=utf-8
import sys, time
from Quartz.CoreGraphics import *

'''
http://stackoverflow.com/questions/1817628/clicking-the-mouse-down-to-drag-objects-on-mac
http://stackoverflow.com/questions/18027342/how-can-i-call-cgeventkeyboardsetunicodestring-from-python
http://stackoverflow.com/questions/1918841/how-to-convert-ascii-character-to-cgkeycode
'''

def postMClickDownE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);

def postMClickUpE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);

def postMDragggedE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventLeftMouseDragged, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);

def postMMovedE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventMouseMoved, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);
 	
def postKeyE(key):
	e = CGEventCreateKeyboardEvent(None, 0, True);
	CGEventKeyboardSetUnicodeString(e, len(key), map(ord, key));
	# CGEventSetFlags(e, kCGEventFlagMaskShift);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);

def postKeycodeE(code):
	e = CGEventCreateKeyboardEvent(None, code, True);	
	CGEventPost(kCGHIDEventTap, e);
	e = CGEventCreateKeyboardEvent(None, code, False);	
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);

def postSearchSCE():
	e = CGEventCreateKeyboardEvent(None, 49, True);
	CGEventSetFlags(e, kCGEventFlagMaskCommand);
	CGEventPost(kCGHIDEventTap, e);
	e = CGEventCreateKeyboardEvent(None, 49, False);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);

def postGoToFolderSCE():
	e = CGEventCreateKeyboardEvent(None, 5, True);
	CGEventSetFlags(e, kCGEventFlagMaskShift|kCGEventFlagMaskCommand);
	CGEventPost(kCGHIDEventTap, e);
	e = CGEventCreateKeyboardEvent(None, 5, False);
	CGEventPost(kCGHIDEventTap, e);
	time.sleep(0.1);
	
# stores mouse position	
e = CGEventCreate(None);
pos = CGEventGetLocation(e);

postMMovedE(30, 15);
postMClickDownE(30, 15);
postMClickUpE(30, 15);
time.sleep(1);

# posts go to folder shortcut event
# postGoToFolderSCE();

# resets mouse position
# postMMovedE(pos.x, pos.y);

postMMovedE(30, 220);
postMClickDownE(30, 220);
postMClickUpE(30, 220);
time.sleep(5);

# enters [ENTER]
postKeycodeE(52);

exit();