class Dad:
    basketBall = True

class Son(Dad):
    dance = 1
    guitar = True
    def doDance(self):
        return f'Yes I do dance {self.dance}.'

class GrandSon(Son):
    dance = 6
    basketBall = False
    guitar = False
    def doDance(self):
        return f'Jackson yeah!'\
         f'Yes I dance very incredibly {self.dance} times a day'
    
    def doHisDadPlayGuitar(self):
        return 'Yes, his dad play guitar' if Son.guitar else 'No, his dad don\'t play guitar'

    def doGuitar(self):
        return 'Yes, I play guitar' if self.guitar else 'No, I don\'t play guitar'
    
    def doHisGrandFatherPlayBasketball(self):
        return 'Yes, his grandfather play basketball' if Dad.basketBall else 'No, his grandfather don\'t play basketball'

darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.doDance())
print(harry.doGuitar())

print(harry.doHisDadPlayGuitar())
print(harry.doHisGrandFatherPlayBasketball())

print(harry.basketBall)



