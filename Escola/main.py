import json
import os
import tkinter as tk
from utils.helpers import tentar_converter_para_int
from models.aluno import aluno
from models.nota import nota

caminho =  'Escola/data/base_alunos.json'
instancia_classe_aluno = aluno
instancia_classe_nota = nota


with open (caminho, 'r', encoding='utf-8') as arquivo:
    alunos = json.load(arquivo)

#for aluno in alunos:
    #print(aluno['nome'])

os.system('cls')
print("Seja bem-vindo ao Sistema de Análise de Desempenho da Escola Genêsis")
Cadastrado_ou_nao = tentar_converter_para_int(input("\n[1] Já possuo login\n[2] Não possuo login\n\nDigite apenas o número correspondente: "),"Valor")

if Cadastrado_ou_nao == 1:
    matricula = tentar_converter_para_int(input("Para confirmarmos sua identidade, digite sua matricula:\n"),"Matricula")
    def Verificar_Matricula(matricula):
        matricula_valida = False
        while not matricula_valida == True:
            for _matricula in alunos:
                if matricula == _matricula['matricula']:
                    print(f"Obrigado por acessar nosso sistema {_matricula['nome']}! Aproveite todas as funcionalidades")
                    matricula_valida = True

                    #Armazenando informações deste aluno no arquivo/classe aluno

                    instancia_classe_aluno(nome=_matricula['nome'],matricula=_matricula['matricula'],idade=_matricula['idade'],turma=_matricula['turma'])

                    #Armazenando informações deste aluno no arquivo/classe nota

                    instancia_classe_nota(nota_matematica=_matricula['notas']['Matemática'],nota_portugues=_matricula['notas']['Português'],nota_historia=_matricula['notas']['História'])
            if matricula_valida == False:
                print("Sua matrícula não foi encontrada em nosso banco de dados. Tente novamente.")
                matricula = tentar_converter_para_int(input("Digite sua matricula:\n"),"Matricula")        
    Verificar_Matricula(matricula)
    

elif Cadastrado_ou_nao == 2:
    print("3w")
else:
    print("3w")

