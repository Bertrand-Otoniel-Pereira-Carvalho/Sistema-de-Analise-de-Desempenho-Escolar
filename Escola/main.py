import json
import os
import tkinter as tk
import time
from utils.helpers import tentar_converter_para_int
from models.aluno import aluno
from models.nota import nota
from models.cadastro import cadastro

caminho =  'Escola/data/base_alunos.json'

with open (caminho, 'r', encoding='utf-8') as arquivo:
    alunos = json.load(arquivo)

#for aluno in alunos:
    #print(aluno['nome'])

os.system('cls')
print("Seja bem-vindo ao Sistema de Análise de Desempenho da Escola Genêsis")
Cadastrado_ou_nao = tentar_converter_para_int(input("\n[1] Já possuo login\n[2] Não possuo login\n\nDigite apenas o número correspondente: "),"Valor")
instancia_classe_cadastro = cadastro(Cadastrado_ou_nao)

Notas = instancia_classe_cadastro.retornar_instancias_nota_aluno() # nota matematica, nota portugues, nota história
Dados_aluno = instancia_classe_cadastro.retornar_dados_aluno() # Nome, matricula, idade, turma

instancia_classe_nota = nota(Notas[0],Notas[1],Notas[2]) 
instancia_classe_aluno = aluno(Dados_aluno[0],Dados_aluno[1],Dados_aluno[2],Dados_aluno[3])

time.sleep(0.01)
os.system("cls")
topico_principal = input(f"{Dados_aluno[0]}, qual tópico deseja abordar?\n\n[1] Notas\n[2] Aulas\n\n")
match topico_principal:
    case "1":
        os.system("cls")
        qual_topico_sobre_nota = input(f"{Dados_aluno[0]}, qual tópico sobre notas gostaria de vizualizar?\n\n[1] Boletim Completo \n[2] Média por disciplina \n[3] Média global \n[4] Aprovações/Reprovações\n")
        match qual_topico_sobre_nota:
            case "1":
                instancia_classe_nota.boletim_completo()
            case "2":
               print(instancia_classe_nota.media_materia(Notas[0]))
            case "3":
                print("j")
            case "4":
                print("j")
            case _:
                print("j")
    case "2":
        print("i")
    case _:
        print("ui")




