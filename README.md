# Sistema de Controle de Estoque e Financeiro
Este é um programa simples e didático, criado com o objetivo de ajudar a gerenciar um pequeno negócio, organizando o estoque de produtos, registrando vendas, controlando despesas e gerando relatórios. Abaixo, você encontrará uma explicação detalhada das funcionalidades, as bibliotecas utilizadas e uma visão geral do código.
## Funcionalidades

### 1. **Login do Usuário**
- O programa possui um sistema de login básico para garantir que apenas usuários autorizados possam acessá-lo. O login padrão é:
  - **Usuário:** `admin`
  - **Senha:** `senha123`
- A função `login()` verifica se o usuário e senha fornecidos são válidos antes de permitir o acesso ao sistema.

### 2. **Menu Principal**
- Após o login, o usuário acessa o menu principal, que dá acesso às funcionalidades do programa:
  - Controle de Estoque
  - Controle Financeiro
  - Relatórios
  - Configurações
  - Filtros de Dados
  - Sugestões
  - Sair

### 3. **Controle de Estoque**
- Esta funcionalidade permite gerenciar o estoque de produtos do sistema. As opções incluem:
  - **Adicionar Produto:** Permite incluir novos produtos ao estoque.
  - **Atualizar Produto:** Atualiza informações de um produto existente, como nome, preço ou quantidade.
  - **Remover Produto:** Remove um produto do estoque.
  - **Visualizar Estoque:** Exibe a lista completa de produtos disponíveis no estoque.
  - **Histórico de Compras:** Mostra todas as compras registradas.

### 4. **Controle Financeiro**
- Este menu permite registrar vendas e despesas, além de visualizar o saldo financeiro:
  - **Registro de Vendas:** Registra uma nova venda, atualizando o estoque e o saldo.
  - **Registro de Despesas:** Adiciona uma nova despesa ao sistema.
  - **Visualizar Relatórios Financeiros:** Mostra um resumo das vendas e despesas, exibindo o lucro total.

### 5. **Relatórios**
- Diversos relatórios estão disponíveis para ajudar na gestão do negócio:
  - **Relatório de Produtos Mais Vendidos:** Lista os produtos com maior volume de vendas.
  - **Relatório de Produtos com Menor Estoque:** Exibe os produtos com menor quantidade em estoque.
  - **Relatório de Lucro por Produto:** Mostra o lucro gerado por cada produto.
  - **Relatório de Despesas por Categoria:** Agrupa as despesas por tipo e exibe o total gasto em cada categoria.
  - **Relatório de Compras por Produto:** Exibe a quantidade de cada produto comprada ao longo do tempo.

### 6. **Filtros**
- O programa permite filtrar dados de produtos, vendas, despesas e compras, facilitando a busca por informações específicas. Por exemplo, você pode filtrar os produtos por categoria ou preço máximo, as vendas por data ou quantidade, entre outros critérios.

### 7. **Sugestões**
- O sistema oferece sugestões automáticas para ajudar na gestão do estoque:
  - **Reabastecimento:** Produtos com baixo estoque.
  - **Ajuste de Preço:** Produtos com margem de lucro baixa.
  - **Promoções:** Produtos com estoque alto e poucas vendas.

### 8. **Configurações**
- O usuário pode:
  - Alterar o nome de usuário e senha.
  - Resetar todos os dados do sistema (estoque, vendas, despesas, etc.).

## Bibliotecas Utilizadas

Este programa utiliza algumas bibliotecas padrão do Python para lidar com operações básicas:

- **`os`**: Usada para limpar a tela, dependendo do sistema operacional (Windows ou Linux/macOS).
- **`json`**: Para ler e escrever dados em arquivos `.txt` no formato JSON, que facilita a organização das informações.

## Conceitos Importantes

### 2. **Try e Except**
- O bloco `try` e `except` é usado para tratar erros. Por exemplo, ao pedir que o usuário insira um número, erros podem acontecer se ele digitar letras em vez de números. O `try` tenta executar o código, e se algo der errado, o `except` captura o erro e exibe uma mensagem amigável ao usuário, em vez de parar o programa abruptamente.

- A função `any()` é usada no programa para verificar se há pelo menos um item em uma lista que atende a uma condição. Por exemplo, no sistema de sugestões, a função `any()` é usada para verificar se há produtos no estoque com vendas baixas e grande quantidade, sugerindo que esses produtos podem entrar em promoção.

## Guia de navegação pelo código
  Para facilitar a navegação do código eu enumerei as funcionalidades, para ir até determinada funcionalidade basta pesquisar pelo número ao invés de procurar por todo o código, segue abaixo a numeração:
  - 01 Login
  - 02 Menu principal
  - 03 Controle de estoque
  - 04 Controle Financeiro
  - 05 Relatórios
  - 06 Configurações
  - 07 Exibição de dados
  - 08 Histórico de compras
  - 09 Filtros
  - 10 Sugestões

## Fluxograma
Segue abaixo o link para acessar o fluxograma do código (projeto) <br> [Fluxograma](https://drive.google.com/file/d/1jqZXmKtdp-6-nEeoddlaPEWiUNkSab-u/view?usp=sharing)
