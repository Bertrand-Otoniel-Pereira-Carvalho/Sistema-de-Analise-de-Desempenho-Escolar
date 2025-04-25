import json
import os
import tkinter as tk
from utils.helpers import tentar_converter_para_int
from models.aluno import aluno
from models.nota import nota
from models.cadastro import cadastro

caminho =  'Escola/data/base_alunos.json'
instancia_classe_aluno = aluno()
instancia_classe_nota = nota()
instancia_classe_cadastro = cadastro("")

with open (caminho, 'r', encoding='utf-8') as arquivo:
    alunos = json.load(arquivo)

#for aluno in alunos:
    #print(aluno['nome'])

os.system('cls')
print("Seja bem-vindo ao Sistema de Análise de Desempenho da Escola Genêsis")
Cadastrado_ou_nao = tentar_converter_para_int(input("\n[1] Já possuo login\n[2] Não possuo login\n\nDigite apenas o número correspondente: "),"Valor")
cadastro(Cadastrado_ou_nao)
#instancia_classe_nota.vizualizar_notas_simples()
# topico_principal = input("Qual tópico deseja vizualizar?\n\n[1] Notas\n[2]Aulas")
# match topico_principal:
#     case "1":
#         os.system("cls")
#         qual_topico_sobre_nota = input("Qual tópico sobre notas gostaria de vizualizar?\n\n[1] Boletim Completo \n[2] Média por disciplina \n[3] Média global \n[4] Aprovações/Reprovações")
#         match qual_topico_sobre_nota:
#             case "1":
#                 nota.media_materia()
#             case "2":
#                 print("j")
#             case "3":
#                 print("j")
#             case "4":
#                 print("j")
#             case _:
#                 print("j")
#     case "2":
#         print("i")
#     case _:
#         print("ui")

# _


