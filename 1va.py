from datetime import datetime
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
compras = carregar_dados('compras.txt')

# Dicionário de usuário e senha para login
usuario_senha = {"admin": "senha123"}

# FEATURE 01: LOGIN DO USUÁRIO ------------------------------------------------------------------

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

# FEATURE 02: MENU PRINCIPAL ----------------------------------------------------------------------

# Função menu principal
def menu_principal():
    while True:
        clear_screen()
        
        # Exibir o menu principal
        print("\nMenu Principal")
        print("1. Controle de Estoque")
        print("2. Controle Financeiro")
        print("3. Relatórios")
        print("4. Configurações")
        print("5. Filtros")
        print("6. Sugestões")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

    # FEATURE 07: EXIBIÇÃO DE DADOS:

        # Verificar se há sugestões aplicáveis
        sugestoes = verificar_sugestoes()

        # Exibir sugestões abaixo do menu, se houver
        if sugestoes:
            print("\n===========\nSugestões:\n===========")
            for sugestao in sugestoes:
                print(f"- {sugestao}")
        
        # Processar a opção escolhida pelo usuário
        if opcao == "1":
            controle_estoque()
        elif opcao == "2":
            controle_financeiro()
        elif opcao == "3":
            relatorios()
        elif opcao == "4":
            configuracoes()
        elif opcao == "5":
            menu_filtros()
        elif opcao == "6":
            menu_sugestoes()
        elif opcao == "7":
            print("Saindo do programa...")
            input("Pressione Enter para sair...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
        
        clear_screen()

# FEATURE 03: CONTROLE DE ESTOQUE -----------------------------------------------------------

# Menu para controle de estoque
def controle_estoque():
    while True:
        clear_screen()
        print("\nControle de Estoque")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Remover Produto")
        print("4. Visualizar Estoque")
        print("5. Histórico de Compras")
        print("6. Voltar ao Menu Principal")
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
            visualizar_historico_compras()
        elif opcao == "6":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...") 

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
        # Registro da compra automaticamente
        registrar_compra_automatico(nome, quantidade, preco_custo)
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
        if p['nome'].lower() == nome.lower():
            produto = p
            break

    if produto:
        try:
            novo_nome = input("Novo nome do produto (ou Enter para manter o atual): ")
            adicionar_quantidade = input("Quantidade a adicionar (ou Enter para manter a atual): ")
            novo_preco_custo = input("Novo preço de custo (ou Enter para manter o atual): ")
            novo_preco_venda = input("Novo preço de venda (ou Enter para manter o atual): ")
            nova_categoria = input("Nova categoria (ou Enter para manter a atual): ")
            nova_descricao = input("Nova descrição (ou Enter para manter a atual): ")

            if novo_nome:
                produto['nome'] = novo_nome
            if adicionar_quantidade:
                quantidade_adicionada = int(adicionar_quantidade)
                produto['quantidade'] += quantidade_adicionada
                # Registro da compra automaticamente
                registrar_compra_automatico(produto['nome'], quantidade_adicionada, produto['preco_custo'])
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

# FEATURE 04: CONTROLE FINANCEIRO ----------------------------------------------------------------

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
            input("Pressione Enter para continuar...")

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

# FEATURE 05: RELATÓRIOS -------------------------------------------------------------------------

def relatorio_produtos_mais_vendidos():
    clear_screen()
    vendas_agrupadas = {}
    for venda in vendas:
        produto = venda['produto']
        quantidade = venda['quantidade']
        if produto in vendas_agrupadas:
            vendas_agrupadas[produto] += quantidade
        else:
            vendas_agrupadas[produto] = quantidade

    # Ordenar os produtos pelas vendas totais
    produtos_ordenados = sorted(vendas_agrupadas.items(), key=lambda x: x[1], reverse=True)

    print("Relatório de Produtos Mais Vendidos:")
    for produto, quantidade in produtos_ordenados:
        print(f"Produto: {produto}, Quantidade Vendida: {quantidade}")

    input("Pressione Enter para continuar...")
    clear_screen()

def relatorio_produtos_com_menor_estoque():
    clear_screen()
    produtos_ordenados = sorted(produtos, key=lambda p: p['quantidade'])

    print("Relatório de Produtos com Menor Estoque:")
    for produto in produtos_ordenados:
        print(f"Produto: {produto['nome']}, Quantidade em Estoque: {produto['quantidade']}")

    input("Pressione Enter para continuar...")
    clear_screen()

def relatorio_lucro_por_produto():
    clear_screen()
    lucro_por_produto = {}
    for venda in vendas:
        produto_vendido = venda['produto']
        quantidade_vendida = venda['quantidade']
        produto = next((p for p in produtos if p['nome'] == produto_vendido), None)
        if produto:
            lucro_unitario = produto['preco_venda'] - produto['preco_custo']
            lucro_total = lucro_unitario * quantidade_vendida
            if produto_vendido in lucro_por_produto:
                lucro_por_produto[produto_vendido] += lucro_total
            else:
                lucro_por_produto[produto_vendido] = lucro_total

    print("Relatório de Lucro por Produto:")
    for produto, lucro in lucro_por_produto.items():
        print(f"Produto: {produto}, Lucro Total: R${lucro:.2f}")

    input("Pressione Enter para continuar...")
    clear_screen()

def relatorio_despesas_por_categoria():
    clear_screen()
    despesas_agrupadas = {}
    for despesa in despesas:
        tipo = despesa['tipo']
        valor = despesa['valor']
        if tipo in despesas_agrupadas:
            despesas_agrupadas[tipo] += valor
        else:
            despesas_agrupadas[tipo] = valor

    print("Relatório de Despesas por Categoria:")
    for tipo, valor in despesas_agrupadas.items():
        print(f"Categoria: {tipo}, Total Gasto: R${valor:.2f}")

    input("Pressione Enter para continuar...")
    clear_screen()

def relatorio_compras_por_produto():
    clear_screen()
    compras_agrupadas = {}
    compras = carregar_dados('compras.txt')
    for compra in compras:
        produto = compra['produto']
        quantidade = compra['quantidade']
        if produto in compras_agrupadas:
            compras_agrupadas[produto] += quantidade
        else:
            compras_agrupadas[produto] = quantidade

    print("Relatório de Compras por Produto:")
    for produto, quantidade in compras_agrupadas.items():
        print(f"Produto: {produto}, Quantidade Comprada: {quantidade}")

    input("Pressione Enter para continuar...")
    clear_screen()

# Menu para relatórios
def relatorios():
    while True:
        clear_screen()
        print("\nRelatórios")
        print("1. Relatório de Estoque")
        print("2. Relatório Financeiro")
        print("3. Relatório de Produtos Mais Vendidos")
        print("4. Relatório de Produtos com Menor Estoque")
        print("5. Relatório de Lucro por Produto")
        print("6. Relatório de Despesas por Categoria")
        print("7. Relatório de Compras por Produto")
        print("8. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_estoque()
        elif opcao == "2":
            visualizar_relatorios_financeiros()
        elif opcao == "3":
            relatorio_produtos_mais_vendidos()
        elif opcao == "4":
            relatorio_produtos_com_menor_estoque()
        elif opcao == "5":
            relatorio_lucro_por_produto()
        elif opcao == "6":
            relatorio_despesas_por_categoria()
        elif opcao == "7":
            relatorio_compras_por_produto()
        elif opcao == "8":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

# FEATURE 06: CONFIGURAÇÕES -------------------------------------------------------------------

# Menu de configurações
def configuracoes():
    while True:
        clear_screen()
        print("\nConfigurações")
        print("1. Mudar Login e Senha")
        print("2. Resetar Todos os Dados")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mudar_login_senha()
        elif opcao == "2":
            resetar_dados()
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
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

# Função para resetar os dados (estoque, vendas, despesas, compras)
def resetar_dados():
    clear_screen()
    print("ATENÇÃO: Você está prestes a resetar todos os dados do sistema!")
    print("Essa ação não pode ser desfeita e você perderá todo o histórico de estoque, vendas, despesas e compras.")
    
    confirmacao = input("Digite 'sim' para confirmar o reset ou qualquer outra tecla para cancelar: ").lower()
    
    if confirmacao == 'sim':
        # Limpar os arquivos recriando-os vazios
        salvar_dados('produtos.txt', [])
        salvar_dados('vendas.txt', [])
        salvar_dados('despesas.txt', [])
        salvar_dados('compras.txt', [])
        
        print("Todos os dados foram resetados com sucesso!")
    else:
        print("Operação de reset cancelada.")
    
    input("Pressione Enter para continuar...")
    clear_screen()

# FEATURE 08: HISTÓRICO DE COMPRAS -------------------------------------------------------------

# Função para registrar automaticamente a compra
def registrar_compra_automatico(nome_produto, quantidade_comprada, preco_custo):
    data_atual = datetime.now().strftime('%d/%m/%Y')
    
    compra = {
        "produto": nome_produto,
        "quantidade": quantidade_comprada,
        "preco": preco_custo,
        "data": data_atual
    }

    compras = carregar_dados('compras.txt')
    compras.append(compra)
    salvar_dados('compras.txt', compras)

# Função para visualizar o histórico de compras
def visualizar_historico_compras():
    compras = carregar_dados('compras.txt')

    if not compras:
        print("Nenhuma compra registrada!")
    else:
        print("\nHistórico de Compras:")
        for compra in compras:
            print(f"Produto: {compra['produto']}, Quantidade: {compra['quantidade']}, Preço: R${compra['preco']:.2f}, Data: {compra['data']}")

    input("Pressione Enter para continuar...")
    clear_screen()

# FEATURE 09: FILTROS ---------------------------------------------------------------------------

# Função para aplicar filtros nos dados
def filtrar_dados(lista_dados, chave, valor):
    """Filtra uma lista de dados com base em uma chave e um valor fornecidos"""
    return [item for item in lista_dados if str(item[chave]).lower() == valor.lower()]

# Função para exibir dados filtrados com melhor formatação
def exibir_dados_filtrados(dados, titulo):
    """Exibe os dados filtrados de forma organizada e formatada"""
    if not dados:
        print(f"\nNenhum dado encontrado para {titulo} com esse filtro.")
    else:
        print(f"\n--- {titulo} ---")
        for dado in dados:
            if 'nome' in dado:  # Produto
                print(f"Produto: {dado['nome']}, Quantidade: {dado['quantidade']}, Preço de Custo: R${dado['preco_custo']:.2f}, Preço de Venda: R${dado['preco_venda']:.2f}")
            elif 'produto' in dado:  # Vendas ou Compras
                print(f"Produto: {dado['produto']}, Quantidade: {dado['quantidade']}, Preço: R${dado.get('preco', 0):.2f}, Data: {dado['data']}")
            elif 'tipo' in dado:  # Despesa
                print(f"Tipo de Despesa: {dado['tipo']}, Valor: R${dado['valor']:.2f}, Data: {dado['data']}")
            else:
                print(dado)

    input("\nPressione Enter para continuar...")
    clear_screen()

# Função para filtrar produtos com tratamento de erro
def filtrar_produtos():
    clear_screen()
    print("Filtrar Produtos")
    print("1. Categoria")
    print("2. Quantidade Disponível (Máximo)")
    print("3. Preço de Custo (Máximo)")
    print("4. Preço de Venda (Máximo)")
    opcao = input("Escolha uma opção de filtro: ")

    try:
        if opcao == "1":
            categoria = input("Digite a categoria: ")
            produtos_filtrados = filtrar_dados(produtos, 'categoria', categoria)
            exibir_dados_filtrados(produtos_filtrados, "Produtos")
        elif opcao == "2":
            quantidade_max = int(input("Digite a quantidade máxima: "))
            produtos_filtrados = [produto for produto in produtos if produto['quantidade'] <= quantidade_max]
            exibir_dados_filtrados(produtos_filtrados, "Produtos")
        elif opcao == "3":
            preco_custo_max = float(input("Digite o preço de custo máximo: "))
            produtos_filtrados = [produto for produto in produtos if produto['preco_custo'] <= preco_custo_max]
            exibir_dados_filtrados(produtos_filtrados, "Produtos")
        elif opcao == "4":
            preco_venda_max = float(input("Digite o preço de venda máximo: "))
            produtos_filtrados = [produto for produto in produtos if produto['preco_venda'] <= preco_venda_max]
            exibir_dados_filtrados(produtos_filtrados, "Produtos")
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
    except ValueError:
        print("\nErro: Por favor, insira um valor numérico válido.")
        input("Pressione Enter para tentar novamente...")
        clear_screen()

# Função para filtros de vendas com tratamento de erro
def filtrar_vendas():
    clear_screen()
    print("Filtrar Vendas")
    print("1. Nome do Produto")
    print("2. Data da Venda")
    print("3. Quantidade Vendida (Mínimo)")
    print("4. Preço de Venda (Máximo)")
    opcao = input("Escolha uma opção de filtro: ")

    try:
        if opcao == "1":
            nome_produto = input("Digite o nome do produto: ")
            vendas_filtradas = filtrar_dados(vendas, 'produto', nome_produto)
            exibir_dados_filtrados(vendas_filtradas, "Vendas")
        elif opcao == "2":
            data_venda = input("Digite a data da venda (dd/mm/yyyy): ")
            vendas_filtradas = filtrar_dados(vendas, 'data', data_venda)
            exibir_dados_filtrados(vendas_filtradas, "Vendas")
        elif opcao == "3":
            quantidade_min = int(input("Digite a quantidade mínima vendida: "))
            vendas_filtradas = [venda for venda in vendas if venda['quantidade'] >= quantidade_min]
            exibir_dados_filtrados(vendas_filtradas, "Vendas")
        elif opcao == "4":
            preco_venda_max = float(input("Digite o preço de venda máximo: "))
            vendas_filtradas = [venda for venda in vendas if venda['preco'] <= preco_venda_max]
            exibir_dados_filtrados(vendas_filtradas, "Vendas")
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
    except ValueError:
        print("\nErro: Por favor, insira um valor numérico válido.")
        input("Pressione Enter para tentar novamente...")
        clear_screen()

# Função para filtros de compras com tratamento de erro
def filtrar_compras():
    clear_screen()
    print("Filtrar Compras")
    print("1. Nome do Produto")
    print("2. Data da Compra")
    print("3. Quantidade Comprada (Mínimo)")
    print("4. Preço de Compra (Máximo)")
    opcao = input("Escolha uma opção de filtro: ")

    try:
        if opcao == "1":
            nome_produto = input("Digite o nome do produto: ")
            compras_filtradas = filtrar_dados(compras, 'produto', nome_produto)
            exibir_dados_filtrados(compras_filtradas, "Compras")
        elif opcao == "2":
            data_compra = input("Digite a data da compra (dd/mm/yyyy): ")
            compras_filtradas = filtrar_dados(compras, 'data', data_compra)
            exibir_dados_filtrados(compras_filtradas, "Compras")
        elif opcao == "3":
            quantidade_min = int(input("Digite a quantidade mínima comprada: "))
            compras_filtradas = [compra for compra in compras if compra['quantidade'] >= quantidade_min]
            exibir_dados_filtrados(compras_filtradas, "Compras")
        elif opcao == "4":
            preco_compra_max = float(input("Digite o preço de compra máximo: "))
            compras_filtradas = [compra for compra in compras if compra['preco'] <= preco_compra_max]
            exibir_dados_filtrados(compras_filtradas, "Compras")
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
    except ValueError:
        print("\nErro: Por favor, insira um valor numérico válido.")
        input("Pressione Enter para tentar novamente...")
        clear_screen()

# Função para filtros de despesas com tratamento de erro
def filtrar_despesas():
    clear_screen()
    print("Filtrar Despesas")
    print("1. Tipo de Despesa")
    print("2. Data da Despesa")
    print("3. Valor da Despesa (Máximo)")
    opcao = input("Escolha uma opção de filtro: ")

    try:
        if opcao == "1":
            tipo_despesa = input("Digite o tipo de despesa: ")
            despesas_filtradas = filtrar_dados(despesas, 'tipo', tipo_despesa)
            exibir_dados_filtrados(despesas_filtradas, "Despesas")
        elif opcao == "2":
            data_despesa = input("Digite a data da despesa (dd/mm/yyyy): ")
            despesas_filtradas = filtrar_dados(despesas, 'data', data_despesa)
            exibir_dados_filtrados(despesas_filtradas, "Despesas")
        elif opcao == "3":
            valor_max = float(input("Digite o valor máximo da despesa: "))
            despesas_filtradas = [despesa for despesa in despesas if despesa['valor'] <= valor_max]
            exibir_dados_filtrados(despesas_filtradas, "Despesas")
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
    except ValueError:
        print("\nErro: Por favor, insira um valor numérico válido.")
        input("Pressione Enter para tentar novamente...")
        clear_screen()

# Função menu dos filtros
def menu_filtros():
    while True:
        clear_screen()
        print("Menu de Filtros")
        print("1. Filtrar Produtos")
        print("2. Filtrar Vendas")
        print("3. Filtrar Compras")
        print("4. Filtrar Despesas")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            filtrar_produtos()
        elif opcao == "2":
            filtrar_vendas()
        elif opcao == "3":
            filtrar_compras()
        elif opcao == "4":
            filtrar_despesas()
        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
        clear_screen()

# FEATURE 10: SUGESTÕES ---------------------------------------------------------------------------

# Sugestões de reabastecimento, ajuste de preço e promoções
def sugestao_reabastecimento():
    produtos_com_baixo_estoque = [produto for produto in produtos if produto['quantidade'] < 10]
    if produtos_com_baixo_estoque:
        return True, "Produtos com estoque abaixo de 10 unidades precisam ser reabastecidos."
    return False, "Nenhum produto necessita de reabastecimento no momento."

def sugestao_ajuste_preco():
    produtos_com_margem_baixa = [produto for produto in produtos if (produto['preco_venda'] - produto['preco_custo']) < 5]
    if produtos_com_margem_baixa:
        return True, "Produtos com margem de lucro inferior a R$5 devem ter o preço ajustado."
    return False, "Nenhum produto necessita de ajuste de preço no momento."

def sugestao_promocao():
    produtos_para_promocao = [produto for produto in produtos if produto['quantidade'] > 50 and 
                              not any(venda['produto'] == produto['nome'] for venda in vendas)]
    if produtos_para_promocao:
        return True, "Há produtos com vendas baixas e estoque alto que podem entrar em promoção."
    return False, "Nenhum produto necessita de promoção no momento."

# Função para coletar todas as sugestões possíveis
def verificar_sugestoes():
    # Retorna todas as sugestões, mesmo as que não estão disponíveis no momento
    sugestoes = [
        ("Reabastecimento", *sugestao_reabastecimento()),
        ("Ajuste de Preço", *sugestao_ajuste_preco()),
        ("Promoções", *sugestao_promocao())
    ]
    return sugestoes

# Menu de sugestões
def menu_sugestoes():
    clear_screen()
    sugestoes = verificar_sugestoes()

    print("Sugestões Disponíveis:")
    for idx, (titulo, _, _) in enumerate(sugestoes, 1):
        print(f"{idx}. {titulo}")
    print(f"{len(sugestoes) + 1}. Voltar ao Menu Principal")

    opcao = input("\nEscolha uma sugestão para visualizar ou digite o número para voltar: ")

    try:
        opcao = int(opcao)
        if opcao == len(sugestoes) + 1:
            return  # Volta ao menu principal
        elif 1 <= opcao <= len(sugestoes):
            titulo, disponivel, detalhe = sugestoes[opcao - 1]
            clear_screen()
            print(f"--- {titulo} ---")
            if disponivel:
                print(detalhe)
            else:
                print(f"Ainda não há dados para {titulo}. {detalhe}")
        else:
            print("Opção inválida!")
    except ValueError:
        print("Por favor, insira um número válido.")

    input("\nPressione Enter para continuar...")

# Iniciar o programa chamando a função de login
if __name__ == "__main__":
    login()