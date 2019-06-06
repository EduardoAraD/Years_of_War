class Castelo:
    def __init__(self, pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vidaMax = 1000
        self.vida = 1000
        self.defesa = 0
        
    def fortificar(self):#aumentar a defesa do castelo
        if self.defesa < 80 :
            self.defesa += 20
            
    def receberDano(self,dano):
        self.vida = self.vida - (dano * ((100-self.defesa)/100))
        if self.vida <= 0 :
            self.vida = 0
            return True
        return False
        
    def receberCura(self,cura):
        self.vida += cura
        if self.vida > self.vidaMax :
            self.vida = self.vidaMax
