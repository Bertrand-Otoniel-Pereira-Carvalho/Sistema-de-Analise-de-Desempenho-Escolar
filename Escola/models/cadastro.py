from utils.helpers import tentar_converter_para_int
from models.aluno import aluno
from models.nota import nota
import json
import os

caminho =  'Escola/data/base_alunos.json'

with open (caminho, 'r', encoding='utf-8') as arquivo:
    alunos = json.load(arquivo)

instancia_classe_aluno = aluno()
instancia_classe_nota = nota()

matricula = 0
class cadastro:
       
    def __init__(self,cadastro_ou_nao):
        self.cadastro_ou_nao = cadastro_ou_nao
        if cadastro_ou_nao == 1:
            matricula = tentar_converter_para_int(input("Para confirmarmos sua identidade, digite sua matricula:\n"),"Matrícula")
            self.Verificar_Matricula(matricula)
        elif cadastro_ou_nao == 2:
            self.criar_login() #lista para armazenar as infos e passar para construtores

    def Verificar_Matricula(self,matricula):
       
        matricula_valida = False
        while matricula_valida == False:
           
            for _matricula in alunos:
                if matricula == _matricula['matricula']:
                    print(f"Obrigado por acessar nosso sistema {_matricula['nome']}! Aproveite todas as funcionalidades")
                    matricula_valida = True
                    
                    #Armazenando informações deste aluno no arquivo/classe aluno
                    
                    instancia_classe_aluno.registrar_aluno(nome=_matricula['nome'],matricula=_matricula['matricula'],idade=_matricula['idade'],turma=_matricula['turma'])
                    #Armazenando informações deste aluno no arquivo/classe nota
                    instancia_classe_nota.notas(nota_matematica=_matricula['notas']['Matemática'],nota_portugues=_matricula['notas']['Português'],nota_historia=_matricula['notas']['História']) 
                    break
            
            if matricula_valida == False:
                acao_que_usuario_deseja = 0
                acao_que_usuario_deseja = tentar_converter_para_int(input(("\nSua matrícula não foi encontrada em nosso banco de dados.\n[1] Gostaria de tentar novamente\n[2] Gostaria de criar meu login\n\nDigite apenas o número correspondente: ")),"Valor")
                if acao_que_usuario_deseja == 1:
                    matricula_valida = True
                    self.Verificar_Matricula(tentar_converter_para_int(input("Digite sua matrícula: "),"Matrícula"))
                elif acao_que_usuario_deseja ==2:
                    matricula_valida = True
                    self.criar_login()
                else:
                    print("Valor digitado é inválido, tente novamente.")

    def criar_login (self):#,nome,matricula,idade,turma):
       caminhoCompleto = "C:/Users/gamer/Downloads/Sistema de Análise de Desempenho Escolar/Escola/data/base_alunos.json"
       nova_info = {"matricula":0,"nome":"","idade":"","turma":""}
       listaInfo = list(input("Digite, nesta ordem, seu nome, turma, idade e matrícula. Em uma mesma linha, separados por espaço em branco:\n").split(" "))
       listaIdadeMatricula = [int(listaInfo[x]) for x in range(2,len(listaInfo))]
       nova_info.update({"matricula": listaIdadeMatricula[1],"nome" : listaInfo[0],"idade":listaIdadeMatricula[0],"turma":listaInfo[1]})
       if os.path.exists(caminhoCompleto):
            with open(caminhoCompleto, "r", encoding="utf-8") as arquivo:
                try:
                    dados = json.load(arquivo)
                except json.JSONDecodeError:
                    dados = []
       else:
            dados = []
        # Adiciona a nova entrada
       dados.append(nova_info)
        # Sobrescreve o arquivo com a lista atualizada
       with open(caminhoCompleto, "w", encoding="utf-8") as arquivo:
             json.dump(dados, arquivo, indent=4, ensure_ascii=False)



instancia_cadastro = cadastro


