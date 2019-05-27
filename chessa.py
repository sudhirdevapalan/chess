# -*- coding: utf-8 -*-
import random
import datetime
import sys
import Tkinter
from Tkinter import *
import tkMessageBox
from PIL import Image,ImageTk
import PIL
import time
#import pdb;pdb.set_trace()
global draw,promo
global b,gx,gy,gv
b=[]
draw=0
promo=0

class board:
	occupied=[0,'w','b']
	rank=['pawn','bishop','knight','rook','queen','king']
	init=[0,1]
	enpass=[0,1]
	value=0
	attacker=0
	defense=0
	attack=0
	#global b
	def init(self,i,j):
		if i==6:
			self.rank='pawn'
			self.occupied='w'
			self.init=1
			self.enpass=0
			self.value=1
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=wpawn)
		elif i==1:
			self.rank='pawn'
			self.occupied='b'
			self.init=1
			self.enpass=0
			self.value=1
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=bpawn)
		elif i==7 and (j==0 or j==7):
			self.rank='rook'
			self.occupied='w'
			self.init=1
			self.enpass=0
			self.value=8
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=wrook)
		elif i==0 and (j==0 or j==7):
			self.rank='rook'
			self.occupied='b'
			self.init=1
			self.enpass=0
			self.value=8
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=brook)
		elif i==7 and (j==1 or j==6):
			self.rank='knight'
			self.occupied='w'
			self.init=1
			self.enpass=0
			self.value=4
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=wknight)
		elif i==0 and (j==1 or j==6):
			self.rank='knight'
			self.occupied='b'
			self.init=1
			self.enpass=0
			self.value=4
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=bknight)
		elif i==7 and (j==2 or j==5):
			self.rank='bishop'
			self.occupied='w'
			self.init=1
			self.enpass=0
			self.value=2
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=wbishop)
		elif i==0 and (j==2 or j==5):
			self.rank='bishop'
			self.occupied='b'
			self.init=1
			self.enpass=0
			self.value=2
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=bbishop)
		elif i==7 and j==3:
			self.rank='queen'
			self.occupied='w'
			self.init=1
			self.enpass=0
			self.value=16
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=wqueen)
		elif i==0 and j==3:
			self.rank='queen'
			self.occupied='b'
			self.init==1
			self.enpass=0
			self.value=16
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=bqueen)
		elif i==7 and j==4:
			self.rank='king'
			self.occupied='w'
			self.init=1
			self.enpass=0
			self.value=32
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=wking)
		elif i==0 and j==4:
			self.rank='king'
			self.occupied='b'
			self.init=1
			self.enpass=0
			self.value=32
			self.attacker=0
			self.defense=0
			self.attack=0
			b[i][j].configure(image=bking)
		else:
			self.rank=''
			self.occupied=0
			self.init=''
			self.enpass=''
			self.attacker=0
			self.defense=0
			self.value=0
			self.attack=0
	def score(self,i,j):						#Generate the variables needed to make decision, Provide multi dim array for gx and gy
		if self.occupied==0:
			self.value=0
		elif self.rank=='pawn':
			self.value=1
		elif self.rank=='bishop':
			self.value=2
		elif self.rank=='knight':
			self.value=3
		elif self.rank=='rook':
			self.value=4
		elif self.rank=='queen':
			self.value=5
		elif self.rank=='king':
			self.value=6
		if self.occupied=='b':
			self.attacker=box[i][j].assess(i,j,'b','w')
			self.defence=box[i][j].assess(i,j,'b','b')
			#self.attackf=box[i][j].attack(i,j,'b','w')
		elif self.occupied=='w':
			self.attacker=box[i][j].assess(i,j,'w','b')
			self.defence=box[i][j].assess(i,j,'w','w')
			#self.attackf=box[i][j].attack(i,j,'w','b')
		else:
			pass
	def disp1(self,i,j):										#Not used
		if i==0 and j==0:
			sys.stdout.write("     0        1        2        3        4        5        6        7")
		if j==0:
			sys.stdout.write("\n------------------------------------------------------------------------\n")
			sys.stdout.write(str(i))
		if self.occupied=='w':
			sys.stdout.write("|")
			if self.rank=='pawn':
				sys.stdout.write(" w-pawn ")
			elif self.rank=='rook':
				sys.stdout.write(" w-rook ")
			elif self.rank=='knight':
				sys.stdout.write("w-knight")
			elif self.rank=='bishop':
				sys.stdout.write("w-bishop")
			elif self.rank=='queen':
				sys.stdout.write("w-queen ")
			elif self.rank=='king':
				sys.stdout.write(" w-king ")
		elif self.occupied=='b':
			sys.stdout.write("|")
			if self.rank=='pawn':
				sys.stdout.write(" b-pawn ")
			elif self.rank=='rook':
				sys.stdout.write(" b-rook ")
			elif self.rank=='knight':
				sys.stdout.write("b-knight")
			elif self.rank=='bishop':
				sys.stdout.write("b-bishop")
			elif self.rank=='queen':
				sys.stdout.write("b-queen ")
			elif self.rank=='king':
				sys.stdout.write(" b-king ")
		else:
			sys.stdout.write("|        ")
		if j==7:
			sys.stdout.write("|")
		if i==7 and j==7:
			sys.stdout.write("\n------------------------------------------------------------------------")
			print("\n")
	def confirm(self,x1,y1,x2,y2,player):						#Check if move is valid, if so complete the coin move
		global b,spin,px,py,bb,draw,promo
		#print "here",player
		temp_occ=self.occupied
		temp_rank=self.rank
		temp_init=self.init
		prev_init=box[x1][y1].init
		prev_enpass=self.enpass
		self.init=0
		self.occupied=player
		self.enpass=box[x1][y1].enpass
		self.rank=box[x1][y1].rank
		box[x1][y1].occupied=0
		box[x1][y1].rank=''
		box[x1][y1].init=0
		box[x1][y1].enpass=0
		#print "solution ",king_locate(player)
		if king_locate(player)==1:
			#print "Cannot move there(Your king will be exposed)"
			tkMessageBox.showinfo("Alert","Your king is in danger!")
			box[x1][y1].occupied=player
			box[x1][y1].rank=self.rank
			box[x1][y1].init=prev_init
			self.occupied=temp_occ
			self.rank=temp_rank
			self.init=temp_init
			self.enpass=0
			return 0
		else:
			name=box[x2][y2].occupied+box[x2][y2].rank+".png"
			#print name
			photo1 = Image.open(name)
			photo=ImageTk.PhotoImage(photo1)
			b[x2][y2].config(image=photo)
			b[x2][y2].image=photo
			b[x1][y1].config(image=blank)
			b[x1][y1].image=blank
		if self.rank=='pawn' and (x2==0 or x2==7):
			promo=1
			px=x2
			py=y2
			spin=Spinbox(c,values=('queen','knight','rook','bishop'), state="readonly", width=10)
			spin.grid(row=8,column=0)
			bb=Button(c,text="Promote",command=accept)
			bb.grid(row=8,column=1)
		for i in range(8):
			for j in range(8):
				box[i][j].score(i,j)						#Assessing the game
				if box[i][j].enpass==2:						#enpass tracking
					box[i][j].enpass=1
				elif box[i][j].enpass==1:
					box[i][j].enpass=0
				else:
					box[i][j].enpass=0
		stale=0
		if player=='w':									#Check for stalemate scenario
			stale=stalemate('b')
		else:
			stale=stalemate('w')
		if stale==0:
			#tkMessageBox.showinfo("Game Over!","Stalemate!!")
			#time.sleep(1)
			#sys.exit(0)
			draw=1
		return 1

	def pawn_moves(self,player,x1,y1,x2,y2):						#Validating each coin move
		if player=='w':
			#print "ththytjhytj",x1,y2,box[x1][y2].enpass,box[x1][y2].occupied
			if self.init==1:
				if (x2==int(x1)-1 or x2==int(x1)-2) and y2==y1 and box[int(x2)][int(y2)].occupied==0:
					if x2==int(x1)-2:
						self.enpass=2
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif (y2==y1+1 or y2==y1-1) and x2==x1-1 and box[int(x2)][int(y2)].occupied=='b':
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1+1 and x2==x1-1 and box[x1][y2].occupied=='b' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1-1 and x2==x1-1 and box[x1][y2].occupied=='b' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				else:
					return 0
			else:
				if x2==(int(x1)-1) and y2==y1 and box[int(x2)][int(y2)].occupied==0:
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif (y2==(y1+1) or y2==(y1-1)) and x2==(x1-1) and (box[int(x2)][int(y2)].occupied=='b'):
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1+1 and x2==x1-1 and box[x1][y2].occupied=='b' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1-1 and x2==x1-1 and box[x1][y2].occupied=='b' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				else:
					return 0
		else:
			if self.init==1:
				if (x2==int(x1)+1 or x2==int(x1)+2) and y2==y1 and box[int(x2)][int(y2)].occupied==0:
					if x2==int(x1)+2:
						self.enpass=2
					return box[int(x2)][int(y2)].confirm(x1,y1,x2,y2,player)
					return 1
				elif (y2==y1+1 or y2==y1-1) and x2==x1+1 and box[int(x2)][int(y2)].occupied=='w':
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1+1 and x2==x1+1 and box[x1][y2].occupied=='w' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1-1 and x2==x1+1 and box[x1][y2].occupied=='w' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				else:
					return 0
			else:
				if x2==int(x1)+1 and y2==y1 and box[int(x2)][int(y2)].occupied==0:
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif (y2==y1+1 or y2==y1-1) and x2==x1+1 and box[int(x2)][int(y2)].occupied=='w':
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1+1 and x2==x1+1 and box[x1][y2].occupied=='w' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				elif y2==y1-1 and x2==x1+1 and box[x1][y2].occupied=='w' and box[x1][y2].rank=='pawn' and box[x1][y2].enpass>0:
					box[x1][y2].occupied=0
					box[x1][y2].rank=''
					box[x1][y2].enpass=0
					box[x1][y2].init=0
					b[x1][y2].config(image=blank)
					return box[x2][y2].confirm(x1,y1,x2,y2,player)
					return 1
				else:
					return 0

	def bishop_moves(self,player,x1,y1,x2,y2):
		if (max(x1,x2)-min(x1,x2))!=(max(y1,y2)-min(y1,y2)):
			return 0
		else:
			for i in range(min(x1,x2)+1,max(x1,x2)):
				for j in range(min(y1,y2),max(y1,y2)):
					if (max(i,x1)-min(i,x1))==(max(j,y1)-min(j,y1)):
						if box[i][j].occupied!=0:
							return 0
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			return 1

	def knight_moves(self,player,x1,y1,x2,y2):
		if (x2==x1+2 and y2==y1+1) or (x2==x1+2 and y2==y1-1) or (x2==x1+1 and y2==y1+2) or (x2==x1+1 and y2==y1-2) or (x2==x1-1 and y2==y1+2) or (x2==x1-1 and y2==y1-2) or (x2==x1-2 and y2==y1+1) or (x2==x1-2 and y2==y1-1):
			 return box[x2][y2].confirm(x1,y1,x2,y2,player)
			 return 1
		else:
			return 0
	def rook_moves(self,player,x1,y1,x2,y2):
		if x1!=x2 and y1!=y2:
			return 0
		if y1==y2 and x2>x1:
			for i in range(x1+1,x2):
				if box[i][y1].occupied!=0:
					return 0
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			#return 1
		elif y1==y2 and x2<x1:
			for i in range(x2+1,x1):
				if box[i][y1].occupied!=0:
					return 0
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			#return 1
		elif x1==x2 and y2>y1:
			for j in range(y1+1,y2):
				if box[x1][j].occupied!=0:
					return 0
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			#return 1
		elif x1==x2 and y2<y1:
			print "y2 ",y2,"y1 ",y1,"x1 ",x1
			for j in range(y2+1,y1):
				if box[x1][j].occupied!=0:
					return 0
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			#return 1

	def queen_moves(self,player,x1,y1,x2,y2):
		if x1==x2 or y1==y2:
			if y1==y2 and x2>x1:
				for i in range(x1+1,x2):
					if box[i][y1].occupied!=0:
						return 0
				return box[x2][y2].confirm(x1,y1,x2,y2,player)
				#return 1
			elif y1==y2 and x2<x1:
				for i in range(x2+1,x1):
					if box[i][y1].occupied!=0:
						return 0
				return box[x2][y2].confirm(x1,y1,x2,y2,player)
				#return 1
			elif x1==x2 and y2>y1:
				for j in range(y1+1,y2):
					if box[x1][j].occupied!=0:
						return 0
				return box[x2][y2].confirm(x1,y1,x2,y2,player)
				#return 1
			elif x1==x2 and y2<y1:
				#print "y2 ",y2,"y1 ",y1,"x1 ",x1
				for j in range(y2+1,y1):
					if box[x1][j].occupied!=0:
						return 0
				return box[x2][y2].confirm(x1,y1,x2,y2,player)
				#return 1
		elif (max(x1,x2)-min(x1,x2))==(max(y1,y2)-min(y1,y2)):
			for i in range(min(x1,x2)+1,max(x1,x2)):
				for j in range(min(y1,y2),max(y1,y2)):
					if (max(i,x1)-min(i,x1))==(max(j,y1)-min(j,y1)):
						if box[i][j].occupied!=0:
							return 0
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			#return 1
		else:
			return 0

	def king_moves(self,player,x1,y1,x2,y2):
		if max(y1,y2)-min(y1,y2)==2 and x1==x2 and king_locate(player)!=1 and box[x1][y1].init==1:		#Castling
			if box[x1][y1].king_check(x2,y2)==1:
				return 0
			if y2>y1:
				for j in range(y1+1,7):
					if box[x1][j].occupied!=0:
						return 0
				for j in range(y1+1,y2):
					print "######",x1,j
					if box[x1][y1].king_check(x1,j)==1:
						print "oo"
						return 0
			else:
				for j in range(1,y1-1):
					if box[x1][j].occupied!=0:
						return 0
				for j in range(y2,y1):
					print "######",x1,j
					if box[x1][y1].king_check(x1,j)==1:
						print "oo"
						return 0
			if y2>y1:
				print "Hello"
				if box[x1][y2+1].rank=='rook':
					if box[x1][y2+1].init==1:
						box[x2][y2].confirm(x1,y1,x2,y2,player)
						box[x2][y2-1].confirm(x1,7,x2,y2-1,player)
						return 1
					else:
						return 0
				elif box[x1][y2+2].rank=='rook':				#Not needed in normal chess
					if box[x1][y2+2].init==1:
						box[x2][y2].confirm(x1,y1,x2,y2,player)
						box[x2][y2-1].confirm(x1,7,x2,y2-1,player)
						return 1
					else:
						return 0
				else:
					return 0
			else:
				print "dvgrg"
				if box[x1][y2-1].rank=='rook':
					if box[x1][y2-1].init==1:
						box[x2][y2].confirm(x1,y1,x2,y2,player)
						box[x2][y2+1].confirm(x1,0,x2,y2+1,player)
						return 1
					else:
						return 0
				elif box[x1][y2-2].rank=='rook':				#Not needed in normal chess
					if box[x1][y2-2].init==1:
						box[x2][y2].confirm(x1,y1,x2,y2,player)
						box[x2][y2+1].confirm(x1,0,x2,y2+1,player)
						return 1
					else:
						return 0
				else:
					return 0
		elif max(x1,x2)-min(x1,x2)>1 or max(y1,y2)-min(y1,y2)>1:
			return 0
		else:
			return box[x2][y2].confirm(x1,y1,x2,y2,player)
			return 1

	def piece(self,player,x1,y1,x2,y2):					#3. Determine which coin has been selected
		if self.rank=='pawn':
			return self.pawn_moves(player,x1,y1,x2,y2)
		elif self.rank=='bishop':
			return self.bishop_moves(player,x1,y1,x2,y2)
		elif self.rank=='knight':
			return self.knight_moves(player,x1,y1,x2,y2)
		elif self.rank=='rook':
			return self.rook_moves(player,x1,y1,x2,y2)
		elif self.rank=='queen':
			return self.queen_moves(player,x1,y1,x2,y2)
		elif self.rank=='king':
			return self.king_moves(player,x1,y1,x2,y2)

	def check(self,x,y,player):						#First check,  If valid coin color is selected
		if self.occupied==player:
			return 1
		else:
			#print "Cannot select that ",self.occupied,self.rank
			return 0
	def validate(self,x1,y1,x2,y2,player):					#Second check,  If the destination of selected coin is valid
		if self.occupied==player:
			#print "Cannot place here"
			return 0
		else:
			return box[int(x1)][int(y1)].piece(player,int(x1),int(y1),int(x2),int(y2))
	def king_check(self,x,y):						#Variables ckx,cky denote the attacking piece location
		global ckx,cky
		if self.occupied=='w':
			try:
				if (box[sub(x,1)][sub(y,1)].occupied=='b' and box[sub(x,1)][sub(y,1)].rank=='pawn'):
					ckx=sub(x,1)
					cky=sub(y,1)
					return 1
			except:
				pass
			try:
				if (box[sub(x,1)][y+1].occupied=='b' and box[sub(x,1)][y+1].rank=='pawn'):
					ckx=sub(x,1)
					cky=y+1
					return 1
			except:
				pass
			block=0
			for i in reversed(range(x)):
				if box[i][y].occupied=='b' and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					ckx=i
					cky=y
					return 1
				elif box[i][y].occupied=='w':
					block=1
				elif box[i][y].occupied=='b':
					block=1
			for j in reversed(range(y)):
				if box[x][j].occupied=='b' and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					ckx=x
					cky=j
					return 1
				elif box[x][j].occupied=='w':
					block=1
				elif box[x][j].occupied=='b':
					block=1
			for i in range(x+1,8):
				if box[i][y].occupied=='b' and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					ckx=i
					cky=y
					return 1
				elif box[i][y].occupied=='w':
					block=1
				elif box[i][y].occupied=='b':
					block=1
			for j in range(y+1,8):
				if box[x][j].occupied=='b' and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					ckx=x
					cky=j
					return 1
				elif box[x][j].occupied=='w':
					block=1
				elif box[x][j].occupied=='b':
					block=1
			block=0
			for i in reversed(range(x)):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='b' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='w':
							block=1
						elif box[i][j].occupied=='b':
							block=1
			block=0
			for i in reversed(range(x)):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='b' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='w':
							block=1
						elif box[i][j].occupied=='b':
							block=1
			block=0
			for i in range(x+1,8):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='b' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='w':
							block=1
						elif box[i][j].occupied=='b':
							block=1
			block=0
			for i in range(x+1,8):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='b' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='w':
							block=1
						elif box[i][j].occupied=='b':
							block=1
			try:
				if (box[x+2][y+1].occupied=='b' and box[x+2][y+1].rank=='knight'):
					ckx=x+2
					cky=y+1
					return 1
			except:
				pass
			try:
				if (box[x+2][sub(y,1)].occupied=='b' and box[x+2][sub(y,1)].rank=='knight'):
					ckx=x+2
					cky=sub(y,1)
					return 1
			except:
				pass
			try:
				if (box[x+1][y+2].occupied=='b' and box[x+1][y+2].rank=='knight'):
					ckx=x+1
					cky=y+2
					return 1
			except:
				pass
			try:
				if (box[x+1][sub(y,2)].occupied=='b' and box[x+1][sub(y,2)].rank=='knight'):
					ckx=x+1
					cky=sub(y,2)
					return 1
			except:
				pass
			try:
				if (box[sub(x,1)][y+2].occupied=='b' and box[sub(x,1)][y+2].rank=='knight'):
					ckx=sub(x,1)
					cky=y+2
					return 1
			except:
				pass
			try:
				if  (box[sub(x,1)][sub(y,2)].occupied=='b' and box[sub(x,1)][sub(y,2)].rank=='knight'):
					ckx=sub(x,1)
					cky=sub(y,2)
					return 1
			except:
				pass
			try:
				if (box[sub(x,2)][y+1].occupied=='b' and box[sub(x,2)][y+1].rank=='knight'):
					ckx=sub(x,2)
					cky=y+1
					return 1
			except:
				pass
			try:
				if (box[sub(x,2)][sub(y,1)].occupied=='b' and box[sub(x,2)][sub(y,1)].rank=='knight'):
					ckx=sub(x,2)
					cky=sub(y,1)
					return 1
			except:
				pass
                        try:
                                if box[x+1][y].occupied=='b' and box[x+1][y].rank=='king':
					return 1
			except:
				pass
			try:
				if box[sub(x,1)][y].occupied=='b' and box[sub(x,1)][y].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x+1][y+1].occupied=='b' and  box[x+1][y+1].rank=='king':
					return 1
			except:
				pass
			try:
				if box[sub(x,1)][y+1].occupied=='b' and box[sub(x,1)][y+1].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x][y+1].occupied=='b' and box[x][y+1].rank=='king':
					return 1
			except:
				pass
			try:
				if box[sub(x,1)][sub(y,1)].occupied=='b' and box[sub(x,1)][sub(y,1)].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x+1][sub(y,1)].occupied=='b' and box[x+1][sub(y,1)].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x][sub(y,1)].occupied=='b' and box[x][sub(y,1)].rank=='king':
					return 1
			except:
				pass
                        return 0
		else:
			try:
				if (box[x+1][y+1].occupied=='w' and box[x+1][y+1].rank=='pawn'):
					ckx=x+1
					cky=y+1
					return 1
			except:
				pass
			try:
				if (box[x+1][sub(y,1)].occupied=='w' and box[x+1][sub(y,1)].rank=='pawn'):
					ckx=x+1
					cky=sub(y,1)
					return 1
			except:
				pass
			block=0
			for i in reversed(range(x)):
				if box[i][y].occupied=='w' and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					ckx=i
					cky=y
					return 1
				elif box[i][y].occupied=='b':
					block=1
				elif box[i][y].occupied=='w':
					block=1
			block=0
			for j in reversed(range(y)):
				if box[x][j].occupied=='w' and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					ckx=x
					cky=j
					return 1
				elif box[x][j].occupied=='b':
					block=1
				elif box[x][j].occupied=='w':
					block=1
			block=0
			for i in range(x+1,8):
				if box[i][y].occupied=='w' and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					ckx=i
					cky=y
					return 1
				elif box[i][y].occupied=='b':
					block=1
				elif box[i][y].occupied=='w':
					block=1
			block=0
			for j in range(y+1,8):
				if box[x][j].occupied=='w' and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					ckx=x
					cky=j
					return 1
				elif box[x][j].occupied=='b':
					block=1
				elif box[x][j].occupied=='w':
					block=1
			block=0
			for i in reversed(range(x)):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='w' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='b':
							block=1
						elif box[i][j].occupied=='w':
							block=1
			block=0
			for i in reversed(range(x)):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='w' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='b':
							block=1
						elif box[i][j].occupied=='w':
							block=1
			block=0
			for i in range(x+1,8):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='w' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='b':
							block=1
						elif box[i][j].occupied=='w':
							block=1
			block=0
			for i in range(x+1,8):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied=='w' and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							ckx=i
							cky=j
							return 1
						elif box[i][j].occupied=='b':
							block=1
						elif box[i][j].occupied=='w':
							block=1
			try:
				if (box[x+2][y+1].occupied=='w' and box[x+2][y+1].rank=='knight'):
					ckx=x+2
					cky=y+1
					return 1
			except:
				pass
			try:
				if (box[x+2][sub(y,1)].occupied=='w' and box[x+2][sub(y,1)].rank=='knight'):
					ckx=x+2
					cky=sub(y,1)
					return 1
			except:
				pass
			try:
				if (box[x+1][y+2].occupied=='w' and box[x+1][y+2].rank=='knight'):
					ckx=x+1
					cky=y+2
					return 1
			except:
				pass
			try:
				if (box[x+1][sub(y,2)].occupied=='w' and box[x+1][sub(y,2)].rank=='knight'):
					ckx=x+1
					cky=sub(y,2)
					return 1
			except:
				pass
			try:
				if (box[sub(x,1)][y+2].occupied=='w' and box[sub(x,1)][y+2].rank=='knight'):
					ckx=sub(x,1)
					cky=y+2
					return 1
			except:
				pass
			try:
				if  (box[sub(x,1)][sub(y,2)].occupied=='w' and box[sub(x,1)][sub(y,2)].rank=='knight'):
					ckx=sub(x,1)
					cky=sub(y,2)
					return 1
			except:
				pass
			try:
				if (box[sub(x,2)][y+1].occupied=='w' and box[sub(x,2)][y+1].rank=='knight'):
					ckx=sub(x,2)
					cky=y+1
					return 1
			except:
				pass
			try:
				if (box[sub(x,2)][sub(y,1)].occupied=='w' and box[sub(x,2)][sub(y,1)].rank=='knight'):
					ckx=sub(x,2)
					cky=sub(y,1)
					return 1
			except:
				pass
                        try:
                                if box[x+1][y].occupied=='w' and box[x+1][y].rank=='king':
					return 1
			except:
				pass
			try:
				if box[sub(x,1)][y].occupied=='w' and box[sub(x,1)][y].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x+1][y+1].occupied=='w' and  box[x+1][y+1].rank=='king':
					return 1
			except:
				pass
			try:
				if box[sub(x,1)][y+1].occupied=='w' and box[sub(x,1)][y+1].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x][y+1].occupied=='w' and box[x][y+1].rank=='king':
					return 1
			except:
				pass
			try:
				if box[sub(x,1)][sub(y,1)].occupied=='w' and box[sub(x,1)][sub(y,1)].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x+1][sub(y,1)].occupied=='w' and box[x+1][sub(y,1)].rank=='king':
					return 1
			except:
				pass
			try:
				if box[x][sub(y,1)].occupied=='w' and box[x][sub(y,1)].rank=='king':
					return 1
			except:
				pass
			return 0

	def assess(self,x,y,player,opp):							#Used to assess the defence and attacker values
		val=0
		if self.occupied==player:
			if player!=opp:
				try:
					if box[sub(x,1)][sub(y,1)].occupied==opp and box[sub(x,1)][sub(y,1)].rank=='pawn':
						val=val+1
				except:
					pass
				try:
					if box[sub(x,1)][y+1].occupied==opp and box[sub(x,1)][y+1].rank=='pawn':
						val=val+1
				except:
					pass
			else:
				try:
					if box[x+1][y+1].occupied==opp and box[x+1][y+1].rank=='pawn':
						val=val+1
				except:
					pass
				try:
					if box[x+1][sub(y,1)].occupied==opp and box[x+1][sub(y,1)].rank=='pawn':
						val=val+1
				except:
					pass
			block=0
			for i in reversed(range(x)):
				if box[i][y].occupied==opp and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[i][y].occupied==player:
					block=1
				elif box[i][y].occupied==opp:
					block=1
			for j in reversed(range(y)):
				if box[x][j].occupied==opp and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[x][j].occupied==player:
					block=1
				elif box[x][j].occupied==opp:
					block=1
			for i in range(x+1,8):
				if box[i][y].occupied==opp and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[i][y].occupied==player:
					block=1
				elif box[i][y].occupied==opp:
					block=1
			for j in range(y+1,8):
				if box[x][j].occupied==opp and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[x][j].occupied==player:
					block=1
				elif box[x][j].occupied==opp:
					block=1
			block=0
			for i in reversed(range(x)):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			block=0
			for i in reversed(range(x)):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			block=0
			for i in range(x+1,8):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			block=0
			for i in range(x+1,8):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			try:
				if (box[x+2][y+1].occupied==opp and box[x+2][y+1].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[x+2][sub(y,1)].occupied==opp and box[x+2][sub(y,1)].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[x+1][y+2].occupied==opp and box[x+1][y+2].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[x+1][sub(y,2)].occupied==opp and box[x+1][sub(y,2)].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[sub(x,1)][y+2].occupied==opp and box[sub(x,1)][y+2].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if  (box[sub(x,1)][sub(y,2)].occupied==opp and box[sub(x,1)][sub(y,2)].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[sub(x,2)][y+1].occupied==opp and box[sub(x,2)][y+1].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[sub(x,2)][sub(y,1)].occupied==opp and box[sub(x,2)][sub(y,1)].rank=='knight'):
					val=val+1
			except:
				pass
			return val
		else:
			if player!=opp:
				try:
					if box[x+1][y+1].occupied==opp and box[x+1][y+1].rank=='pawn':
						val=val+1
				except:
					pass
				try:
					if box[x+1][sub(y,1)].occupied==opp and box[x+1][sub(y,1)].rank=='pawn':
						val=val+1
				except:
					pass
			else:
				try:
					if box[sub(x,1)][sub(y,1)].occupied==opp and box[sub(x,1)][sub(y,1)].rank=='pawn':
						val=val+1
				except:
					pass
				try:
					if box[sub(x,1)][y+1].occupied==opp and box[sub(x,1)][y+1].rank=='pawn':
						val=val+1
				except:
					pass
			block=0
			for i in reversed(range(x)):
				if box[i][y].occupied==opp and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[i][y].occupied==player:
					block=1
				elif box[i][y].occupied==opp:
					block=1
			block=0
			for j in reversed(range(y)):
				if box[x][j].occupied==opp and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[x][j].occupied==player:
					block=1
				elif box[x][j].occupied==opp:
					block=1
			block=0
			for i in range(x+1,8):
				if box[i][y].occupied==opp and (box[i][y].rank=='queen' or box[i][y].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[i][y].occupied==player:
					block=1
				elif box[i][y].occupied==opp:
					block=1
			block=0
			for j in range(y+1,8):
				if box[x][j].occupied==opp and (box[x][j].rank=='queen' or box[x][j].rank=='rook') and block==0:
					val=val+1
					block=1
				elif box[x][j].occupied==player:
					block=1
				elif box[x][j].occupied==opp:
					block=1
			block=0
			for i in reversed(range(x)):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			block=0
			for i in reversed(range(x)):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			block=0
			for i in range(x+1,8):
				for j in reversed(range(y)):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			block=0
			for i in range(x+1,8):
				for j in range(y+1,8):
					if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0:
						if box[i][j].occupied==opp and (box[i][j].rank=='queen' or box[i][j].rank=='bishop'):
							val=val+1
							block=1
						elif box[i][j].occupied==player:
							block=1
						elif box[i][j].occupied==opp:
							block=1
			try:
				if (box[x+2][y+1].occupied==opp and box[x+2][y+1].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[x+2][sub(y,1)].occupied==opp and box[x+2][sub(y,1)].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[x+1][y+2].occupied==opp and box[x+1][y+2].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[x+1][sub(y,2)].occupied==opp and box[x+1][sub(y,2)].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[sub(x,1)][y+2].occupied==opp and box[sub(x,1)][y+2].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if  (box[sub(x,1)][sub(y,2)].occupied==opp and box[sub(x,1)][sub(y,2)].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[sub(x,2)][y+1].occupied==opp and box[sub(x,2)][y+1].rank=='knight'):
					val=val+1
			except:
				pass
			try:
				if (box[sub(x,2)][sub(y,1)].occupied==opp and box[sub(x,2)][sub(y,1)].rank=='knight'):
					val=val+1
			except:
				pass
			return val

	def attackf(self,x,y,player,opp):						#Pieces than can be attacked(incomplete)
		global gx,gy,gv								#gx,gy is used to identify the location of the pieces that can be attacked
		val=0
		gv1=-101
		if player=='w':
			try:
				if box[sub(x,1)][sub(y,1)].occupied==opp and self.rank=='pawn' and legal_move(x,y,sub(x,1),sub(y,1),player)==1:
					val=val+1
					if box[sub(x,1)][sub(y,1)].defence==0:
						gv1=box[sub(x,1)][sub(y,1)].value
					else:
						gv1=box[sub(x,1)][sub(y,1)].value-self.value
					if gv1>gv:
						gx=sub(x,1)
						gy=sub(y,1)
						gv=gv1
			except:
				pass
			try:
				if box[sub(x,1)][y+1].occupied==opp and self.rank=='pawn' and legal_move(x,y,sub(x,1),y+1,player)==1:
					val=val+1
					if box[sub(x,1)][y+1].defence==0:
						gv1=box[sub(x,1)][y+1].value
					else:
						gv1=box[sub(x,1)][y+1].value-self.value
					if gv1>gv:
						gx=sub(x,1)
						gy=y+1
						gv=gv1
			except:
				pass
		elif player=='b':
			try:
				if box[x+1][y+1].occupied==opp and self.rank=='pawn' and legal_move(x,y,x+1,y+1,player)==1:
					val=val+1
					if box[x+1][y+1].defence==0:
						gv1=box[x+1][y+1].value
					else:
						gv1=box[x+1][y+1].value-self.value
					if gv1>gv:
						gx=x+1
						gy=y+1
						gv=gv1
			except:
				pass
			try:
				if box[x+1][sub(y,1)].occupied==opp and self.rank=='pawn' and legal_move(x,y,x+1,sub(y,1),player)==1:
					val=val+1
					if box[x+1][sub(y,1)].defence==0:
						gv1=box[x+1][sub(y,1)].value
					else:
						gv1=box[x+1][sub(y,1)].value-self.value
					if gv1>gv:
						gx=x+1
						gy=sub(y,1)
						gv=gv1
			except:
				pass
		block=0
		for i in reversed(range(x)):
			if box[i][y].occupied==opp and (self.rank=='queen' or self.rank=='rook') and block==0 and legal_move(x,y,i,y,player)==1:
				val=val+1
				if box[i][y].defence==0:
					gv1=box[i][y].value
				else:
					gv1=box[i][y].value-self.value
				if gv1>gv:
					gx=i
					gy=y
					gv=gv1
				block=1
			elif box[i][y].occupied==player:
				block=1
			elif box[i][y].occupied==opp:
				block=1
		for j in reversed(range(y)):
			if box[x][j].occupied==opp and (self.rank=='queen' or self.rank=='rook') and block==0 and legal_move(x,y,x,j,player)==1:
				val=val+1
				if box[x][j].defence==0:
					gv1=box[x][j].value
				else:
					gv1=box[x][j].value-self.value
				if gv1>gv:
					gx=x
					gy=j
					gv=gv1
				block=1
			elif box[x][j].occupied==player:
				block=1
			elif box[x][j].occupied==opp:
				block=1
		for i in range(x+1,8):
			if box[i][y].occupied==opp and (self.rank=='queen' or self.rank=='rook') and block==0 and legal_move(x,y,i,y,player)==1:
				val=val+1
				if box[i][y].defence==0:
					gv1=box[i][y].value
				else:
					gv1=box[i][y].value-self.value
				if gv1>gv:
					gx=i
					gy=y
					gv=gv1
				block=1
			elif box[i][y].occupied==player:
				block=1
			elif box[i][y].occupied==opp:
				block=1
		for j in range(y+1,8):
			if box[x][j].occupied==opp and (self.rank=='queen' or self.rank=='rook') and block==0 and legal_move(x,y,x,j,player)==1:
				val=val+1
				if box[x][j].defence==0:
					gv1=box[x][j].value
				else:
					gv1=box[x][j].value-self.value
				if gv1>gv:
					gx=x
					gy=j
					gv=gv1
				block=1
			elif box[x][j].occupied==player:
				block=1
			elif box[x][j].occupied==opp:
				block=1
		block=0
		for i in reversed(range(x)):
			for j in reversed(range(y)):
				if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0 and legal_move(x,y,i,j,player)==1:	#Check bishop n queen moves(jumping)
					if box[i][j].occupied==opp and (self.rank=='queen' or self.rank=='bishop'):
						val=val+1
						print "b1"
						if box[i][j].defence==0:
							gv1=box[i][j].value
						else:
							gv1=box[i][j].value-self.value
						if gv1>gv:
							gx=i
							gy=j
							gv=gv1
						block=1
					elif box[i][j].occupied==player:
						block=1
					elif box[i][j].occupied==opp:
						block=1
				else:
					block=1
		block=0
		for i in reversed(range(x)):
			for j in range(y+1,8):
				if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0 and legal_move(x,y,i,j,player)==1:
					if box[i][j].occupied==opp and (self.rank=='queen' or self.rank=='bishop'):
						val=val+1
						print "b2"
						if box[i][j].defence==0:
							gv1=box[i][j].value
						else:
							gv1=box[i][j].value-self.value
						if gv1>gv:
							gx=i
							gy=j
							gv=gv1
						block=1
					elif box[i][j].occupied==player:
						block=1
					elif box[i][j].occupied==opp:
						block=1
				else:
					block=1
		block=0
		for i in range(x+1,8):
			for j in reversed(range(y)):
				if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0 and legal_move(x,y,i,j,player)==1:
					if box[i][j].occupied==opp and (self.rank=='queen' or self.rank=='bishop'):
						val=val+1
						print "b3"
						if box[i][j].defence==0:
							gv1=box[i][j].value
						else:
							gv1=box[i][j].value-self.value
						if gv1>gv:
							gx=i
							gy=j
							gv=gv1
						block=1
					elif box[i][j].occupied==player:
						block=1
					elif box[i][j].occupied==opp:
						block=1
				else:
					block=1
		block=0
		for i in range(x+1,8):
			for j in range(y+1,8):
				if (max(x,i)-min(x,i))==(max(y,j)-min(y,j)) and block==0 and legal_move(x,y,i,j,player)==1:
					if box[i][j].occupied==opp and (self.rank=='queen' or self.rank=='bishop'):
						val=val+1
						print "b4"
						if box[i][j].defence==0:
							gv1=box[i][j].value
						else:
							gv1=box[i][j].value-self.value
						if gv1>gv:
							gx=i
							gy=j
							gv=gv1
						block=1
					elif box[i][j].occupied==player:
						block=1
					elif box[i][j].occupied==opp:
						block=1
				else:
					block=1
		try:
			if (box[x+2][y+1].occupied==opp and self.rank=='knight') and legal_move(x,y,x+2,y+1,player)==1:
				val=val+1
				if box[x+2][y+1].defence==0:
					gv1=box[x+2][y+1].value
				else:
					gv1=box[x+2][y+1].value-self.value
				if gv1>gv:
					gx=x+2
					gy=y+1
					gv=gv1
		except:
			pass
		try:
			if (box[x+2][sub(y,1)].occupied==opp and self.rank=='knight') and legal_move(x,y,x+2,sub(y,1),player)==1:
				val=val+1
				if box[x+2][sub(y,1)].defence==0:
					gv1=box[x+2][sub(y,1)].value
				else:
					gv1=box[x+2][sub(y,1)].value-self.value
				if gv1>gv:
					gx=x+2
					gy=sub(y,1)
					gv=gv1
		except:
			pass
		try:
			if (box[x+1][y+2].occupied==opp and self.rank=='knight') and legal_move(x,y,x+1,y+2,player)==1:
				val=val+1
				if box[x+1][y+2].defence==0:
					gv1=box[x+1][y+2].value
				else:
					gv1=box[x+1][y+2].value-self.value
				if gv1>gv:
					gx=x+1
					gy=y+2
					gv=gv1
		except:
			pass
		try:
			if (box[x+1][sub(y,2)].occupied==opp and self.rank=='knight') and legal_move(x,y,x+1,sub(y,2),player)==1:
				val=val+1
				if box[x+1][sub(y,2)].defence==0:
					gv1=box[x+1][sub(y,2)].value
				else:
					gv1=box[x+1][sub(y,2)].value-self.value
				if gv1>gv:
					gx=x+1
					gy=sub(y,2)
					gv=gv1
		except:
			pass
		try:
			if (box[sub(x,1)][y+2].occupied==opp and self.rank=='knight') and legal_move(x,y,sub(x,1),y+2,player)==1:
				val=val+1
				if box[sub(x,1)][y+2].defence==0:
					gv1=box[sub(x,1)][y+2].value
				else:
					gv1=box[sub(x,1)][y+2].value-self.value
				if gv1>gv:
					gx=sub(x,1)
					gy=y+2
					gv=gv1
		except:
			pass
		try:
			if  (box[sub(x,1)][sub(y,2)].occupied==opp and self.rank=='knight') and legal_move(x,y,sub(x,1),sub(y,2),player)==1:
				val=val+1
				if box[sub(x,1)][sub(y,2)].defence==0:
					gv1=box[sub(x,1)][sub(y,2)].value
				else:
					gv1=box[sub(x,1)][sub(y,2)].value-self.value
				if gv1>gv:
					gx=sub(x,1)
					gy=sub(x,2)
					gv=gv1
		except:
			pass
		try:
			if (box[sub(x,2)][y+1].occupied==opp and self.rank=='knight') and legal_move(x,y,sub(x,2),y+1,player)==1:
				val=val+1
				if box[sub(x,2)][y+1].defence==0:
					gv1=box[sub(x,2)][y+1].value
				else:
					gv1=box[sub(x,2)][y+1].value-self.value
				if gv1>gv:
					gx=sub(x,2)
					gy=y+1
					gv=gv1
		except:
			pass
		try:
			if (box[sub(x,2)][sub(y,1)].occupied==opp and self.rank=='knight') and legal_move(x,y,sub(x,2),sub(y,1),player)==1:
				val=val+1
				if box[sub(x,2)][sub(y,1)].defence==0:
					gv1=box[sub(x,2)][sub(y,1)].value
				else:
					gv1=box[sub(x,2)][sub(y,1)].value-self.value
				if gv1>gv:
					gx=sub(x,2)
					gy=sub(x,1)
					gv=gv1
		except:
			pass
		return val

'''
def end():
	wking=0
	bking=0
	for i in range(8):
		for j in range(8):
			if box[i][j].rank=='king':
				if box[i][j].occupied=='w':
					wking=1
				else:
					bking=1
	if wking==0:
		tkMessageBox.showinfo("Game Over","Black wins!!")
		sys.exit(0)
		return 1
	elif bking==0:
		tkMessageBox.showinfo("Game Over","White wins!!")
		sys.exit(0)
		return 1
	else:
		return 0
'''
def sub(a,b):
	if a>=b:
		return a-b
	else:
		return 10

def disp():
	for i in range(8):
		for j in range(8):
			box[i][j].disp1(i,j)

def king_locate(player):								#Locate position of king-> return 1 if check
	for i in range(8):
		for j in range(8):
			if box[i][j].rank=='king' and box[i][j].occupied==player:
				#print i,j,box[i][j].king_check(i,j)
				return box[i][j].king_check(i,j)

def stalemate(player):
	for i in range(8):
		for j in range(8):
			if box[i][j].occupied==player:
				if box[i][j].rank=='pawn' and player=='b':
					try:
						if box[i+1][j].occupied==0:
							if legal_move(i,j,i+1,j,player)==1:
								return 1
							else:
								pass
					except:
						pass
					try:
						if box[i+1][j+1].occupied=='w':
							if legal_move(i,j,i+1,j+1,player)==1:
								return 1
							else:
								pass
					except:
						pass
					try:
						if box[i+1][j+1].occupied=='w':
							if legal_move(i,j,i+1,sub(j,1),player)==1:
								return 1
							else:
								pass
					except:
						pass
				elif box[i][j].rank=='pawn' and player=='w':
					try:
						if box[sub(i,1)][j].occupied==0:
							if legal_move(i,j,sub(i,1),j,player)==1:
								return 1
							else:
								pass
					except:
						pass
					try:
						if box[sub(i,1)][j+1].occupied=='b':
							if legal_move(i,j,sub(i,1),j+1,player)==1:
								return 1
							else:
								pass
					except:
						pass
					try:
						if box[sub(i,1)][sub(j,1)].occupied=='b':
							if legal_move(i,j,sub(i,1),sub(j,1),player)==1:
								return 1
							else:
								pass
					except:
						pass
				elif box[i][j].rank=='rook':
					if legal_move(i,j,i,j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i,sub(j,1),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,j,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),j,player)==1:
						return 1
					else:
						pass
				elif box[i][j].rank=='bishop':
					if legal_move(i,j,i+1,j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,sub(j,1),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),sub(j,1),player)==1:
						return 1
					else:
						pass
				elif box[i][j].rank=='queen' or box[i][j].rank=='king':
					if legal_move(i,j,i,j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i,sub(j,1),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,j,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),j,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,sub(j,1),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),sub(j,1),player)==1:
						return 1
					else:
						pass
				elif box[i][j].rank=='knight':
					if legal_move(i,j,sub(i,2),sub(j,1),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,2),j+1,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),sub(j,2),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,sub(i,1),j+2,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,sub(j,2),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+1,j+2,player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+2,sub(j,1),player)==1:
						return 1
					else:
						pass
					if legal_move(i,j,i+2,j+1,player)==1:
						return 1
					else:
						pass
	return 0

def legal_move(i,j,x,y,player):					#1 if move is legal
	try:
		if box[x][y].occupied!=player:
			temp_occ=box[x][y].occupied
			temp_rank=box[x][y].rank
			temp_init=box[x][y].init
			temp_enpass=box[x][y].enpass
			box[x][y].occupied=box[i][j].occupied
			box[x][y].rank=box[i][j].rank
			box[x][y].init=box[i][j].init
			box[x][y].enpass=box[i][j].enpass
			box[i][j].occupied=0
			box[i][j].rank=0
			box[i][j].init=0
			box[i][j].enpass=0
			if king_locate(player)==1:
				box[i][j].occupied=box[x][y].occupied
				box[i][j].rank=box[x][y].rank
				box[i][j].init=box[x][y].init
				box[i][j].enpass=box[x][y].enpass
				box[x][y].occupied=temp_occ
				box[x][y].rank=temp_rank
				box[x][y].init=temp_init
				box[x][y].enpass=temp_enpass
				return 0
			else:
				box[i][j].occupied=box[x][y].occupied
				box[i][j].rank=box[x][y].rank
				box[i][j].init=box[x][y].init
				box[i][j].enpass=box[x][y].enpass
				box[x][y].occupied=temp_occ
				box[x][y].rank=temp_rank
				box[x][y].init=temp_init
				box[x][y].enpass=temp_enpass
				return 1
	except:
		return 0

def accept():
	global spin,px,py,bb,promo
	promo=0
	print spin.get(),px,py
	box[px][py].rank=spin.get()
	if spin.get()=='Queen':
		box[px][py].value=16
	elif spin.get()=='knight':
		box[px][py].value=4
	elif spin.get()=='rook':
		box[px][py].value=8
	elif spin.get()=='bishop':
		box[px][py].value=2
	spin.grid_forget()
	bb.grid_forget()
	name=box[px][py].occupied+box[px][py].rank+".png"
	#print name
	photo1 = Image.open(name)
	photo=ImageTk.PhotoImage(photo1)
	b[px][py].config(image=photo)
	b[px][py].image=photo

def computer(player,opp):							#Automation
	global gx,gy,gv,ckx,cky								#First, see if the king is in check and evade if necessary(not done); Second, see if an important coin is in danger and without support and evade if needed(not done); Third, Attack the enemy coin if it is profitable(success); Else, Make a random move
	gv=-101
	av=-100
	if king_locate(player)==1:
		for i in range(8):								#Step 1
			for j in range(8):							#Moving the king
				if box[i][j].rank=='king' and box[i][j].occupied==player:
					x=i
					y=j
		try:
			if box[x+1][y].occupied!=player and legal_move(x,y,x+1,y,player)==1:
				box[x+1][y].confirm(x,y,x+1,y,player)
				return
		except:
			pass
		try:
			if box[sub(x,1)][y].occupied!=player and legal_move(x,y,sub(x,1),y,player)==1:
				box[sub(x,1)][y].confirm(x,y,sub(x,1),y,player)
				return
		except:
			pass
		try:
			if box[x+1][y+1].occupied!=player and legal_move(x,y,x+1,y+1,player)==1:
                                print x,y
				box[x+1][y+1].confirm(x,y,x+1,y+1,player)
				return
		except:
			pass
		try:
			if box[sub(x,1)][y+1].occupied!=player and legal_move(x,y,sub(x,1),y+1,player)==1:
				box[sub(x,1)][y+1].confirm(x,y,sub(x,1),y+1,player)
				return
		except:
			pass
		try:
			if box[x][y+1].occupied!=player and legal_move(x,y,x,y+1,player)==1:
				box[x][y+1].confirm(x,y,x,y+1,player)
				return
		except:
			pass
		try:
			if box[sub(x,1)][sub(y,1)].occupied!=player and legal_move(x,y,sub(x,1),sub(y,1),player)==1:
				box[sub(x,1)][sub(y,1)].confirm(x,y,sub(x,1),sub(y,1),player)
				return
		except:
			pass
		try:
			if box[x+1][sub(y,1)].occupied!=player and legal_move(x,y,x+1,sub(y,1),player)==1:
				box[x+1][sub(y,1)].confirm(x,y,x+1,sub(y,1),player)
				return
		except:
			pass
		try:
			if box[x][sub(y,1)].occupied!=player and legal_move(x,y,x,sub(y,1),player)==1:
				box[x][sub(y,1)].confirm(x,y,x,sub(y,1),player)
				return
		except:
			pass
		'''
		if x==ckx:								#Saving the king with a blocking coin(Start changes from here)********
			for i in range(min(x,ckx)+1,max(x,ckx)):
				
		elif y==cky:
			for i in range(min(y,cky)+1,max(y,cky)):
		else:
			pass
		'''
	for i in range(8):								#Step 3
		for j in range(8):
			if box[i][j].occupied==player:
				att=box[i][j].attackf(i,j,player,opp)
				if gv>av:
					av=gv						#ax,ay-> Destination location
					ax=gx						#px,py-> The location of coin to be moved
					ay=gy
					px=i
					py=j
	print att
	if av>=0:
		box[ax][ay].confirm(px,py,ax,ay,player)
                return



c=Tkinter.Tk()


wpawn1 = Image.open("wpawn.png")
bpawn1=Image.open("bpawn.png")
wrook1=Image.open("wrook.png")
brook1=Image.open("brook.png")
wknight1=Image.open("wknight.png")
bknight1=Image.open("bknight.png")
wbishop1=Image.open("wbishop.png")
bbishop1=Image.open("bbishop.png")
wqueen1=Image.open("wqueen.png")
bqueen1=Image.open("bqueen.png")
wking1=Image.open("wking.png")
bking1=Image.open("bking.png")
blank1=Image.open("blank.png")
'''
wpawn1 = wpawn1.resize((120, 120), PIL.Image.ANTIALIAS)
bpawn1 = bpawn1.resize((80, 80), PIL.Image.ANTIALIAS)
wrook1 = wrook1.resize((100, 100), PIL.Image.ANTIALIAS)
brook1 = brook1.resize((100, 100), PIL.Image.ANTIALIAS)
wknight1 = wknight1.resize((120, 120), PIL.Image.ANTIALIAS)
bknight1 = bknight1.resize((120, 120), PIL.Image.ANTIALIAS)
wbishop1 = wbishop1.resize((100, 100), PIL.Image.ANTIALIAS)
bbishop1 = bbishop1.resize((70, 100), PIL.Image.ANTIALIAS)
wqueen1 = wqueen1.resize((100, 100), PIL.Image.ANTIALIAS)
bqueen1 = bqueen1.resize((80, 100), PIL.Image.ANTIALIAS)
wking1 = wking1.resize((100, 100), PIL.Image.ANTIALIAS)
bking1 = bking1.resize((110, 110), PIL.Image.ANTIALIAS)
blank1 = blank1.resize((100, 100), PIL.Image.ANTIALIAS)

wpawn1.save("wpawn.png")
bpawn1.save("bpawn.png")
wrook1.save("wrook.png")
brook1.save("brook.png")
wknight1.save("wknight.png")
bknight1.save("bknight.png")
wbishop1.save("wbishop.png")
bbishop1.save("bbishop.png")
wqueen1.save("wqueen.png")
bqueen1.save("bqueen.png")
wking1.save("wking.png")
bking1.save("bking.png")
blank1.save("blank.png")
'''
wpawn=ImageTk.PhotoImage(wpawn1)
bpawn=ImageTk.PhotoImage(bpawn1)
wrook=ImageTk.PhotoImage(wrook1)
brook=ImageTk.PhotoImage(brook1)
wknight=ImageTk.PhotoImage(wknight1)
bknight=ImageTk.PhotoImage(bknight1)
wbishop=ImageTk.PhotoImage(wbishop1)
bbishop=ImageTk.PhotoImage(bbishop1)
wqueen=ImageTk.PhotoImage(wqueen1)
bqueen=ImageTk.PhotoImage(bqueen1)
wking=ImageTk.PhotoImage(wking1)
bking=ImageTk.PhotoImage(bking1)
blank=ImageTk.PhotoImage(blank1)


global cx,cy
def mouse(event):
	global cx,cy
	try:
		grid_info = event.widget.grid_info()
		cy=int(event.x)
		cx=int(event.y)
	except:
		return
	#print "click",cx,cy
c.bind("<Button-1>", mouse)

global turn
turn='w'
def mouse(event):
	global turn,cx,cy,draw,promo
	if promo==0:
		try:
			grid_info = event.widget.grid_info()
			#print (grid_info["row"],grid_info["column"] )
			x1=int(grid_info["row"])
			y1=int(grid_info["column"])
			t= (c.grid_location(event.x, event.y))
			#print c.bbox(box[0][0])
			y2=int(t[0])
			x2=int(t[1])
			yy=int(event.x)
			xx=int(event.y)
		except:
			return
		#print "click",cx,cy
		#print "drop",xx,yy
		#print event.x,event.y
		#print xx,yy
		if x2<0:							#Approximating cursor position
			x2=0
		if y2<0:
			y2=0
		while(xx<0):
			xx=xx+107
			x2=x2-1
		while(yy<0):
			yy=yy+107
			y2=y2-1
		x2=x1+x2
		y2=y1+y2
		if (x2>7) or (y2 >7) or (x2<0) or (y2 <0):
			print "Outside box"
		else:
			#print x1,y1
			#print x2,y2
			if turn=='w':				#Always start with white
				#turn='b'
				chk=0
				val=0
				chk=box[int(x1)][int(y1)].check(int(x1),int(y1),'w')
				#val=box[int(x2)][int(y2)].validate(int(x1),int(y1),int(x2),int(y2),'w')
				if chk==0:
					#tkMessageBox.showinfo("Invalid selection","Select the correct coin")
					print "Invalid selection. Select the correct coin"
				else:
					val=box[int(x2)][int(y2)].validate(int(x1),int(y1),int(x2),int(y2),'w')	#Player turn(White)
					#tkMessageBox.showinfo("Invalid move","Can't move there")
					if val==0:
						print "Invalid move. Can't move there"
					else:
						turn='b'
						kcheck=0
						kcheck=king_locate('b')
						if kcheck==1:
							tkMessageBox.showinfo("Alert","Check!")
							checkmate(x2,y2,'b')
						if draw==1 and kcheck!=1:
							tkMessageBox.showinfo("Game drawn","Stalemate!")
			computer('b','w')									#Computer turn(Black)
			turn='w'
			kcheck=0
			print "hello"
			kcheck=king_locate('w')
			if kcheck==1:
				tkMessageBox.showinfo("Alert","Check!")
				checkmate(x2,y2,'w')
			if draw==1 and kcheck!=1:
				tkMessageBox.showinfo("Game drawn","Stalemate!")
			else:
				print "Some problem"
				'''
				chk=0
				val=0
				chk=box[int(x1)][int(y1)].check(int(x1),int(y1),'b')
				if chk==0:
					#tkMessageBox.showinfo("Invalid selection","Select the correct coin")
					print "Invalid selection. Select the correct coin"
				else:
					val=box[int(x2)][int(y2)].validate(int(x1),int(y1),int(x2),int(y2),'b')
					#tkMessageBox.showinfo("Invalid move","Can't move there")
					if val==0:
						print "Invalid move. Can't move there"
					else:
						turn='w'
						kcheck=0
						kcheck=king_locate('w')
						if kcheck==1:
							tkMessageBox.showinfo("Alert","Check!")
							checkmate(x2,y2,'w')
						if draw==1 and kcheck!=1:
							tkMessageBox.showinfo("Game drawn","Stalemate!")
				'''



c.bind("<ButtonRelease-1>", mouse)

def checkmate(x1,y1,player):								#Check for checkmate
	print "inside"
	ck=1
	for i in range(8):
		for j in range(8):
			if box[i][j].rank=='king' and box[i][j].occupied==player:
				x2=i
				y2=j
	if legal_move(x2,y2,x2,y2+1,player)==1:			#Check if king can move
		ck=0
	else:
		pass
	if legal_move(x2,y2,x2,sub(y2,1),player)==1:
		ck=0
	else:
		pass
	if legal_move(x2,y2,x2+1,y2,player)==1:
		ck=0
	else:
		pass
	if legal_move(x2,y2,sub(x2,1),y2,player)==1:
		ck=0
	else:
		pass
	if legal_move(x2,y2,x2+1,y2+1,player)==1:
		ck=0
	else:
		pass
	if legal_move(x2,y2,x2+1,sub(y2,1),player)==1:
		ck=0
	else:
		pass
	if legal_move(x2,y2,sub(x2,1),y2+1,player)==1:
		ck=0
	else:
		pass
	if legal_move(x2,y2,sub(x2,1),sub(y2,1),player)==1:
		ck=0
	else:
		pass
	if box[x1][y1].king_check(x1,y1)==1:			#Check if the attacking coin can be captured
		ck=0
	else:
		pass
	if box[x1][y1].rank=='knight':				#Check if any coin can be brought in the way of the king and the attacker
		if box[x1][y1].king_check(x1,y1)==1:
			ck=0
		else:
			pass
	elif box[x1][y1].rank=='pawn':
		if box[x1][y1].king_check(x1,y1)==1:
			ck=0
		else:
			pass
	elif box[x1][y1].rank=='rook' and (max(x1,x2)-min(x1,x2)>1 and max(y1,y2)-min(y1,y2)>1):
		if box[x1][y1].king_check(x1,y1)==1:
			ck=0
		else:
			pass
		if x1==x2:
			for j in range(min(y1,y2),max(y1,y2)):
				if box[x1][j].king_check(x1,j)==1:
					ck=0
				else:
					pass
		elif y1==y2:
			for i in range(min(x1,x2),max(x1,x2)):
				if box[i][y1].king_check(i,y1)==1:
					ck=0
				else:
					pass
	elif box[x1][y1].rank=='bishop' and (max(x1,x2)-min(x1,x2)>1 and max(y1,y2)-min(y1,y2)>1):
		if box[x1][y1].king_check(x1,y1)==1:
			ck=0
		else:
			pass
		if x1<x2 and y1<y2:
			for i in reversed(range(min(x1,x2),max(x1,x2))):
				for j in reversed(range(min(y1,y2),max(y1,y2))):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							ck=0
						else:
							pass
		elif x1<x2 and y1>y2:
			for i in reversed(range(min(x1,x2),max(x1,x2))):
				for j in range(min(y1+1,y2),max(y1+1,y2)):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							ck=0
						else:
							pass
		elif x1>x2 and y1<y2:
			for i in range(min(x1+1,x2),max(x1+1,x2)):
				for j in reversed(range(min(y1,y2),max(y1,y2))):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							ck=0
						else:
							pass
		elif x1>x2 and y1>y2:
			for i in range(min(x1+1,x2),max(x1+1,x2)):
				for j in range(min(y1+1,y2),max(y1+1,y2)):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							ck=0
						else:
							pass
	elif box[x1][y1].rank=='queen' and (max(x1,x2)-min(x1,x2)>1 and max(y1,y2)-min(y1,y2)>1):
		if box[x1][y1].king_check(x1,y1)==1:
			ck=0
		else:
			pass
		if x1==x2:
			for j in range(min(y1,y2),max(y1,y2)):
				if box[x1][j].king_check(x1,j)==1:
					print "q1"
					ck=0
				else:
					pass
		elif y1==y2:
			for i in range(min(x1,x2),max(x1,x2)):
				if box[i][y1].king_check(i,y1)==1:
					print "q2"
					ck=0
				else:
					pass
		elif x1<x2 and y1<y2:
			for i in reversed(range(min(x1,x2),max(x1,x2))):
				for j in reversed(range(min(y1,y2),max(y1,y2))):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							print "q3"
							ck=0
						else:
							pass
		elif x1<x2 and y1>y2:
			for i in reversed(range(min(x1,x2),max(x1,x2))):
				for j in range(min(y1+1,y2),max(y1+1,y2)):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							print "q4"
							ck=0
						else:
							pass
		elif x1>x2 and y1<y2:
			for i in range(min(x1+1,x2),max(x1+1,x2)):
				for j in reversed(range(min(y1,y2),max(y1,y2))):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							print "q5"
							ck=0
						else:
							pass
		elif x1>x2 and y1>y2:
			for i in range(min(x1+1,x2),max(x1+1,x2)):
				for j in range(min(y1+1,y2),max(y1+1,y2)):
					if (max(x1,i)-min(x1,i))==(max(y1,j)-min(y1,j)):
						if box[i][j].king_check(i,j)==1:
							print "q6"
							ck=0
						else:
							pass
	if ck==1:
		if player=='w':
			tkMessageBox.showinfo("Game over!!","Checkmate! Black wins!!!")
		else:
			tkMessageBox.showinfo("Game over!!","Checkmate! White wins!!!")

for i in range(8):
	#global b
	b.append([])
	for j in range(8):
		b[i].append(j)
		b[i][j]=Button(c,image=blank,fg="green",bg="black",font=("Times New Roman",12),activebackground="gray",activeforeground="red",width=80,height=80)
		if j%2==0 and i%2==0:
			b[i][j].config(bg="white")
		if j%2!=0 and i%2!=0:
			b[i][j].config(bg="white")
		b[i][j].grid(row=i, column=j)

box=[]

for i in range(8):
	box.append([])
	for j in range(8):
		box[i].append(board())

for i in range(8):
	for j in range(8):
		box[i][j].init(i,j)


c.mainloop()



