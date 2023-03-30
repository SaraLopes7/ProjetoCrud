from conexaobd import ConexaoDB
from mysql.connector import Error



class cadastro:
    
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
            print('\n1. Visualizar livro')
            print('2. Alterar livro')
            print('3. Deletar livro')
            print('4. Sair\n')
            escolha2 = int(input("\nQual número deseja: "))
            
            if escolha2 == 1:
                APP.visualizar()
            
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
            
            
        

