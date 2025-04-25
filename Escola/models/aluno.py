class aluno:

   # def __init__ (self):
     
    def __init__ (self,nome, matricula,idade,turma):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.turma = turma
    
    def retornar_dados_aluno(self):
        return self.nome,self.matricula,self.idade,self.turma
        


#Nome, matricula

# "matricula": 123,
#       "nome": "Ana Souza",
#       "idade": 16,
#       "turma": "2A",
#       "notas": {
#         "Matemática": [8.5, 7.0, 9.0],
#         "Português": [9.0, 8.5, 8.0],
#         "História": [7.0, 6.5, 8.0]