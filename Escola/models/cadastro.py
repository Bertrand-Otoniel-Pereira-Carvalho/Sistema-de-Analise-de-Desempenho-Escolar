from utils.helpers import tentar_converter_para_int
from models.aluno import aluno
from models.nota import nota
import json

caminho =  'Escola/data/base_alunos.json'
instancia_classe_aluno = aluno
instancia_classe_nota = nota

with open (caminho, 'r', encoding='utf-8') as arquivo:
    alunos = json.load(arquivo)

matricula = 0
class cadastro:
    
    def __init__(self,cadastro_ou_nao):
        self.cadastro_ou_nao = cadastro_ou_nao
        if cadastro_ou_nao == 1:
            matricula = tentar_converter_para_int(input("Para confirmarmos sua identidade, digite sua matricula:\n"),"Matrícula")
            self.Verificar_Matricula(matricula)
    
    def Verificar_Matricula(self,matricula):
       
        matricula_valida = False
        while matricula_valida == False:
           
            for _matricula in alunos:
                if matricula == _matricula['matricula']:
                    print(f"Obrigado por acessar nosso sistema {_matricula['nome']}! Aproveite todas as funcionalidades")
                    matricula_valida = True
                    
                    #Armazenando informações deste aluno no arquivo/classe aluno

                    instancia_classe_aluno(nome=_matricula['nome'],matricula=_matricula['matricula'],idade=_matricula['idade'],turma=_matricula['turma'])

                    #Armazenando informações deste aluno no arquivo/classe nota

                    instancia_classe_nota(nota_matematica=_matricula['notas']['Matemática'],nota_portugues=_matricula['notas']['Português'],nota_historia=_matricula['notas']['História'])
                    break
            
            if matricula_valida == False:
                acao_que_usuario_deseja = 0
                acao_que_usuario_deseja = tentar_converter_para_int(input(("Sua matrícula não foi encontrada em nosso banco de dados.\n[1] Gostaria de tentar novamente\n[2] Gostaria de criar meu login\n\nDigite apenas o número correspondente: ")),"Valor")
                if acao_que_usuario_deseja == 1:
                    matricula_valida = True
                    self.Verificar_Matricula(tentar_converter_para_int(input("Digite sua matrícula: "),"Matrícula"))
                elif acao_que_usuario_deseja ==2:
                    print(1)#Criar função de realizar cadastro
                else:
                    print(2)
                    
instancia_cadastro = cadastro


    

# elif Cadastrado_ou_nao == 2:
#     print("3w")
# else:
#     print("3w")
