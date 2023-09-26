import os
import datetime

class Evento:
    def __init__(self, diretorio):
        self.diretorio = diretorio

        # Criação dos arquivos se não existirem
        for arquivo_nome in ['inscritos.txt', 'entradas.txt', 'saidas.txt']:
            arquivo_path = os.path.join(self.diretorio, arquivo_nome)
            if not os.path.exists(arquivo_path):
                open(arquivo_path, 'w').close()

    def realizar_inscricao(self):
        nome = input("Digite seu nome: ")
        matricula = input("Digite sua matrícula: ")
        email = input("Digite seu email: ")

        # Verificar se a matrícula já existe na lista de inscritos
        if not self.matricula_existe(matricula):
            with open(os.path.join(self.diretorio, 'inscritos.txt'), 'a') as arquivo:
                arquivo.write(f"{nome},{matricula},{email}\n")
            print("Inscrição realizada com sucesso!")
        else:
            print("Matrícula já existe!")

    def matricula_existe(self, matricula):
        with open(os.path.join(self.diretorio, 'inscritos.txt'), 'r') as arquivo:
            for linha in arquivo:
                _, matricula_existente, _ = linha.strip().split(',')
                if matricula == matricula_existente:
                    return True
        return False

    def listar_inscritos(self):
        with open(os.path.join(self.diretorio, 'inscritos.txt'), 'r') as arquivo:
            print("Lista de inscritos:")
            for linha in arquivo:
                nome, matricula, email = linha.strip().split(',')
                print(f"Nome: {nome}, Matrícula: {matricula}, Email: {email}")

    def registrar_entrada(self):
        matricula = input("Digite sua matrícula: ")

        # Verificar se a matrícula existe na lista de inscritos
        if self.matricula_existe(matricula):
            # Verificar se o usuário já registrou a entrada
            if not self.entrada_registrada(matricula):
                with open(os.path.join(self.diretorio, 'entradas.txt'), 'a') as arquivo:
                    data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    arquivo.write(f"{matricula},{data_hora}\n")
                print("Entrada registrada com sucesso!")
            else:
                print("Você já registrou a entrada!")
        else:
            print("Matrícula não encontrada!")

    def entrada_registrada(self, matricula):
        with open(os.path.join(self.diretorio, 'entradas.txt'), 'r') as arquivo:
            for linha in arquivo:
                matricula_existente, _ = linha.strip().split(',')
                if matricula == matricula_existente:
                    return True
        return False

    def registrar_saida(self):
        matricula = input("Digite sua matrícula: ")

        # Verificar se a matrícula existe na lista de inscritos
        if self.matricula_existe(matricula):
            # Verificar se o usuário já registrou a entrada
            if self.entrada_registrada(matricula):
                # Verificar se o usuário já registrou a saída
                if not self.saida_registrada(matricula):
                    with open(os.path.join(self.diretorio, 'saidas.txt'), 'a') as arquivo:
                        data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        arquivo.write(f"{matricula},{data_hora}\n")
                    print("Saída registrada com sucesso!")
                else:
                    print("Você já registrou a saída!")
            else:
                print("Você não registrou a entrada!")
        else:
            print("Matrícula não encontrada!")

    def saida_registrada(self, matricula):
        with open(os.path.join(self.diretorio, 'saidas.txt'), 'r') as arquivo:
            for linha in arquivo:
                matricula_existente, _ = linha.strip().split(',')
                if matricula == matricula_existente:
                    return True
        return False

# Diretório onde os arquivos serão salvos (Mudar para o seu diretório de preferência)
diretorio = r'C:\Users\paulo\Desktop'

# Criar uma instância da classe Evento
evento = Evento(diretorio)

# Menu principal do programa
while True:
    print("\nMenu:")
    print("1. Realizar inscrição no evento")
    print("2. Listar usuários inscritos")
    print("3. Registrar entrada no evento")
    print("4. Registrar saída do evento")
    print("5. Sair do programa")

    escolha = input("Digite a opção desejada: ")

    if escolha == '1':
        evento.realizar_inscricao()
    elif escolha == '2':
        evento.listar_inscritos()
    elif escolha == '3':
        evento.registrar_entrada()
    elif escolha == '4':
        evento.registrar_saida()
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
