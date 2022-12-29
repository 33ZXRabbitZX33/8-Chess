import pygame,sys
import datetime

pygame.init()

WIDTH = 800
HEIGHT = 800
block = WIDTH/8

DISPLAYSURF = pygame.display.set_mode((WIDTH+300,HEIGHT))
pygame.display.set_caption("Chess")

bg1_img = pygame.image.load("brown dark.png")
bg1_img = pygame.transform.scale(bg1_img,(block,block))

bg2_img = pygame.image.load("brown light.png")
bg2_img = pygame.transform.scale(bg2_img,(block,block))

bg_right = pygame.image.load("bg_right.jpg")
bg_right = pygame.transform.scale(bg_right,(300,HEIGHT)) 

hes = 0.8
sizeb = block*hes
sizec = block*0.6
sizep = block*0.6

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BROWN = (207, 194, 157)
YELLOW = (196, 214, 58)
YELLOW2 = (213, 227, 102)
XAM = (120,120,120)

ls =['X1', 'M1', 'T1', 'Q1', 'K1', 'T1', 'M1', 'X1',
     't1', 't1', 't1', 't1', 't1', 't1', 't1', 't1', 
     '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', 
     't', 't', 't', 't', 't', 't', 't', 't', 
     'X', 'M', 'T', 'Q', 'K', 'T', 'M', 'X']


FPS = 60
fpsClock = pygame.time.Clock()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


rook_img = pygame.image.load("rook.png")
rook_img = pygame.transform.scale(rook_img,(sizeb,sizeb))

queen_img = pygame.image.load("queen.png")
queen_img = pygame.transform.scale(queen_img,(sizeb,sizeb))

king_img = pygame.image.load("king.png")
king_img = pygame.transform.scale(king_img,(sizeb,sizeb))

knight_img = pygame.image.load("knight.png")
knight_img = pygame.transform.scale(knight_img,(sizeb,sizeb))

bishop_img = pygame.image.load("bishop.png")
bishop_img = pygame.transform.scale(bishop_img,(sizeb,sizeb))

pawn_img = pygame.image.load("pawn.png")
pawn_img = pygame.transform.scale(pawn_img,(sizep,sizep))

#################################################

rook1_img = pygame.image.load("rook1.png")
rook1_img = pygame.transform.scale(rook1_img,(sizeb,sizeb))

queen1_img = pygame.image.load("queen1.png")
queen1_img = pygame.transform.scale(queen1_img,(sizeb,sizeb))

king1_img = pygame.image.load("king1.png")
king1_img = pygame.transform.scale(king1_img,(sizeb,sizeb))

knight1_img = pygame.image.load("knight1.png")
knight1_img = pygame.transform.scale(knight1_img,(sizeb,sizeb))

bishop1_img = pygame.image.load("bishop1.png")
bishop1_img = pygame.transform.scale(bishop1_img,(sizeb,sizeb))

pawn1_img = pygame.image.load("pawn1.png")
pawn1_img = pygame.transform.scale(pawn1_img,(sizep,sizep))

def BackGround():
    for i in range(64):
         a = i%8
         b = i//8
         if (not a%2 and not b%2) or (a%2 and b%2 ) :
            img = bg2_img
            DISPLAYSURF.blit(img,(block*a,block*b))
         else :
            img = bg1_img
            DISPLAYSURF.blit(img,(block*a,block*b))


def Draw(ls):
        for i in range(64):
            a = i%8
            b = i//8
            if ls[i] == "X":
                img = rook_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "Q":
                img = queen_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "K":
                img = king_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "M":       
                img = knight_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "T":          
                img = bishop_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "t":            
                img = pawn_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "X1":            
                img = rook1_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "Q1":    
                img = queen1_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "K1":              
                img = king1_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "M1":             
                img = knight1_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "T1":              
                img = bishop1_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
            if ls[i] == "t1":             
                img = pawn1_img
                size = img.get_size()
                DISPLAYSURF.blit(img,(block*a+(block-size[0])/2,block*b+(block-size[1])/2))
cas,cas1,cas2,cas3 = True,True,True,True
turn = True
c1 = True
class Current():
    def __init__(self):
        self.a = -1
        self.b = -1
        self.no = ""
        self.can = []
        self.active = [False for i in range(64)]
        self.last = [-1,-1,-1,-1]
    def choose(self,event,coc):
        global c1,turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            nex1 = coc[0]
            nex2 = coc[1] 
            if nex1 > 0 and nex1 < 800 and nex2 > 0 and nex2 < 800:
                ne1 = round(coc[0]//block)
                ne2 = round(coc[1]//block)  
                chec = ne1 + ne2*8
                if turn:
                    if len(ls[chec]) == 1 or len(ls[chec]) == 0:
                        self.a = round(coc[0]//block)
                        self.b = round(coc[1]//block)          
                        self.no = ls[self.a+self.b*8]             
                        if self.no != "":
                            c1 = False
                elif not turn:
                    if len(ls[chec]) == 2 or len(ls[chec]) == 0:
                        self.a = round(coc[0]//block)
                        self.b = round(coc[1]//block)          
                        self.no = ls[self.a+self.b*8]             
                        if self.no != "":
                            c1 = False
                else:
                    pass
            else:
                self.a = -1
                self.b = -1
       
    def rook(a,b):
                global cas,cas1,cas2,cas3
                can = []
                for i in range(1,8):
                    ox = a-i
                    oy = b
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  if ls[chec] == "K" and cas:
                                      can.append(chec)
                                      break
                                  else:
                                      break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    if ls[chec] == "K1" and cas2:
                                          can.append(chec)
                                          break
                                    else:
                                      break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass
                for i in range(1,8):
                    ox = a+i
                    oy = b
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  if ls[chec] == "K" and cas1:
                                      can.append(chec)
                                      break
                                  else:
                                      break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    if ls[chec] == "K1" and cas3:
                                          can.append(chec)
                                          break
                                    else:
                                      break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass
                        
                for i in range(1,8):
                    ox = a
                    oy = b-i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass
                       
                for i in range(1,8):
                    ox = a
                    oy = b+i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass   
                return can
    def knight(a,b):
        can = []
        for z in [-1,1]:
            for i in [-1,1]:
                ox = a + 2*z
                oy = b + 1*i
                chec = ox + oy*8
                if ox*oy<0 or ox > 7 or oy > 7:
                    continue
                else: 
                    if len(ls[a+b*8]) == 1:
                        if len(ls[chec]) == 0 or len(ls[chec]) == 2:
                            can.append(chec)
                    elif len(ls[a+b*8]) == 2:
                        if len(ls[chec]) == 0 or len(ls[chec]) == 1:
                            can.append(chec)
                    else:
                        pass
        for z in [-1,1]:
            for i in [-1,1]:
                ox = a + 1*z
                oy = b + 2*i
                chec = ox + oy*8
                if ox*oy<0 or ox > 7 or oy > 7:
                    continue
                else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0 or len(ls[chec]) == 2:
                                can.append(chec)
                        elif len(ls[a+b*8]) == 2:
                            if len(ls[chec]) == 0 or len(ls[chec]) == 1:
                                can.append(chec)
                        else:
                            pass
        return can
    def bishop(a,b):
        can = []
        for i in range(1,8):
                    ox = a+i
                    oy = b-i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass   
                        
        for i in range(1,8):
                    ox = a-i
                    oy = b+i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass      
                        
        for i in range(1,8):
                    ox = a-i
                    oy = b-i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass   
                       
        for i in range(1,8):
                    ox = a+i
                    oy = b+i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass                         
        return can
    def king(a,b):
        can = []
        for i in [-1,1]:
            ox = a + 1*i
            oy = b 
            chec = ox +  oy*8
            if ox*oy<0 or ox > 7 or oy > 7:
               continue
            else:
               if len(ls[a+b*8]) == 1:
                   if len(ls[chec]) == 0 or len(ls[chec]) == 2:
                       can.append(chec)
               elif len(ls[a+b*8]) == 2:
                     if len(ls[chec]) == 0 or len(ls[chec]) == 1:
                         can.append(chec)
               else:
                  pass     
            for z in [-1,1]:
                oz = ox 
                ob = b + 1*z
                chec = oz +  ob*8
                if oz*ob<0 or oz> 7 or ob > 7:
                     continue
                else:
                   if len(ls[a+b*8]) == 1:
                        if len(ls[chec]) == 0 or len(ls[chec]) == 2:
                            can.append(chec)
                   elif len(ls[a+b*8]) == 2:
                        if len(ls[chec]) == 0 or len(ls[chec]) == 1:
                            can.append(chec)
                   else:
                        pass 
        for i in [-1,1]:
            ox = a 
            oy = b + 1*i
            chec = ox +  oy*8
            if ox*oy<0 or ox > 7 or oy > 7:
               continue
            else:
               if len(ls[a+b*8]) == 1:
                   if len(ls[chec]) == 0 or len(ls[chec]) == 2:
                       can.append(chec)
               elif len(ls[a+b*8]) == 2:
                     if len(ls[chec]) == 0 or len(ls[chec]) == 1:
                         can.append(chec)
               else:
                  pass

        return can
    def queen(a,b):
                q1 = Current.bishop(a,b)
                can = []
                for i in range(1,8):
                    ox = a-i
                    oy = b
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass
                for i in range(1,8):
                    ox = a+i
                    oy = b
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:                
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass
                        
                for i in range(1,8):
                    ox = a
                    oy = b-i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass
                       
                for i in range(1,8):
                    ox = a
                    oy = b+i
                    chec = ox + 8*oy
                    if ox*oy<0 or ox > 7 or oy > 7:
                         break
                    else:
                        if len(ls[a+b*8]) == 1:
                            if len(ls[chec]) == 0:
                                can.append(chec)
                            elif len(ls[chec]) == 1:               
                                  break
                            elif len(ls[chec]) == 2:
                                  can.append(chec)
                                  break
                            else:
                                pass
                        elif len(ls[a+b*8]) == 2:
                              if len(ls[chec]) == 0:
                                can.append(chec)
                              elif len(ls[chec]) == 2:               
                                    break
                              elif len(ls[chec]) == 1:
                                    can.append(chec)
                                    break
                              else:
                                 pass
                        else:
                            pass   
                return q1 +can    
      
    def pawn(a,b):
        can = []
        for i in range(1):
            ox = a 
            oy = b - 1
            chec = ox +  oy*8            
            if ox*oy<0 or ox > 7 or oy > 7:
                continue
            else:                 
                if len(ls[chec]) == 0 :
                    can.append(chec) 
                else:
                    pass
                    
            for z in [-1,1]:
                oz = ox +1*z
                chec = oz + oy*8
                if oz*oy<0 or oz > 7 or oy > 7:
                    continue
                else:   
                    if len(ls[chec]) == 2 :
                        can.append(chec) 
                    else:
                        pass   
        if a+b*8 in range(48,56,1):
            can.append(a+(b-2)*8)

        return   can
    def pawn1(a,b):
        can = []
        for i in range(1):
            ox = a 
            oy = b + 1
            chec = ox +  oy*8            
            if ox*oy<0 or ox > 7 or oy > 7:
                continue
            else:                 
                if len(ls[chec]) == 0 :
                    can.append(chec) 
                else:
                    pass
                    
            for z in [-1,1]:
                oz = ox +1*z
                chec = oz + oy*8
                if oz*oy<0 or oz > 7 or oy > 7:
                    continue
                else:   
                    if len(ls[chec]) == 1 :
                        can.append(chec) 
                    else:
                        pass   
        if a+b*8 in range(8,16,1):
            can.append(a+(b+2)*8)

        return   can
                

    def move(self,event,coc,ls):  
         global c1,turn
         global cas,cas1,cas2,cas3
         def mov(s):
             global c1,turn
             if event.type == pygame.MOUSEBUTTONDOWN:
                    nex1 = round(coc[0]//block)
                    nex2 = round(coc[1]//block)  
                    chec = nex1 + nex2*8
                    if chec in self.can:
                        if s == "X" and ls[chec] == "K":
                            if self.a+self.b*8 == 56:
                                ls[self.a+self.b*8] = ""
                                self.last[0] = self.a
                                self.last[1] = self.b
                                ls[self.a+2+self.b*8] = "K"
                                ls[self.a+3+self.b*8] = s
                                ls[self.a+4+self.b*8] = ""
                                if ls[self.a+4+self.b*8] == "":      
                                    self.a = round(coc[0]//block)-1
                                    self.b = round(coc[1]//block) 

                                    self.last[2] = self.a
                                    self.last[3] = self.b
                                    turn = not turn
                                    c1 = True      
                                    self.can = []
                            else:
                                ls[self.a+self.b*8] = ""
                                self.last[0] = self.a
                                self.last[1] = self.b
                                ls[self.a-1+self.b*8] = "K"
                                ls[self.a-2+self.b*8] = s
                                ls[self.a-3+self.b*8] = ""
                                if ls[self.a-3+self.b*8] == "":      
                                    self.a = round(coc[0]//block)+1
                                    self.b = round(coc[1]//block) 

                                    self.last[2] = self.a
                                    self.last[3] = self.b
                                    turn = not turn
                                    c1 = True      
                                    self.can = []
                        if s == "X1" and ls[chec] == "K1":
                            if self.a+self.b*8 == 0:
                                ls[self.a+self.b*8] = ""
                                self.last[0] = self.a
                                self.last[1] = self.b
                                ls[self.a+2+self.b*8] = "K1"
                                ls[self.a+3+self.b*8] = s
                                ls[self.a+4+self.b*8] = ""
                                if ls[self.a+4+self.b*8] == "":      
                                    self.a = round(coc[0]//block)-1
                                    self.b = round(coc[1]//block) 

                                    self.last[2] = self.a
                                    self.last[3] = self.b
                                    turn = not turn
                                    c1 = True      
                                    self.can = []
                            else:
                                ls[self.a+self.b*8] = ""
                                self.last[0] = self.a
                                self.last[1] = self.b
                                ls[self.a-1+self.b*8] = "K1"
                                ls[self.a-2+self.b*8] = s
                                ls[self.a-3+self.b*8] = ""
                                if ls[self.a-3+self.b*8] == "":      
                                    self.a = round(coc[0]//block)+1
                                    self.b = round(coc[1]//block) 

                                    self.last[2] = self.a
                                    self.last[3] = self.b
                                    turn = not turn
                                    c1 = True      
                                    self.can = []

                    if chec in self.can:
                        ls[self.a+self.b*8] = ""
                        self.last[0] = self.a
                        self.last[1] = self.b
                        if ls[self.a+self.b*8] == "":
                            self.a = round(coc[0]//block)
                            self.b = round(coc[1]//block) 
                            ls[self.a+self.b*8] = s

                            self.last[2] = self.a
                            self.last[3] = self.b
                            turn = not turn
                            c1 = True      
                            self.can = []

                            print(self.a,self.b)
                            print(s)
                    else:
                        c1 = True
                        self.can = []
         
         if ls[56] == "":
             cas1 = False
         elif ls[63] == "":
             cas = False
         elif ls[60] == "":
             cas1 = False
             cas = False

         if ls[0] == "":
             cas3 = False
         elif ls[7] == "":
             cas2 = False
         elif ls[4] == "":
             cas2 = False
             cas3 = False

                
         

         if self.no == "X" or self.no == "X1":                     
                self.can = Current.rook(self.a,self.b)
                if self.no == "X" : mov("X")
                else : mov("X1")
         elif self.no == "M" or self.no == "M1":
                self.can = Current.knight(self.a,self.b)
                if self.no == "M" : mov("M")
                else : mov("M1")               
         elif self.no == "T" or self.no == "T1": 
                self.can = Current.bishop(self.a,self.b)
                if self.no == "T" : mov("T")
                else : mov("T1")                
         elif self.no == "K" or self.no == "K1":     
                self.can = Current.king(self.a,self.b)
                if self.no == "K" : mov("K")
                else : mov("K1")               
         elif self.no == "Q" or self.no == "Q1": 
                self.can = Current.queen(self.a,self.b)
                if self.no == "Q" : mov("Q")
                else : mov("Q1")            
         elif self.no == "t" :
                self.can = Current.pawn(self.a,self.b)
                mov("t")
         elif self.no == "t1" :
                self.can = Current.pawn1(self.a,self.b)
                mov("t1")
                          
         else:
             pass
pause = False
now = datetime.datetime.now().timestamp()
class Clock():
     def __init__(self):
         self.ti1 = 1800
         self.ti2 = 1800
         self.tinow = 0
     def draw(self):
          global turn,now,now2,pause

          now3 = datetime.datetime.now().timestamp()
          
          if now <= now3:
              now += 1
              self.tinow += -1
          if pause:
              self.tinow = 0

          if not turn:  
              self.ti1 += self.tinow
              self.tinow = 0
          elif  turn:
              self.ti2 += self.tinow
              self.tinow = 0
          else:
              pass
          
          hours = self.ti1 //3600
          mins = (self.ti1 //60)%60   
          secs = self.ti1 %60    

          font = pygame.font.SysFont("consolas",40)
          font = font.render("<{}:{}:{}>".format(hours,mins,secs),True,BROWN)
          font_size = font.get_size()
          DISPLAYSURF.blit(font,(WIDTH+(300-font_size[0])/2,100))

          hours2 = self.ti2 //3600
          mins2 = (self.ti2 //60)%60   
          secs2 = self.ti2 %60 

          font2 = pygame.font.SysFont("consolas",40)
          font2 = font2.render("<{}:{}:{}>".format(hours2,mins2,secs2),True,BROWN)
          font_size2 = font2.get_size()
          DISPLAYSURF.blit(font2,(WIDTH+(300-font_size2[0])/2,700-font_size2[1]))
                              

lsup = -1
def Gameplay(cl,cc):
    global c1,pause,lsup,ls
    global play,pau,lev,lev1,end,end1

    font_pause = pygame.font.SysFont("consolas",50)
    font_pause = font_pause.render("<PAUSE>",True,BROWN)
    font_size_pause = font_pause.get_size()
    x = WIDTH+(300-font_size_pause[0])/2
    y = (HEIGHT-font_size_pause[1])/2
    box_pause = pygame.Rect(x,y,font_size_pause[0],font_size_pause[1])  
    
      
    
    while True:
        coc = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if c1:
                cc.choose(event,coc)
            else:
                cc.move(event,coc,ls)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_pause.collidepoint(event.pos): 
                    pause = not pause
                    pau = True
                    play = False
                    return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(cc.can)             
                    

                    
                
        BackGround()
        DISPLAYSURF.blit(bg_right,(WIDTH,0))
        cl.draw()

        DISPLAYSURF.blit(font_pause,(box_pause.x,box_pause.y))
        
        pygame.draw.rect(DISPLAYSURF,YELLOW,(cc.last[0]*block,cc.last[1]*block,block,block))   
        pygame.draw.rect(DISPLAYSURF,YELLOW2,(cc.last[2]*block,cc.last[3]*block,block,block))         

        pygame.draw.rect(DISPLAYSURF,RED,(cc.a*block,cc.b*block,block,block),2)
        for io in cc.can:
            a = io %8 +0.5
            b = io //8 +0.5  
            if ls[io] == "":
                pygame.draw.circle(DISPLAYSURF,XAM,(a*block,b*block),20)
            else:
                pygame.draw.circle(DISPLAYSURF,XAM,(a*block,b*block),50,5)
                     
        Draw(ls) 

        for i in range(8):
            if ls[i] == "t":
                lsup = i
                pause = not pause
                lev = True
                play = False
                return
        for i in range(56,64):
            if ls[i] == "t1":
                lsup = i
                pause = not pause
                lev1 = True
                play = False
                return

        if "K1" not in ls or cl.ti1 == 0:
             pause = not pause
             end = True
             play = False
             return
        if "K" not in ls or cl.ti2 == 0:
             pause = not pause
             end1 = True
             play = False
             return
           
        pygame.display.update()
        fpsClock.tick(FPS)

def Pause(cl):
     global pause
     global play,pau

     font = pygame.font.SysFont("consolas",80)
     font = font.render("<PAUSE>",True,BROWN)
     font_size = font.get_size()

     font_pause = pygame.font.SysFont("consolas",50)
     font_pause = font_pause.render("<PAUSE>",True,BROWN)
     font_size_pause = font_pause.get_size()
     x = WIDTH+(300-font_size_pause[0])/2
     y = (HEIGHT-font_size_pause[1])/2
     box_pause = pygame.Rect(x,y,font_size_pause[0],font_size_pause[1])  

     while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_pause.collidepoint(event.pos): 
                    pause = not pause
                    play = True
                    pau = False
                    return           

         BackGround()
         DISPLAYSURF.blit(bg_right,(WIDTH,0))
         cl.draw()

         DISPLAYSURF.blit(font_pause,(box_pause.x,box_pause.y))

         Draw(ls) 
         
         DISPLAYSURF.blit(font,((WIDTH-font_size[0])/2,(HEIGHT-font_size[1])/2))

         pygame.display.update()
         fpsClock.tick(FPS)

def Level(cl):
     global pause,lsup   
     global play,pau,lev
     
     rook_img = pygame.image.load("rook.png")
     rook_img = pygame.transform.scale(rook_img,(sizec,sizec))

     queen_img = pygame.image.load("queen.png")
     queen_img = pygame.transform.scale(queen_img,(sizec,sizec))    
 
     knight_img = pygame.image.load("knight.png")
     knight_img = pygame.transform.scale(knight_img,(sizec,sizec))

     bishop_img = pygame.image.load("bishop.png")
     bishop_img = pygame.transform.scale(bishop_img,(sizec,sizec))

     rook_img_size = rook_img.get_size()
     queen_img_size = queen_img.get_size()
     knight_img_size = knight_img.get_size()
     bishop_img_size = bishop_img.get_size()

     x = WIDTH+30
     y = 500
     box_rook = pygame.Rect(x,y,rook_img_size[0],rook_img_size[1])  

     x += sizec
     box_knight = pygame.Rect(x,y,knight_img_size[0],knight_img_size[1])  

     x += sizec
     box_bishop = pygame.Rect(x,y,bishop_img_size[0],bishop_img_size[1])  

     x += sizec
     box_queen = pygame.Rect(x,y,queen_img_size[0],queen_img_size[1])  

     font_pause = pygame.font.SysFont("consolas",50)
     font_pause = font_pause.render("<PAUSE>",True,BROWN)
     font_size_pause = font_pause.get_size()
     x = WIDTH+(300-font_size_pause[0])/2
     y = (HEIGHT-font_size_pause[1])/2
     box_pause = pygame.Rect(x,y,font_size_pause[0],font_size_pause[1])  

     font_choose = pygame.font.SysFont("consolas",50)
     font_choose = font_choose.render("<CHOOSE>",True,RED)
     font_size_choose = font_choose.get_size()
     x = WIDTH+(300-font_size_choose[0])/2
     y = 600
     box_choose = pygame.Rect(x,y,font_size_choose[0],font_size_choose[1])  

     while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_rook.collidepoint(event.pos): 
                    ls[lsup] = "X"
                    pause = not pause
                    play = True
                    lev = False
                    return
                if box_knight.collidepoint(event.pos): 
                    ls[lsup] = "M"
                    pause = not pause
                    play = True
                    lev = False
                    return
                if box_bishop.collidepoint(event.pos): 
                    ls[lsup] = "T"
                    pause = not pause
                    play = True
                    lev = False
                    return
                if box_queen.collidepoint(event.pos): 
                    ls[lsup] = "Q"
                    pause = not pause
                    play = True
                    lev = False
                    return       

         BackGround()
         DISPLAYSURF.blit(bg_right,(WIDTH,0))
         cl.draw()

         DISPLAYSURF.blit(font_pause,(box_pause.x,box_pause.y))
         DISPLAYSURF.blit(font_choose,(box_choose.x,box_choose.y))

         DISPLAYSURF.blit(rook_img,(box_rook.x,box_rook.y))
         DISPLAYSURF.blit(knight_img,(box_knight.x,box_knight.y))
         DISPLAYSURF.blit(bishop_img,(box_bishop.x,box_bishop.y))
         DISPLAYSURF.blit(queen_img,(box_queen.x,box_queen.y))

         Draw(ls)         

         pygame.display.update()
         fpsClock.tick(FPS)
def Level1(cl):
     global pause,lsup   
     global play,pau,lev,lev1
     
     rook_img = pygame.image.load("rook1.png")
     rook_img = pygame.transform.scale(rook_img,(sizec,sizec))

     queen_img = pygame.image.load("queen1.png")
     queen_img = pygame.transform.scale(queen_img,(sizec,sizec))    
 
     knight_img = pygame.image.load("knight1.png")
     knight_img = pygame.transform.scale(knight_img,(sizec,sizec))

     bishop_img = pygame.image.load("bishop1.png")
     bishop_img = pygame.transform.scale(bishop_img,(sizec,sizec))

     rook_img_size = rook_img.get_size()
     queen_img_size = queen_img.get_size()
     knight_img_size = knight_img.get_size()
     bishop_img_size = bishop_img.get_size()

     x = WIDTH+30
     y = 300-sizec
     box_rook = pygame.Rect(x,y,rook_img_size[0],rook_img_size[1])  

     x += sizec
     box_knight = pygame.Rect(x,y,knight_img_size[0],knight_img_size[1])  

     x += sizec
     box_bishop = pygame.Rect(x,y,bishop_img_size[0],bishop_img_size[1])  

     x += sizec
     box_queen = pygame.Rect(x,y,queen_img_size[0],queen_img_size[1])  

     font_pause = pygame.font.SysFont("consolas",50)
     font_pause = font_pause.render("<PAUSE>",True,BROWN)
     font_size_pause = font_pause.get_size()
     x = WIDTH+(300-font_size_pause[0])/2
     y = (HEIGHT-font_size_pause[1])/2
     box_pause = pygame.Rect(x,y,font_size_pause[0],font_size_pause[1])  

     font_choose = pygame.font.SysFont("consolas",50)
     font_choose = font_choose.render("<CHOOSE>",True,RED)
     font_size_choose = font_choose.get_size()
     x = WIDTH+(300-font_size_choose[0])/2
     y = 200 - font_size_choose[1]
     box_choose = pygame.Rect(x,y,font_size_choose[0],font_size_choose[1])  

     while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_rook.collidepoint(event.pos): 
                    ls[lsup] = "X1"
                    pause = not pause
                    play = True
                    lev = False
                    return
                if box_knight.collidepoint(event.pos): 
                    ls[lsup] = "M1"
                    pause = not pause
                    play = True
                    lev = False
                    return
                if box_bishop.collidepoint(event.pos): 
                    ls[lsup] = "T1"
                    pause = not pause
                    play = True
                    lev = False
                    return
                if box_queen.collidepoint(event.pos): 
                    ls[lsup] = "Q1"
                    pause = not pause
                    play = True
                    lev = False
                    return       

         BackGround()
         DISPLAYSURF.blit(bg_right,(WIDTH,0))
         cl.draw()

         DISPLAYSURF.blit(font_pause,(box_pause.x,box_pause.y))
         DISPLAYSURF.blit(font_choose,(box_choose.x,box_choose.y))

         DISPLAYSURF.blit(rook_img,(box_rook.x,box_rook.y))
         DISPLAYSURF.blit(knight_img,(box_knight.x,box_knight.y))
         DISPLAYSURF.blit(bishop_img,(box_bishop.x,box_bishop.y))
         DISPLAYSURF.blit(queen_img,(box_queen.x,box_queen.y))

         Draw(ls)         

         pygame.display.update()
         fpsClock.tick(FPS)
def EndGame(cl,s1,s2):
     global pause
     global play,end

     font = pygame.font.SysFont("consolas",80)
     font = font.render("<"+s1+">",True,BROWN)
     font_size = font.get_size()

     font2 = pygame.font.SysFont("consolas",80)
     font2 = font2.render("<"+s2+">",True,BROWN)
     font2_size = font2.get_size()

     font_pause = pygame.font.SysFont("consolas",40)
     font_pause = font_pause.render("<Play again!>",True,BROWN)
     font_size_pause = font_pause.get_size()
     x = WIDTH+(300-font_size_pause[0])/2
     y = (HEIGHT-font_size_pause[1])/2
     box_pause = pygame.Rect(x,y,font_size_pause[0],font_size_pause[1])  


     while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_pause.collidepoint(event.pos):             
                    cl.ti1 = 1800
                    cl.ti2 = 1800
                  
                    pause = not pause
                   
                    return           

         BackGround()
         DISPLAYSURF.blit(bg_right,(WIDTH,0))
         cl.draw()

         DISPLAYSURF.blit(font_pause,(box_pause.x,box_pause.y))

         Draw(ls) 
         
         DISPLAYSURF.blit(font,((WIDTH-font_size[0])/2,(HEIGHT-font_size[1])/2+200))
         DISPLAYSURF.blit(font2,((WIDTH-font2_size[0])/2,(HEIGHT-font2_size[1])/2-200))

         pygame.display.update()
         fpsClock.tick(FPS)

def Reset(ls):
    ls = ['X1', 'M1', 'T1', 'Q1', 'K1', 'T1', 'M1', 'X1',
         't1', 't1', 't1', 't1', 't1', 't1', 't1', 't1', 
         '', '', '', '', '', '', '', '', 
             '', '', '', '', '', '', '', '', 
             '', '', '', '', '', '', '', '', 
             '', '', '', '', '', '', '', '', 
         't', 't', 't', 't', 't', 't', 't', 't', 
         'X', 'M', 'T', 'Q', 'K', 'T', 'M', 'X']
    return ls
         
play,pau,lev,lev1,end,end1 = True,False,False,False,False,False

def main():
    global ls,turn
    global play,pau,lev,lev1,end,end1
    global cas,cas1,cas2,cas3
    cl = Clock()
    cc = Current()  

    while True:
        if play:
            Gameplay(cl,cc)
        elif pau:
            Pause(cl)
        elif lev:
            Level(cl)
        elif lev1:
            Level1(cl)
        elif end:
            EndGame(cl,"Win","Lose")
            ls = Reset(ls)
            turn = True
            cc.last = [-1,-1,-1,-1]
            cas,cas1,cas2,cas3 = True,True,True,True
            play = True
            end = False
        elif end1:
            EndGame(cl,"Lose","Win")
            ls = Reset(ls)
            turn = True
            cas,cas1,cas2,cas3 = True,True,True,True
            cc.last = [-1,-1,-1,-1]
            play = True
            end = False
        else:
            pass

if __name__ == "__main__":
    main()