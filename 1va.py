import os
import json

# Função para limpar a tela do terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para carregar dados de um arquivo txt
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Função para salvar dados em um arquivo txt
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Carregar os dados ao iniciar o programa
produtos = carregar_dados('produtos.txt')
vendas = carregar_dados('vendas.txt')
despesas = carregar_dados('despesas.txt')

# Dicionário de usuário e senha para login
usuario_senha = {"admin": "senha123"}

# Função de login do usuário
def login():
    while True:
        clear_screen()
        usuario = input("Digite o login/usuário: ")
        senha = input("Digite a senha: ")
        if usuario in usuario_senha and senha == usuario_senha["admin"]:
            print("Login executado com sucesso!")
            input("Pressione Enter para continuar...")  # Pausa antes de continuar
            break
        else:
            print("Usuário ou Senha incorreto!")
            input("Pressione Enter para tentar novamente...")  # Pausa para leitura da mensagem

    clear_screen()
    menu_principal()  # Chama o menu principal após login bem-sucedido

# Função para exibir o menu principal
def menu_principal():
    while True:
        clear_screen()
        print("\nMenu Principal")
        print("1. Controle de Estoque")
        print("2. Controle Financeiro")
        print("3. Relatórios")
        print("4. Configurações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            controle_estoque()
        elif opcao == "2":
            controle_financeiro()
        elif opcao == "3":
            relatorios()
        elif opcao == "4":
            configuracoes()
        elif opcao == "5":
            print("Saindo do programa...")
            input("Pressione Enter para sair...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")  # Pausa para leitura da mensagem

        clear_screen()

# Menu para controle de estoque
def controle_estoque():
    while True:
        clear_screen()
        print("\nControle de Estoque")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Remover Produto")
        print("4. Visualizar Estoque")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")  # Pausa para leitura da mensagem

        clear_screen()

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    try:
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco_custo = float(input("Preço de custo: "))
        preco_venda = float(input("Preço de venda: "))
        categoria = input("Categoria: ")
        descricao = input("Descrição (opcional): ")

        novo_produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco_custo": preco_custo,
            "preco_venda": preco_venda,
            "categoria": categoria,
            "descricao": descricao,
        }

        produtos.append(novo_produto)
        salvar_dados('produtos.txt', produtos)
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para quantidade e preços.")
    
    input("Pressione Enter para continuar...")
    clear_screen()

# Função para atualizar um produto existente no estoque
def atualizar_produto():
    nome = input("Nome do produto a ser atualizado: ")
    produto = None
    for p in produtos:
        if p['nome'] == nome:
            produto = p
            break

    if produto:
        try:
            novo_nome = input("Novo nome do produto (ou Enter para manter o atual): ")
            nova_quantidade = input("Nova quantidade (ou Enter para manter a atual): ")
            novo_preco_custo = input("Novo preço de custo (ou Enter para manter o atual): ")
            novo_preco_venda = input("Novo preço de venda (ou Enter para manter o atual): ")
            nova_categoria = input("Nova categoria (ou Enter para manter a atual): ")
            nova_descricao = input("Nova descrição (ou Enter para manter a atual): ")

            if novo_nome:
                produto['nome'] = novo_nome
            if nova_quantidade:
                produto['quantidade'] = int(nova_quantidade)
            if novo_preco_custo:
                produto['preco_custo'] = float(novo_preco_custo)
            if novo_preco_venda:
                produto['preco_venda'] = float(novo_preco_venda)
            if nova_categoria:
                produto['categoria'] = nova_categoria
            if nova_descricao:
                produto['descricao'] = nova_descricao

            salvar_dados('produtos.txt', produtos)
            print("Produto atualizado com sucesso!")
        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos para quantidade e preços.")
    else:
        print("Produto não encontrado!")

    input("Pressione Enter para continuar...")
    clear_screen()

# Função para remover um produto do estoque
def remover_produto():
    nome = input("Nome do produto a ser removido: ")
    produto = None
    for p in produtos:
        if p['nome'] == nome:
            produto = p
            break

    if produto:
        produtos.remove(produto)
        salvar_dados('produtos.txt', produtos)
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado!")

    input("Pressione Enter para continuar...")
    clear_screen()

# Função para visualizar todos os produtos no estoque
def visualizar_estoque():
    if not produtos:
        print("Nenhum produto no estoque!")
    else:
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço de Custo: {produto['preco_custo']:.2f}, Preço de Venda: {produto['preco_venda']:.2f}, Categoria: {produto['categoria']}, Descrição: {produto['descricao']}")

    input("Pressione Enter para continuar...")
    clear_screen()

# Menu para controle financeiro
def controle_financeiro():
    while True:
        clear_screen()
        print("\nControle Financeiro")
        print("1. Registro de Vendas")
        print("2. Registro de Despesas")
        print("3. Visualizar Relatórios Financeiros")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registro_vendas()
        elif opcao == "2":
            registro_despesas()
        elif opcao == "3":
            visualizar_relatorios_financeiros()
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")  # Pausa para leitura da mensagem

        clear_screen()

# Função para registrar uma nova venda
def registro_vendas():
    produto_nome = input("Nome do produto vendido: ")
    try:
        quantidade_vendida = int(input("Quantidade vendida: "))
        preco_venda = float(input("Preço de venda: "))
        data_venda = input("Data da venda (dd/mm/yyyy): ")

        produto = None
        for p in produtos:
            if p['nome'] == produto_nome:
                produto = p
                break

        if produto and produto['quantidade'] >= quantidade_vendida:
            produto['quantidade'] -= quantidade_vendida
            venda = {"produto": produto_nome, "quantidade": quantidade_vendida, "preco": preco_venda, "data": data_venda}
            vendas.append(venda)
            salvar_dados('produtos.txt', produtos)
            salvar_dados('vendas.txt', vendas)
            print("Venda registrada com sucesso!")
        else:
            print("Produto não encontrado ou quantidade insuficiente!")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para quantidade e preço.")

    input("Pressione Enter para continuar...")
    clear_screen()

# Função para registrar uma nova despesa
def registro_despesas():
    try:
        tipo_despesa = input("Tipo de despesa: ")
        valor = float(input("Valor: "))
        data = input("Data da despesa (dd/mm/yyyy): ")

        despesa = {"tipo": tipo_despesa, "valor": valor, "data": data}
        despesas.append(despesa)
        salvar_dados('despesas.txt', despesas)
        print("Despesa registrada com sucesso!")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para a despesa.")
    
    input("Pressione Enter para continuar...")
    clear_screen()

# Função para visualizar relatórios financeiros
def visualizar_relatorios_financeiros():
    total_vendas = 0
    for venda in vendas:
        total_vendas += venda['preco'] * venda['quantidade']

    total_despesas = 0
    for despesa in despesas:
        total_despesas += despesa['valor']

    print(f"Total de Vendas: R${total_vendas:.2f}")
    print(f"Total de Despesas: R${total_despesas:.2f}")
    print(f"Balanço: R${(total_vendas - total_despesas):.2f}")

    input("Pressione Enter para continuar...")
    clear_screen()

# Menu para relatórios
def relatorios():
    while True:
        clear_screen()
        print("\nRelatórios")
        print("1. Relatório de Estoque")
        print("2. Relatório Financeiro")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_estoque()
        elif opcao == "2":
            visualizar_relatorios_financeiros()
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")  # Pausa para leitura da mensagem

        clear_screen()

# Menu de configurações
def configuracoes():
    while True:
        clear_screen()
        print("\nConfigurações")
        print("1. Mudar Login e Senha")
        print("2. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mudar_login_senha()
        elif opcao == "2":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")  # Pausa para leitura da mensagem

        clear_screen()

# Função para mudar login e senha
def mudar_login_senha():
    usuario_atual = input("Nome de usuário atual: ")
    senha_atual = input("Senha atual: ")

    if usuario_atual in usuario_senha and usuario_senha[usuario_atual] == senha_atual:
        novo_usuario = input("Novo nome de usuário: ")
        nova_senha = input("Nova senha: ")

        usuario_senha[novo_usuario] = nova_senha
        del usuario_senha[usuario_atual]
        print("Nome de usuário e senha alterados com sucesso!")
    else:
        print("Usuário ou senha atual incorretos!")

    input("Pressione Enter para continuar...")
    clear_screen()

# Iniciar o programa chamando a função de login
if __name__ == "__main__":
    login()