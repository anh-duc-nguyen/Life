'''
Remake Conway's Game of Life
'''
# import numpy as np
class Gaia:
    def __init__(self,H,W):
        self.H = H
        self.W = W
        self.curr =[]
        self.clearNext()
        for i in range(self.H):
            line = []
            for j in range(self.W):
                p = Particle(i,j)
                line.append(p)
            self.curr.append(line)
    
    def clearNext(self):
        self.next =[[None for x in range( self.W )] for y in range( self.H )]
    
    def show(self):
        print ("--------------------")
        for i in self.curr:
            line =''
            for j in i:
                line += j.toString()
            print(line)
        print ("--------------------")
    
    def nextTick(self):
        for i in range (self.H):
            for j in range (self.W):
                self.next[i][j] = self.update(self.curr[i][j])
        
        self.curr = self.next
        self.clearNext()

    def update(self,aParticle):
        neighbors = aParticle.neighbors()
        hp = 0
        for n in neighbors:
            if n[0] in range(self.H) and n[1] in range(self.W):
                hp += self.curr[n[0]][n[1]].getState()
        if aParticle.alive():
            if hp in range(3,5):
                newParticle = Particle(aParticle.x,aParticle.y)
                newParticle.live()
                return newParticle
            else:
                newParticle = Particle(aParticle.x,aParticle.y)
                newParticle.kill()
                return newParticle
        else:
            if hp == 3:
                newParticle = Particle(aParticle.x,aParticle.y)
                newParticle.live()
                return newParticle
            else:
                newParticle = Particle(aParticle.x,aParticle.y)
                newParticle.kill()
                return newParticle


class Particle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = 0
    def toString(self):
        return str(self.state)
    
    def neighbors(self):
        a0 = self.x
        a1 = self.x - 1
        a2 = self.x + 1
        
        b0 = self.y
        b1 = self.y + 1
        b2 = self.y - 1

        return[
            (a0,b0),(a0,b1),(a0,b2),
            (a1,b0),(a1,b1),(a1,b2),
            (a2,b0),(a2,b1),(a2,b2) ]
    
    def getState(self):
        return self.state
    def alive(self):
        return self.state == 1
    def death(self):
        return self.state == 0
    def live(self):
        self.state = 1
    def kill(self):
        self.state = 0
