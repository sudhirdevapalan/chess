# -*- coding: utf-8 -*-
import random
import datetime
import sys
import Tkinter
from Tkinter import *
import tkMessageBox
from PIL import Image,ImageTk
import PIL
#import Image
#import ImageTk
#import PIL
#import time
#import pdb;pdb.set_trace()
global draw,promo
global b
b=[]
draw=0
promo=0

class board:
	occupied=[0,'w','b']
	rank=['pawn','bishop','knight','rook','queen','king']
	init=[0,1]
	enpass=[0,1]
	#global b
	def init(self,i,j):
		if i==6:
			self.rank='pawn'
			self.occupied='w'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=wpawn)
		elif i==1:
			self.rank='pawn'
			self.occupied='b'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=bpawn)
		elif i==7 and (j==0 or j==7):
			self.rank='rook'
			self.occupied='w'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=wrook)
		elif i==0 and (j==0 or j==7):
			self.rank='rook'
			self.occupied='b'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=brook)
		elif i==7 and (j==1 or j==6):
			self.rank='knight'
			self.occupied='w'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=wknight)
		elif i==0 and (j==1 or j==6):
			self.rank='knight'
			self.occupied='b'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=bknight)
		elif i==7 and (j==2 or j==5):
			self.rank='bishop'
			self.occupied='w'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=wbishop)
		elif i==0 and (j==2 or j==5):
			self.rank='bishop'
			self.occupied='b'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=bbishop)
		elif i==7 and j==3:
			self.rank='queen'
			self.occupied='w'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=wqueen)
		elif i==0 and j==3:
			self.rank='queen'
			self.occupied='b'
			self.init==1
			self.enpass=0
			b[i][j].configure(image=bqueen)
		elif i==7 and j==4:
			self.rank='king'
			self.occupied='w'
			self.init=1
			self.enpass=0
			b[i][j].configure(image=wking)
		elif i==0 and j==4:
			self.rank='king'
			self.occupied='b'
			self.init=1
			self.en