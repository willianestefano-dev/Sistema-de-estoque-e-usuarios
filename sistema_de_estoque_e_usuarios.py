import json
from datetime import date

#classe usuario------------------------
class Usuario:
    def __init__(self, login, senha, nome, data_nascimento, cpf, endereco, email, tipo):

        self._login = login
        self.set_senha(senha)
        self.set_nome(nome) 
        self.set_data_nascimento(data_nascimento)
        self.set_cpf(cpf)
        self.set_endereco(endereco)
        self.set_email(email)       
        self.set_tipo(tipo)

    #getter----------------------
    def get_login(self):
        return self._login
    
    def get_senha(self):
        return self._senha
    
    def get_nome(self):
        return self._nome
    
    def get_data_nascimento(self):
        return self._data_nascimento
    
    def get_cpf(self):
        return self._cpf
    
    def get_endereco(self):
        return self._endereco
    
    def get_email(self):
        return self._email
    
    def get_tipo(self):
        return self._tipo
    
    #setter----------------------
    def set_login(self, login):

        if not login.strip():
            print("Campo login vazio")
            return False
        return True
        
    #----------------------------
    def set_senha(self, senha):        
        
        if len(senha) != 6:
            print("Senha deve conter seis digitos")
            return False
        
        self._senha = senha
        return True
    
    #-----------------------------
    def set_nome(self, nome):

        if not nome.strip():
            print("Campo nome vazio")
            return False
        
        if not nome.replace(" ","").isalpha():
            print("Apenas letras")
            return False

        self._nome = nome
        return True
    
    #------------------------------
    def set_data_nascimento(self, data_nascimento):

        if len(data_nascimento) != 10:
            print("Data de nascimento invalida, digite dd/mm/aaaa")
        
        if "/" not in data_nascimento:
            print("Use / para separar as datas")
        
        self._data_nascimento = data_nascimento
        return True
    
    #------------------------------
    def set_cpf(self, cpf):
       
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF invalido, Digite apenas os 11 numeros sem ponto e traço")
            return False
        else:
            self._cpf = cpf
            return True    
    
    #-------------------------------    
    def set_endereco(self, endereco):

        if not endereco.strip():
            print("Campo nome vazio")
            return False     

        self._endereco = endereco
        return True
    
    #-------------------------------
    def set_email(self, email):

        if "@" not in email or ".com" not in email:
            print("Email invalido")
            return False
        
        self._email = email
        return True
    
    #------------------------------
    def set_tipo(self, tipo):
        
        if tipo in ['admin', 'adm']:
            self._tipo = 'admin'            
            return True
        
        elif tipo in ['funcionario', 'estoquista']:
            self._tipo = 'funcionario'            
            return True

        else:
            print("Usuario invalido")
            return False
        
    #metodo to dict-------------------
    def to_dict(self):
        return {

            'login': self._login,
            'senha': self._senha,
            'nome': self._nome,
            'data_nascimento': self._data_nascimento,
            'cpf': self._cpf,
            'endereco': self._endereco,
            'email': self._email,
            'tipo': self._tipo

        }
        
#classe brinquedo-----------------------------
class Produto:
    def __init__(self, codigo, nome, preco, quantidade, descricao, imagem):

        self._codigo = codigo
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._descricao = descricao
        self._imagem = imagem
        self._data_cadastro = date.today()

    #getter---------------------------
    def get_codigo(self):
        return self._codigo
    
    def get_nome(self):
        return self._nome
    
    def get_preco(self):
        return self._preco
    
    def get_quantidade(self):
        return self._quantidade
    
    def get_descricao(self):
        return self._descricao
    
    def get_imagem(self):
        return self._imagem
    
    def get_data_cadastro(self):
        return self._data_cadastro
    
    #setter----------------------------
    #nome
    def set_nome(self, nome):

        if not nome.strip():
            print("Campos nome vazio")
            return False
        
        if not nome.replace(" ", "").isalpha():
            print("Apenas letras")
            return False
        
        self._nome = nome
        return True
    #preco
    def set_preco(self, valor):

        if valor < 0:
            print("Valor incorreto")
            return False
        else:
            self._preco = valor
            return True
    #quantidade
    def set_quantidade(self, valor):

        if valor < 0:
            print("Valor incorreto")
            return False
        else:
            self._quantidade = valor
            return True
    #descrição
    def set_descricao(self, descricao):
        self._descricao = descricao
        
    #imagem
    def set_imagem(self, imagem):
        self._imagem = imagem
    
    #metodo to dict-------------------------
    def to_dict(self):
        return {

            'codigo': self._codigo,
            'nome': self._nome,
            'preco': self._preco,
            'quantidade': self._quantidade,
            'descricao': self._descricao,
            'imagem': self._imagem,
            'data_cadastro': str(self._data_cadastro)
        }

#validação do cadastro------------------------

#validar nome

def validar_nome(nome):

    if not nome.strip():
        return 'Campo nome vazio'
    
    if not nome.replace(" ","").isalpha():
        return 'Apenas letras'
    
    return 'ok'

#validar preco

def validar_preco(preco):   
    
    if preco < 0:
        return 'Preço invalido'
    
    return 'ok'

#validar quantidade

def validar_quantidade(quantidade):

    if quantidade < 0:
        return 'Quantidade invalida'
    
    return 'ok'

#validar cadastro ususario-------------------

#validar login
def validar_login(login):

    if not login.strip():
        return 'Campo login vazio'
    
    return 'ok'

#validar senha
def validar_senha(senha):    

    if len(senha) != 6:
        return 'Senha invalida, senha deve conter 6 digitos'
    
    return "ok"

#validar data nascimento
def validar_data_nascimento(data_nascimento):

    if not data_nascimento.strip():
        return 'Campo data de nascimento vazia'

    if len(data_nascimento) != 10:
        return 'Data de nascimento invalida, digite dd/mm/aaaa'
    
    if "/" not in data_nascimento:
        return 'Use / para separar as datas'

    return 'ok'

#validar cpf
def validar_cpf(cpf):

    if len(cpf) != 11 or not cpf.isdigit():
        return 'CPF invalido, Digite apenas os 11 numeros sem ponto e traço'   
    return "ok"

#formatar cpf
def formatar_cpf(cpf):

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

#validar endereço
def validar_endereco(endereco):

    if not endereco.strip():
        return 'Campo endereço deve conter Rua: e N:'
    return 'ok'

#validar email
def validar_email(email):

    if not email.strip():
        return 'Campo email vazio'

    if "@" not in email or ".com" not in email:
        return 'Email invalido'
    return "ok"

#validar tipo
def validar_tipo(tipo):

    if not tipo.strip():
        return 'Campo vazio'
    return 'ok'    

#carregar usuarios----------------------------
def carregar_usuario():

    try:
        with open("dados/usuarios.json", "r") as f:
            dados = json.load(f)
            lista = []
            for item in dados:
                usuario = Usuario(item['login'], item['senha'], item['nome'], item['data_nascimento'], item['cpf'], item['endereco'], item['email'], item['tipo'])
                lista.append(usuario)
            return lista

    except FileNotFoundError:
        return []   
    
#salvar usuarios------------------------------
def salvar_usuarios(lista):

    dados = [{'login': u.get_login(), 'senha': u.get_senha(), 'nome': u.get_nome(), 'data_nascimento': u.get_data_nascimento(), 'cpf': u.get_cpf(), 'endereco': u.get_endereco(), 'email': u.get_email(), 'tipo': u.get_tipo()} for u in lista]
    with open("dados/usuarios.json", "w") as f:
        json.dump(dados, f, indent=4)

#carregar brinquedos---------------------------
def carregar_produto():

    try:
        with open("dados/brinquedos.json", "r") as f:
            dados = json.load(f)
            lista = []
            for item in dados:
                brinquedo = Produto(item['codigo'], item['nome'], item['preco'], item['quantidade'], item['descricao'], item['imagem'])
                lista.append(brinquedo)
            return lista
    
    except FileNotFoundError:
        return []
    
#salvar brinquedo-------------------------------
def salvar_produto(lista):

    dados = [{'codigo': b.get_codigo(), 'nome': b.get_nome(), 'preco': b.get_preco(), 'quantidade': b.get_quantidade(), 'descricao': b.get_descricao(), 'imagem': b.get_imagem(), 'data_cadastro': str(b.get_data_cadastro())} for b in lista]
    with open("dados/brinquedos.json", "w") as f:
        json.dump(dados, f, indent=4)

#menu--------------------------------------------
while True:
    print("-------Sistema de estoque------")
    print("1 - Login")
    print("2 - Sair")

    opcao = input("Digite sua escolha: ")

#login--------------------------------------------

    if opcao == "1":

        lista = carregar_usuario()
        encontrou = False

        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        for usuario in lista:            
            if usuario.get_login() == login:
                if usuario.get_senha() == senha:
                    encontrou = True
                    print("Login correto")

                    if usuario.get_tipo() == 'admin':

                        while True:
                            print("-------Menu adm------")
                            print("1 - Cadastra produto")
                            print("2 - Listar produtos")
                            print("3 - Buscar produto")
                            print("4 - Alterar produto")
                            print("5 - Remover produto")
                            print("6 - Relatorio")
                            print("7 - Cadastrar usuario")
                            print("8 - Buscar Usuarios")
                            print("9 - Remover usuario")
                            print("10 - Alterar usuario")
                            print("11 - Sair")

                            opcao = input("Digite sua escolha: ")

                            #cadastro----------------------------

                            if opcao == "1":
                                
                                nome = input("Digite o nome do produto: ").lower()
                                #validar--------------------
                                validar = validar_nome(nome)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                try:
                                    preco = float(input("Digite o preco R$: "))                                
                                    #validar----------------------
                                    validar = validar_preco(preco)
                                    if validar != "ok":
                                        print(validar)
                                        continue
                                except ValueError:
                                    print("Apenas numeros")
                                    continue
                                
                                try:
                                    quantidade = int(input("Digite a quantidade: "))                                
                                    #validar----------------------
                                    validar = validar_quantidade(quantidade)
                                    if validar != "ok":
                                        print(validar)
                                        continue
                                except ValueError:
                                    print("Apenas numeros")
                                    continue

                                #gerar codigo
                                lista_produto = carregar_produto()
                                maior = 0
                                for p in lista_produto:
                                    if p.get_codigo() > maior:
                                        maior = p.get_codigo()
                                codigo = maior +1

                                descricao = input("Digite a descrição: ").lower()
                                imagem = input("Gostaria de adicionar uma imagem: ")

                                produto = Produto(codigo, nome, preco, quantidade, descricao, imagem)
                                
                                lista_produto.append(produto)
                                salvar_produto(lista_produto)

                                print(f"Produto {nome} cadastrado com o codigo {codigo}")

                            #lista produtos--------------------------------------

                            elif opcao == "2":

                                lista = carregar_produto()

                                if not lista:
                                    print("Lista de produtos vazia")
                                else:
                                    for p in lista:
                                        nome_formatado = p.get_nome().capitalize()
                                        descricao_formatado = p.get_descricao().capitalize()
                                        print(f"Codigo: {p.get_codigo()} - Nome: {nome_formatado} - Preço R$: {p.get_preco()} - Quantidade: {p.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {p.get_imagem()}")

                            #bucar produtos---------------------------------------

                            elif opcao == "3":

                                lista = carregar_produto()
                                encontrou = False
                                

                                buscar = input("Bucar pelo Nome(n) ou Cod(c): ").lower()                                
                                #busca nome-------
                                if buscar == "n":
                                    nome = input("Digite o nome do produto: ").lower()
                                    #validar----------------------
                                    validar = validar_nome(nome)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    for p in lista:
                                        if p.get_nome() == nome:
                                            nome_formatado = p.get_nome().capitalize()
                                            descricao_formatado = p.get_descricao().capitalize()
                                            encontrou = True
                                            print(f"Codigo: {p.get_codigo()} - Nome: {nome_formatado} - Preço R$: {p.get_preco()} - Quantidade: {p.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {p.get_imagem()}")
                                            break

                                    if not encontrou:
                                        print("Produto não encontrado")                                        
                                
                                #busca codigo---------
                                elif buscar == "c":
                                    try:
                                        codigo = int(input("Digite o codigo do produto: "))
                                    except ValueError:
                                        print("Apenas numeros")
                                        continue

                                    for p in lista:
                                        if p.get_codigo() == codigo:
                                            nome_formatado = p.get_nome().capitalize()
                                            descricao_formatado = p.get_descricao().capitalize()
                                            encontrou = True
                                            print(f"Codigo: {p.get_codigo()} - Nome: {nome_formatado} - Preço R$: {p.get_preco()} - Quantidade: {p.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {p.get_imagem()}")
                                            break

                                    if not encontrou:
                                        print("Produto não encontrado")

                            #alterar produto---------------------------------------------

                            elif opcao == "4":

                                lista = carregar_produto()
                                encontrou = False

                                codigo = int(input("Digite o codigo do produto: "))

                                for produto in lista:
                                    if produto.get_codigo() == codigo:
                                        nome_formatado = produto.get_nome().capitalize()
                                        descricao_formatado = produto.get_descricao().capitalize()
                                        encontrou = True

                                        print(f"Nome: {nome_formatado} - Preço R$: {produto.get_preco()} - Quantidade: {produto.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {produto.get_imagem()}")
                                        while True:
                                            print("------Menu alterar produto------")
                                            print("1 - Nome")
                                            print("2 - Preço")
                                            print("3 - Quantidade")
                                            print("4 - Descrição")
                                            print("5 - Imagem")
                                            print("6 - Voltar")

                                            opcao_pro = input("Digite sua escolha: ")
                                        
                                            #alterar nome-------------------------
                                            if opcao_pro == "1":
                                                confirmar = input("Realmente gostaria de alterar o nome do produto? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome do produto: {nome_formatado}")
                                                    novo_nome = input("Digite o novo nome: ").lower()

                                                    if produto.set_nome(novo_nome):
                                                        salvar_produto(lista)
                                                        print("Nome alterado com sucesso")
                                                    else:
                                                        print("Nome invalido, não alterado")
                                                
                                                else:
                                                    print("Alterar nome cancelado")
                                                    
                                            #alterar preço-------------------------
                                            elif opcao_pro == "2":
                                                confirmar = input("Realmente deseja alterar o preço deste produto? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Preço: {produto.get_preco()}")
                                                    try:
                                                        novo_preco = float(input("Digite o novo preço: "))
                                                    except ValueError:
                                                        print("Apenas numeros")
                                                        continue

                                                    if produto.set_preco(novo_preco):
                                                        salvar_produto(lista)
                                                        print("Preço alterado com sucesso")
                                                    else:
                                                        print("Preço invalido, não alterado")

                                                else:
                                                    print("Alterar preço cancelado")

                                            #alterar quantidade---------------------
                                            elif opcao_pro == "3":
                                                confirmar = input("Realmente deseja alterar a quantidade deste produto? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Quantidade: {produto.get_quantidade()}")
                                                    try:
                                                        nova_quantidade = int(input("Digite a nova quantidade: "))
                                                    except ValueError:
                                                        print("Apenas numeros")
                                                        continue

                                                    if produto.set_quantidade(nova_quantidade):
                                                        salvar_produto(lista)
                                                        print("Quantidade alterada com sucesso")
                                                    else:
                                                        print("Quantidade invalida, não alterada")

                                                else:
                                                    print("Alterar quantidade cancelado")

                                            #alterar descrição-------------------------
                                            elif opcao_pro == "4":
                                                confirmar = input("Realmente deseja alterar a descrição deste produto? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Descrição: {descricao_formatado}")
                                                    
                                                    nova_descricao = input("Digite a nova descrição: ")

                                                    produto.set_descricao(nova_descricao)
                                                    salvar_produto(lista)

                                                    print("Descrição alterada com sucesso")
                                                
                                                else:
                                                    print("Alterar descrição cancelado")

                                            #imagem-----------------------------------
                                            elif opcao_pro == "5":
                                                confirmar = input("Realmente deseja alterar a imagem deste produto? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Imagem: {produto.get_imagem()}")
                                                    
                                                    nova_imagem = input("Digite o caminho da imagem")

                                                    produto.set_imagem(nova_imagem)
                                                    salvar_produto(lista)

                                                    print("Imagem alterada com sucesso")
                                                
                                                else:
                                                    print("Alterar Imagem cancelado")

                                            #voltar--------------------------------------
                                            elif opcao_pro == "6":
                                                print("")
                                                break


                                if not encontrou:
                                    print("Produto não cadastrado")
                            
                            #remover produto--------------------------------------------
                            elif opcao == "5":

                                lista = carregar_produto()
                                encontrou = False
                                try:
                                    codigo = int(input("Digite o codigo do produto: "))
                                except ValueError:
                                    print("Apenas numeros")
                                    continue

                                for produto in lista:
                                    if produto.get_codigo() == codigo:
                                        nome_formatado = produto.get_nome().capitalize()
                                        descricao_formatado = produto.get_descricao().capitalize()
                                        encontrou = True                                        
                                        print(f"Nome: {nome_formatado} - Preço: {produto.get_preco()} - Quantidade: {produto.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {produto.get_imagem()}")
                                        
                                        confirmar = input("Realmente deseja remover ester produto? (s/n): ").lower()

                                        if confirmar == "s":
                                            lista.remove(produto)
                                            salvar_produto(lista)

                                            print("Produto removido")  
                                            break                                          
                                        else:
                                            print("Remover produto cancelado")
                                            break
                                
                                if not encontrou:
                                    print("Produto não cadastrado")

                            #relatorio---------------------------------------------------
                            elif opcao == "6":

                                lista = carregar_produto()

                                while True:

                                    print("-----Relatorio----")
                                    print("1 - Valor total de estoque")
                                    print("2 - Quantidade total de produtos")
                                    print("3 - Produtos com estoque baixo (menos de 5 unidades)")
                                    print("4 - Voltar")

                                    opcao_rela = input("Digite sua escolha: ")

                                    #Valor total--------------------------------------------

                                    if opcao_rela == "1":

                                        total = 0

                                        #cabeçalho
                                        print(f"{'Nome':<30} {'Quantidade':>10} {'Preço':>10}")
                                        print("-" * 55)

                                        #dados                                        
                                        for produto in lista:
                                            nome_formatado = produto.get_nome().capitalize()
                                            print(f"{nome_formatado:<30} {produto.get_quantidade():>10} R$: {produto.get_preco():>7.2f}")
                                            total += produto.get_preco() * produto.get_quantidade()

                                        #Total
                                        print("-" * 55)
                                        print(f"{'Total':<30} {'':>10} R$: {total:>7.2f}")

                                    #quantidade total------------------------------------------

                                    elif opcao_rela == "2":

                                        total = 0

                                        #cabeçalho
                                        print(f"{'Nome':<30} {'Quantidade':>20}")
                                        print("-" * 55)

                                        for produto in lista:
                                            nome_formatado = produto.get_nome().capitalize()
                                            print(f"{nome_formatado:<30} {produto.get_quantidade():>17}")
                                            total += produto.get_quantidade()

                                        #Total
                                        print("-" * 55)
                                        print(f"{'Total':<30} {total:>17}")

                                    #produtos com estoque baixo----------------------------------

                                    elif opcao_rela == "3":

                                        #cabeçalho
                                        print(f"{'Produtos com estoque baixo':<30} {'Quantidade':>20}")
                                        print("-" * 55)

                                        for produto in lista:
                                            if produto.get_quantidade() < 5:
                                                nome_formatado = produto.get_nome().capitalize()
                                                print(f"{nome_formatado:<30} Critico: {produto.get_quantidade():>17}")

                                        #
                                        print("-" * 55)

                                    #voltar--------------------------------------------------------

                                    elif opcao_rela == "4":
                                        print("")
                                        break
                            
                            #cadastro de usuarios---------------------------------------------------

                            elif opcao == "7":

                                login = input("Login do usuario: ").lower()
                                #validar--------------------
                                validar = validar_login(login)
                                if validar != "ok":
                                    print(validar)
                                    continue 

                                
                                senha = input("Digite sua senha: ")                                                                      
                                #validar--------------------
                                validar = validar_senha(senha)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                nome = input("Digite seu nome: ").lower()
                                #validar--------------------
                                validar = validar_nome(nome)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                data_nascimento = input("Digite sua data de nascimento: ")
                                #validar data---------------
                                validar = validar_data_nascimento(data_nascimento)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                cpf = input("Digite seu CPF: ")
                                #validar---------------------
                                validar = validar_cpf(cpf)
                                if validar != "ok":
                                    print(validar)
                                    continue                                

                                endereco = input("Digite seu endereço: ")
                                #validar-----------------------
                                validar = validar_endereco(endereco)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                email = input("Digite seu email: ")
                                #validar------------------------
                                validar = validar_email(email)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                tipo = input("Digite Funcionario ou Adm: ").lower()
                                #validar-------------------------
                                validar = validar_tipo(tipo)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                usuario = Usuario(login, senha, nome, data_nascimento, cpf, endereco, email, tipo)

                                lista = carregar_usuario()
                                lista.append(usuario)
                                salvar_usuarios(lista)                                                 
                                print("Usuario cadastrado")
                            
                            #listar usuarios-----------------------------------------

                            elif opcao == "8":

                                lista = carregar_usuario()

                                while True:
                                    print("1 - Buscar por usuario")
                                    print("2 - Listar todos os usuarios")
                                    print("3 - Voltar")

                                    opcao_busca = input("Digite sua escolha: ")

                                    #------------------------------------------------

                                    if opcao_busca == "1":
                                        #busca pelo login-----------------------------
                                        login = input("Digite o login do usuario: ")
                                        encontrou = False

                                        for usuario in lista:
                                            if usuario.get_login() == login:
                                                cpf_formatado = formatar_cpf(usuario.get_cpf())
                                                encontrou = True

                                                print("\nInformações do usuario")
                                                print("-----------------------------------")
                                                print(f"Login:              {usuario.get_login()}")
                                                print(f"Nome:               {usuario.get_nome()}")
                                                print(f"Data de nascimento: {usuario.get_data_nascimento()}")
                                                print(f"CPF:                {cpf_formatado}")
                                                print(f"Endereço:           {usuario.get_endereco()}")
                                                print(f"Email:              {usuario.get_email()}")
                                                print(f"Tipo:               {usuario.get_tipo()}")
                                                print("\n")
                                                break

                                        if not encontrou:
                                            print("Usuario não cadastrado")

                                    #busca todos-------------------------------------
                                    elif opcao_busca == "2":

                                        if not lista:
                                            print("Lista de ususarios vazia")
                                        else:
                                            print("\n")
                                            print(f"{'Login':<15} {'Nome':<20} {'Tipo':<12}")
                                            print("-" * 50)

                                            for usuario in lista:
                                                nome_formatado = usuario.get_nome().capitalize()
                                                tipo_formatao = usuario.get_tipo().capitalize()
                                                print(f"{usuario.get_login():<15} {nome_formatado:<20} {tipo_formatao:<12}")
                                                
                                    #voltar-----------------------------------------
                                    elif opcao_busca == "3":
                                        print("")
                                        break

                            #remover-------------------------------------------------

                            elif opcao == "9":

                                lista = carregar_usuario()
                                encontrou = False

                                login = input("Digite o login do usuario que deseja remover: ").lower()
                                
                                for usuario in lista:
                                    if usuario.get_login() == login:
                                        nome_formatado = usuario.get_nome().capitalize()
                                        tipo_formatado = usuario.get_tipo().capitalize()
                                        encontrou = True                                        
                                        print(f"Nome: {nome_formatado} - Tipo: {tipo_formatado}")

                                        confirmar = input("Realmente deseja remover este usuario? (s/n): ")
                                        if confirmar == "s":
                                            lista.remove(usuario)
                                            salvar_usuarios(lista)

                                            print("Usuario removido")
                                            break
                                        else:
                                            print("Remover usuario cancelado")
                                            break

                                if not encontrou:
                                    print("Usuario não cadastrado")

                            #alterar usuario--------------------------------------------

                            elif opcao == "10":

                                lista = carregar_usuario()
                                encontrou = False

                                login = input("Digite seu login: ")

                                for usuario in lista:
                                    if usuario.get_login() == login:
                                        nome_formatado = usuario.get_nome().capitalize()
                                        endereco_formatado = usuario.get_endereco().capitalize()
                                        tipo_formatado = usuario.get_tipo().capitalize()
                                        encontrou = True

                                        print("\nInformações do usuario")
                                        print("----------------------------------")
                                        print(f"Nome:     {nome_formatado}")
                                        print(f"Email:    {usuario.get_email()}")
                                        print(f"Endereço: {endereco_formatado}")
                                        print(f"Senha:    {usuario.get_senha()}")
                                        print(f"Tipo:     {tipo_formatado}")
                                        print("----------------------------------\n")
                                        while True:
                                            print("1 - nome")
                                            print("2 - Email")
                                            print("3 - Endereço")
                                            print("4 - Senha")
                                            print("5 - Tipo")
                                            print("6 - Voltar")

                                            opcao_alt = input("Digite sua escolha: ")

                                            #nome-----------------------------------------

                                            if opcao_alt == "1":

                                                confirmar = input("Realmente gostaria de alterar o nome deste usuario? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome do usuario: {nome_formatado}")

                                                    novo_nome = input("Digite o novo nome: ").lower()

                                                    if usuario.set_nome(novo_nome):
                                                        salvar_usuarios(lista)
                                                        print("Nome de usuario alterado com sucesso")
                                                    else:
                                                        print("Nome invalido, não alterado")
                                                
                                                else:
                                                    print("Alterar nome cancelado")

                                            #email-----------------------------------------

                                            elif opcao_alt == "2":

                                                confirmar = input("Realmente deseja alterar o email do usuario? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Email do usuario: {usuario.get_email()}")

                                                    novo_email = input("Digite o novo email: ")

                                                    if usuario.set_email(novo_email):
                                                        salvar_usuarios(lista)
                                                        print("Email do usuario alterado com sucesso")
                                                    else:
                                                        print("Email invalido, não alterado")

                                                else:
                                                    print("Alterar email cancelado")

                                            #endereço---------------------------------------

                                            elif opcao_alt == "3":

                                                confirmar = input("Realmente gostaria de alterar o endereço do usuario? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Endereço do usuarios: {endereco_formatado}")

                                                    novo_endereco = input("Digite o novo endereço do usuario: ").lower()

                                                    if usuario.set_endereco(novo_endereco):
                                                        salvar_usuarios(lista)
                                                        print("Enredeço alterado com sucesso")
                                                    else:
                                                        print("Endereço invalido, não alterado")
                                                    
                                                else:
                                                    print("Alterar endereço cancelado")

                                            #senha--------------------------------------------

                                            elif opcao_alt == "4":

                                                confirmar = input("Realmente gostaria de alterar a senha do usuario? (s/n): ").lower()

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Senha do usuario: {usuario.get_senha()}")

                                                    nova_senha = input("Digite a nova senha do usuario: ")

                                                    if usuario.set_senha(nova_senha):
                                                        salvar_usuarios(lista)
                                                        print("Senha alterada com sucesso")
                                                    else:
                                                        print("Senha invalida, não alterada")

                                                else:
                                                    print("Alterar senha cancelao")

                                            #tipo----------------------------------------------

                                            elif opcao_alt == "5":

                                                confirmar = input("Realmente gostaria de alterar o tipo do usuario? (s/n): ")

                                                if confirmar == "s":
                                                    print(f"Nome: {nome_formatado} - Tipo: {tipo_formatado}")

                                                    novo_tipo = input("Digite o novo Tipo do usuario: ")

                                                    if usuario.set_tipo(novo_tipo):
                                                        salvar_usuarios(lista)
                                                        print("Tipo alterado com sucesso")
                                                    else:
                                                        print("Tipo invalido, não alterado")
                                                
                                                else:
                                                    print("Alterar tipo cancelado")

                                            #voltar---------------------------------------------

                                            elif opcao_alt == "6":
                                                print("")
                                                break
                                
                                if not encontrou:
                                    print("Usuario não cadastrado")
                                

                            #sair-----------------------------------------------------------------

                            elif opcao == "11":
                                print("Sair do sistema...........")
                                break
                    #menu funcionario--------------------------------------------------------------
                    else:

                        while True:

                            print("-------Menu------")
                            print("1 - Cadastrar produto")                            
                            print("2 - Buscar produto")
                            print("3 - Sair")

                            opcao_fun = input("Digite sua escolha: ")

                            #cadastro produto------------------------------------------------------

                            if opcao_fun =="1":

                                nome = input("Digite o nome do produto: ").lower()
                                #validar--------------------
                                validar = validar_nome(nome)
                                if validar != "ok":
                                    print(validar)
                                    continue

                                try:
                                    preco = float(input("Digite o preco R$: "))                                
                                    #validar----------------------
                                    validar = validar_preco(preco)
                                    if validar != "ok":
                                        print(validar)
                                        continue
                                except ValueError:
                                    print("Apenas numeros")
                                    continue
                                
                                try:
                                    quantidade = int(input("Digite a quantidade: "))                                
                                    #validar----------------------
                                    validar = validar_quantidade(quantidade)
                                    if validar != "ok":
                                        print(validar)
                                        continue
                                except ValueError:
                                    print("Apenas numeros")
                                    continue

                                #gerar codigo
                                lista_produto = carregar_produto()
                                maior = 0
                                for p in lista_produto:
                                    if p.get_codigo() > maior:
                                        maior = p.get_codigo()
                                codigo = maior +1

                                descricao = input("Digite a descrição: ").lower()
                                imagem = input("Gostaria de adicionar uma imagem: ")

                                produto = Produto(codigo, nome, preco, quantidade, descricao, imagem)
                                
                                lista_produto.append(produto)
                                salvar_produto(lista)

                                print(f"Produto {nome} cadastrado com o codigo {codigo}")
                            
                            #listar produtos-------------------------------------------------------

                            elif opcao_fun == "2":

                                lista = carregar_produto()
                                encontrou = False                                

                                buscar = input("Bucar pelo Nome(n) ou Cod(c): ").lower()                                
                                #busca nome-------
                                if buscar == "n":
                                    nome = input("Digite o nome do produto: ").lower()
                                    #validar----------------------
                                    validar = validar_nome(nome)
                                    if validar != "ok":
                                        print(validar)
                                        continue

                                    for p in lista:
                                        if p.get_nome() == nome:
                                            nome_formatado = p.get_nome().capitalize()
                                            descricao_formatado = p.get_descricao().capitalize()
                                            encontrou = True
                                            print(f"Nome: {nome_formatado} - Preço R$: {p.get_preco()} - Quantidade: {p.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {p.get_imagem()}")
                                            break

                                    if not encontrou:
                                        print("Produto não encontrado")                                        
                                
                                #busca codigo---------
                                elif buscar == "c":
                                    try:
                                        codigo = int(input("Digite o codigo do produto: "))
                                    except ValueError:
                                        print("Apenas numeros")
                                        continue

                                    for p in lista:
                                        if p.get_codigo() == codigo:
                                            nome_formatado = p.get_nome().capitalize()
                                            descricao_formatado = p.get_descricao().capitalize()
                                            encontrou = True
                                            print(f"Nome: {nome_formatado} - Preço R$: {p.get_preco()} - Quantidade: {p.get_quantidade()} - Descrição: {descricao_formatado} - Imagem: {p.get_imagem()}")
                                            break

                                    if not encontrou:
                                        print("Produto não encontrado")
                            
                            #sair--------------------------------------------------------------------
                            elif opcao_fun == "3":
                                print("")
                                break

                else:
                    print("Senha incorreta, tente novamente")
                break

        if not encontrou:
            print("Usuario não cadastrado")

    elif opcao == "2":
        print("Sair")
        break

            





        
        