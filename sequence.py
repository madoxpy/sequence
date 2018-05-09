from pygame import *
from random import randint
from time import sleep

init()
res=[600,600]
window=display.set_mode(res)
clock=time.Clock()
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
yellow=(255,255,0)
lightred=(204,0,0)
lightblue=(51,153,255)
lightgreen=(153,255,51)
lightyellow=(255,255,102)
white=(255,255,255)
Font=font.SysFont("arial",20)

class Game(object):
	def __init__(self):
		self.level=1
		self.seq=self.randseq(self.level)
		self.userseq=[]
		self.mode='show'
	def randseq(self,level):
		tab=[]
		for i in range(level):
			tab.append(randint(1,4))
		return tab
	def show(self):
		for s in self.seq:
			if s==1:
				draw.rect(window,lightred,Rect(90,90,170,170),0)
				#mixer.music.load('c.wav')
				mixer.Channel(0).play(mixer.Sound('c.wav'))
			if s==2:
				draw.rect(window,lightblue,Rect(340,90,170,170),0)
				#mixer.music.load('d.wav')
				mixer.Channel(1).play(mixer.Sound('d.wav'))
			if s==3:
				draw.rect(window,lightgreen,Rect(90,340,170,170),0)
				#mixer.music.load('e.wav')
				mixer.Channel(2).play(mixer.Sound('e.wav'))
			if s==4:
				draw.rect(window,lightyellow,Rect(340,340,170,170),0)
				#mixer.music.load('f.wav')
				mixer.Channel(3).play(mixer.Sound('f.wav'))
			#mixer.Channel(0).play(1)
			display.flip()
			sleep(0.1)
			#mixer.stop()
			self.draw()
			display.flip()
			sleep(0.5)
		self.mode='play'
	
	def play(self):
		if mouse.get_pressed()[0]:
			if mouse.get_pos()[0]>100 and mouse.get_pos()[0]<250 and mouse.get_pos()[1]>100 and mouse.get_pos()[1]<250:
				self.userseq.append(1)
				mixer.Channel(0).play(mixer.Sound('c.wav'))
			if mouse.get_pos()[0]>350 and mouse.get_pos()[0]<500 and mouse.get_pos()[1]>100 and mouse.get_pos()[1]<250:
				self.userseq.append(2)
				mixer.Channel(1).play(mixer.Sound('d.wav'))
			if mouse.get_pos()[0]>100 and mouse.get_pos()[0]<250 and mouse.get_pos()[1]>350 and mouse.get_pos()[1]<500:
				self.userseq.append(3)
				mixer.Channel(2).play(mixer.Sound('e.wav'))
			if mouse.get_pos()[0]>350 and mouse.get_pos()[0]<500 and mouse.get_pos()[1]>350 and mouse.get_pos()[1]<500:
				self.userseq.append(4)
				mixer.Channel(3).play(mixer.Sound('f.wav'))
			#mixer.music.play(1)
			sleep(0.5)
		if len(self.userseq)==len(self.seq):
			self.mode='check'
	def check(self):
		win=True
		for i in range(len(self.seq)):
			if self.seq[i]!=self.userseq[i]:
				win=False
		if win:
			self.level=self.level+1
		else:
			self.level=1
		self.seq=self.randseq(self.level)
		self.userseq=[]
		self.mode='show'
		sleep(1.0)
	def draw(self):
		window.fill(black)
		draw.rect(window,red,Rect(100,100,150,150),0)
		draw.rect(window,blue,Rect(350,100,150,150),0)
		draw.rect(window,green,Rect(100,350,150,150),0)
		draw.rect(window,yellow,Rect(350,350,150,150),0)
		text = Font.render("Level "+str(self.level),True,white)
		window.blit(text,(260,290))

end=False
game=Game()
while not end:
	for z in event.get():
		if z.type==QUIT:
			end=True
	game.draw()
	display.flip()
	if game.mode=='show':
		sleep(1.0)
		game.show()
	elif game.mode=='play':
		game.play()
	elif game.mode=='check':
		game.check()
	clock.tick(20)
