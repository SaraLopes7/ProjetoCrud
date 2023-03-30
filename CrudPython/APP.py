from conexaobd import ConexaoDB
from mysql.connector import Error
import cadastroapp

class app:



    def _init_(self):
        pass

    def create(self):
        
        self.titulo = str(input('Digite o título do livro: '))
        self.autor = str(input('Digite o autor do livro: '))
        self.genero = str(input('Digite o gênero do livro: '))
        self.tpaginas = int(input('Digite o total de páginas do livro: '))
        self.lpaginas = int(input('Digite o número de páginas lidas: '))
        self.anotacoes = str(input('Digite as anotações sobre o livro: '))
        
        try:
            c = ConexaoDB() # faz a conexão com o banco 
            sql = f"insert into livro (titulo, autor, genero, tpaginas, lpaginas, anotacoes) "
            sql += f"values ('{self.titulo.upper()}','{self.autor.upper()}','{self.genero.upper()}','{self.tpaginas}','{self.lpaginas}','{self.anotacoes.upper()}')" # nomeia os campos da tabela os quais os valores serão inseridos
            c.executarDML(sql) # comando que jogo os dados para o banco de dados
        except Error as ex:
            print('Erro de conexão:', ex)
            
            
        print("\nDeseja fazer mais alguma ação?")
        escolha = str(input("\nDIGITE SIM OU NÃO:"))
        
        if escolha == "SIM" or "sim" or "Sim":
            print('\n1. Visualizar livro')
            print('2. Alterar livro')
            print('3. Deletar livro')
            print('4. Sair\n')
            escolha2 = int(input("\nQual número deseja: "))
            
            if escolha2 == 1:
                self.visualizar() 
            
            elif escolha2 == 2:
                self.alterar()
            
            elif escolha2 == 3:
                self.deletar()
            
            else:
                self.sair() 
                
        elif escolha == "NãO" or "não" or "Não" or "NAO" or "nao" or "Nao" :
            self.sair()
            
        else:
            print("você digitou algo errado! Tente outra vez")
            self.create()

    def visualizar(self):
        
        self.titulo = input("Digite o nome do livro que você quer visualizar: ")
        
        try:
            c = ConexaoDB()
            sql = f"select * from livro where titulo='{self.titulo.upper()}'" 
            c.executarDQL(sql)
            print("essas são as informações dos funcionários")
            c.desconectar()
            
        except Error as ex:
            print('Erro de conexão:', ex)
            
        print("Deseja fazer mais alguma ação?")
        escolha = str(input("SIM OU NÃO:"))
            
        if escolha == "SIM" or "sim" or "Sim":
            print('1. Visualizar livro')
            print('2. Criar um novo livro')
            print('3. Deletar um livro ')
            print('4. Sair\n')
            escolha2 = int(input("Qual número deseja: "))
                
            if escolha2 == 1:
                self.create() 
                
            elif escolha2 == 2:
                self.alterar()
                
            elif escolha2 == 3:
                self.deletar()
                
            else:
                self.sair() 
                    
        elif escolha == "NãO" or "não" or "Não" or "NAO" or "nao" or "Nao" :
            self.sair()
                
        else:
            print("você digitou algo errado! Tente outra vez")
            self.visualizar()
    
    def alterar(self):
        
        print("digite o que você vai querer atualizar de cada livro: ")
        print("1- paginas lidas")
        print("2- anotações")
        print("3- sair")
        escolha = int(input("escolha: "))
        
        if escolha == 1:
            
            self.lpaginas = int(input("Digite a quantidade de paginas lidas: "))
            self.titulo = str(input("\nEm qual livro?"))
            try:
                c = ConexaoDB() 
                sql = f"update livro " 
                sql += f"set lpaginas ='{self.lpaginas}' where titulo='{self.titulo.upper()}'"
                c.executarDML(sql)
                print("\ndados alterados com sucesso!")
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)
                
                
            print("Deseja fazer mais alguma ação?")
            escolha = str(input("SIM OU NÃO:"))
            
            if escolha == "SIM" or "sim" or "Sim":
                print('1. Visualizar livro')
                print('2. Criar um novo livro')
                print('3. Deletar um livro ')
                print('4. Sair\n')
                escolha2 = int(input("Qual número deseja: "))
                
                if escolha2 == 1:
                    self.visualizar() 
                
                elif escolha2 == 2:
                    self.create()
                
                elif escolha2 == 3:
                    self.deletar()
                
                else:
                    self.sair() 
                    
            elif escolha == "NãO" or "não" or "Não" or "NAO" or "nao" or "Nao" :
                self.sair()
                
            else:
                print("você digitou algo errado! Tente outra vez")
                self.alterar()
        
        elif escolha == 2:
            
            self.anotacoes = str(input("Digite a nova anotação que deseja colocar: "))
            self.titulo = str(input("\nEm qual livro?"))
            try:
                c = ConexaoDB() 
                sql = f"update livro " 
                sql += f"set anotacoes ='{self.anotacoes}' where titulo='{self.titulo.upper()}'"
                c.executarDML(sql)
                print("\ndados alterados com sucesso!")
                c.desconectar()
            except SystemError as ex:
                print('Erro de conexão:', ex)
                
            print("Deseja fazer mais alguma ação?")
            escolha = str(input("SIM OU NÃO:"))
            
            if escolha == "SIM" or "sim" or "Sim":
                print('1. Visualizar livro')
                print('2. Criar um novo livro')
                print('3. Deletar um livro ')
                print('4. Sair\n')
                escolha2 = int(input("Qual número deseja: "))
                
                if escolha2 == 1:
                    self.visualizar() 
                
                elif escolha2 == 2:
                    self.create()
                
                elif escolha2 == 3:
                    self.deletar()
                
                else:
                    self.sair() 
                    
            elif escolha == "NãO" or "não" or "Não" or "NAO" or "nao" or "Nao" :
                self.sair()
                
            else:
                print("você digitou algo errado! Tente outra vez")
                self.alterar()
            
        
        elif escolha == 3:
            self.sair()
        
        elif escolha == 4:
            self.menu()

    def deletar(self):
        
        print("Vamos deletar um livro!")
        self.titulo = str(input(("\nDigite o nome do livro que deseja deletar: ")))
             
        try:
            c = ConexaoDB() # faz a conexão com o banco 
            sql = f"delete from livro where titulo='{self.titulo.upper()}'" # define o que será feito na tabela funcionário
            c.executarDML(sql) # comando que jogo os dados para o banco de dados
            print("\ndados deletados com sucesso!")
            c.desconectar()
        except SystemError as ex:
            print('Erro de conexão:', ex)
            
        print("Deseja fazer mais alguma ação?")
        escolha = str(input("SIM OU NÃO:"))
        
        if escolha == "SIM" or "sim" or "Sim":
            print('1. Visualizar livro')
            print('2. Criar um novo livro')
            print('3. Alterar um livro ')
            print('4. Sair\n')
            escolha2 = int(input("Qual número deseja: "))
            
            if escolha2 == 1:
                self.visualizar() 
            
            elif escolha2 == 2:
                self.create()
            
            elif escolha2 == 3:
                self.alterar()
            
            else:
                self.sair() 
                
        elif escolha == "NãO" or "não" or "Não" or "NAO" or "nao" or "Nao" :
            self.sair()
            
        else:
            print("você digitou algo errado! Tente outra vez")
            self.deletar()
        
    def sair(self):
        print("você acabou de sair da aplicação!")

    def menu(self):
        
        print('\n\nCRUD de Livros\n')
        print('1. Criar um livro')
        print('2. Visualizar livro')
        print('3. Editar um livro existente')
        print('4. Deletar um livro')
        print('5. Sair\n')
        
        escolha1 = int(input("\nEscolha: "))

        if escolha1 == 1:
            # registrar consulta 
            self.create()
        
        elif escolha1 == 2:
            # função para ir visualizar as informações do livro
            self.visualizar()
                
        elif escolha1 == 3:
            # função para ir alterar as informações do livro
            self.alterar()
            
        elif escolha1 == 4:
            # deletar o livro
            self.deletar()
            
        elif escolha1 == 6:
            # deletar o livro
            cadastroapp.cadastro(self)
            
        elif escolha1 == 5:
            self.sair()
                    
        else:
            print("\nerro!")

    def cadastro(self):

        
        print("vamos criar seu cadastro!")
        self.nome_usuario = input("digite seu nome: ")
        self.email = input("digite seu email: ")
        self.usuario = input("digite seu usuario: ")
        self.senha = input("digite sua senha com números: ")
        
        try:
            c = ConexaoDB() # faz a conexão com o banco 
            sql = f"insert into cadastros (nome_usuario, email, usuario, senha) "
            sql += f"values ('{self.nome_usuario.upper()}','{self.email}','{self.usuario}','{self.senha}')" # nomeia os campos da tabela os quais os valores serão inseridos
            c.executarDML(sql) # comando que jogo os dados para o banco de dados
        except Error as ex:
            print('Erro de conexão:', ex)
            
            
        print("\nDeseja fazer mais alguma ação?")
        escolha = str(input("\nDIGITE SIM OU NÃO:"))
        
        if escolha == "SIM" or "sim" or "Sim":
            print('\n1. Menu livro')
            print('2. Sair\n')
            escolha2 = int(input("\nQual número deseja: "))
            
            if escolha2 == 1:
                self.menu()
            
            elif escolha2 == 2:
                self.sair()
            
            else:
                self.sair() 
                
        elif escolha == "NãO" or "não" or "Não" or "NAO" or "nao" or "Nao" :
            self.sair()
            
        else:
            print("você digitou algo errado! Tente outra vez")
            self.create()
            

object = app()
object.cadastro()