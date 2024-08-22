usuario_senha = {"admin" : "senha123"}
produtos = []
vendas = []
despesas = []

# Funcionalidade 1: LOGIN DO USUÁRIO
def login():
    usuario = input("Digite o login/usuário: ")
    senha = input("Digite a senha: ")
    if usuario in usuario_senha and senha == usuario_senha["admin"]:
        print("Login executado com sucesso!")
        menu_principal()
    else:
        print("Usuário ou Senha incorreto!")
        login()

# Funcionalidade 2: EXIBIÇÃO DE INFORMAÇÕES NO MENU PRINCIPAL
def exibir_relatorio_menu():
    faturamento_atual = 0
    for venda in vendas:
        faturamento_atual += venda['preco'] * venda['quantidade']

    total_produtos_estoque = 0
    for produto in produtos:
        total_produtos_estoque += produto['quantidade']

    total_despesas = 0
    for despesa in despesas:
        total_despesas += despesa['valor']

    balanco_atual = faturamento_atual - total_despesas

    print("\nInformações Gerais:")
    print(f"Faturamento Atual: R${faturamento_atual:.2f}")
    print(f"Total de Produtos no Estoque: {total_produtos_estoque:.2f}")
    print(f"Total de Despesas: R${total_despesas:.2f}")
    print(f"Balanço Atual: R${balanco_atual:.2f}")

# Funcionalidade 3: MENU PRINCIPAL
def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Controle de Estoque")
        print("2. Controle Financeiro")
        print("3. Relátorios")
        print("4. Configurações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        exibir_relatorio_menu()

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
            break
        else:
            print("Opção inválida! Tente novamente.")

# Funcionalidade 4: CONTROLE DE ESTOQUE
def controle_estoque():
    while True:
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


# Funcionalidade 4.1: ADICIONAR PRODUTO
def adicionar_produto():
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
    print("Produto adicionado com sucesso!")

# Funcionalidade 4.2: ATUALIZAR PRODUTO
def atualizar_produto():
    nome = input("Nome do produto a ser atualizado: ")
    produto = None
    for p in produtos:
        if p['nome'] == nome:
            produto = p
            break

    if produto:
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

        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado!")

# Funcionalidade 4.3: REMOVER PRODUTO
def remover_produto():
    nome = input("Nome do produto a ser removido: ")
    produto = None
    for p in produtos:
        if p['nome'] == nome:
            produto = p
            break

    if produto:
        produtos.remove(produto)
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado!")

# Funcionalidade 4.4: VISUALIZAR ESTOQUE
def visualizar_estoque():
    if not produtos:
        print("Nenhum produto no estoque!")
    else:
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço de Custo: {produto['preco_custo']:.2f}, Preço de Venda: {produto['preco_venda']:.2f}, Categoria: {produto['categoria']}, Descrição: {produto['descricao']}")

# Funcionalidade 5: MENU CONTROLE FINANCEIRO
def controle_financeiro():
    while True:
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

# Funcionalidade 5.1: REGISTRO DE VENDAS
def registro_vendas():
    produto_nome = input("Nome do produto vendido: ")
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
        print("Venda registrada com sucesso!")
    else:
        print("Produto não encontrado ou quantidade insuficiente!")

# Funcionalidade 5.2: REGISTRO DE DESPESAS
def registro_despesas():
    tipo_despesa = input("Tipo de despesa: ")
    valor = float(input("Valor: "))
    data = input("Data da despesa (dd/mm/yyyy): ")

    despesa = {"tipo": tipo_despesa, "valor": valor, "data": data}
    despesas.append(despesa)
    print("Despesa registrada com sucesso!")

# Funcionalidade 5.3: RELÁTORIOS FINANCEIROS
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

# Funcionalidade 6: RELATÓRIOS
def relatorios():
    while True:
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

# Funcionalidade 7: MENU CONFIGURAÇÕES
def configuracoes():
    while True:
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

# Funcionalidade 7.1: MUDAR LOGIN E SENHA
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

# Iniciar o programa
login()