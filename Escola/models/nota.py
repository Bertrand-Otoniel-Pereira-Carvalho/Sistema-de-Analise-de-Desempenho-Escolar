class nota:

    def __init__ (self,nota_matematica,nota_portugues,nota_historia):
        self.nota_matematica = nota_matematica
        self.nota_portugues = nota_portugues
        self.nota_historia = nota_historia
        
    def retornar_notas_simples (self):
        return self.nota_matematica,self.nota_portugues,self.nota_historia

    def media_materia (self,nota):
        self.nota = nota
        contador = 0
        acumulador_notas = 0
        for i in nota:
            acumulador_notas = acumulador_notas+i
            contador +=1
        media = acumulador_notas/contador
        return media

    def boletim_completo(self):
        self.media_historia = self.media_materia(self.nota_historia)# Arrumar para não repetir isso tanto vezes shiuo
        self.media_matematica = self.media_materia(self.nota_matematica)# Arrumar para não repetir isso tanto vezes
        self.media_portugues = self.media_materia(self.nota_portugues)# Arrumar para não repetir isso tanto vezes
        print("\n\t\tBoletim Completo\n\n","Matéria\tNotas por bimestre\tMédia\n","Matemática\t",self.nota_matematica,f"\t{(round(self.media_matematica,2))}","\n","Português\t",self.nota_portugues,f"\t{(round(self.media_portugues,2))}""\n","História\t",self.nota_historia,f"\t{(round(self.media_historia,2))}")

    def exibe_medias(self):
        self.media_historia = self.media_materia(self.nota_historia)# Arrumar para não repetir isso tanto vezes
        self.media_matematica = self.media_materia(self.nota_matematica)# Arrumar para não repetir isso tanto vezes
        self.media_portugues = self.media_materia(self.nota_portugues)# Arrumar para não repetir isso tanto vezes
        print(f"\nMédia em matemática: {round(self.media_matematica,2)}\nMédia em português: {round(self.media_portugues)}\nMédia em história: {round(self.media_historia,2)}")

    def exibe_aprovaçoes(self):
        self.media_historia = self.media_materia(self.nota_historia) # Arrumar para não repetir isso tanto vezes
        self.media_matematica = self.media_materia(self.nota_matematica)# Arrumar para não repetir isso tanto vezes
        self.media_portugues = self.media_materia(self.nota_portugues)# Arrumar para não repetir isso tanto vezes
        lista_medias_notas = [self.media_matematica,self.media_portugues,self.media_historia]
      # for i in lista_medias_notas:
          #  if i  

    
    #def media_global (self): args e kargs ??
    

# [1] Boletim Completo 
# [2] Média por disciplina 
# [3] Média global 
# [4] Aprovações/Reprovações