class nota:

    def __init__ (self,nota_matematica,nota_portugues,nota_historia):
        self.nota_matematica = nota_matematica
        self.nota_portugues = nota_portugues
        self.nota_historia = nota_historia
    
    def media_materia (self,materia,nota):
        self.nota = nota
        self.materia = materia
        contador = 0
        for i in nota:
            acumulador_notas = i
            contador +=1
        media = acumulador_notas/contador
        return media
    
    #def media_global (self): args e kargs ??
    



# disciplina e valor