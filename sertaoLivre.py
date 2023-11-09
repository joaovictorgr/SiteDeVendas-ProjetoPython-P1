def Menu():
    print(20 * '-')
    print('--------MENU--------')
    print(20 * '-')

def Linha():
    print(20 * '-')

vendedor = dict()
op = 99

print('\nSeja Bem Vindo ao Sertão Livre, seu site de compras e vendas!\n')

while(op != 0):
    Menu()
    print('1- Cadastrar vendedor')
    print('2- Fazer login')
    print('3- Menu cliente')
    print('0- Sair do site')
    Linha()
    op = int(input('\nDigite a opção desejada:'))

    if(op == 1):
        Linha()
        usuario = input('\nDigite um nome para usuário:')
        cpf = input('Digite seu CPF:')
        nome = input('Digite seu nome completo:')
        idade = int(input('Digite sua idade:'))
        sexo = input('Digite seu gênero sexual:')
        est_civil = input('Digite seu estado civil:')
        senha = input('Digite uma senha:')
        Linha()
        vendedor[usuario] = {'CPF': cpf, 'Nome': nome, 'Idade': idade, 'Sexo': sexo, 'Estado Civil': est_civil,'Senha': senha, 'Produtos':{}}

        print(f'\nVendedor {nome} cadastrado com sucesso!')

    elif (op == 2):
        Linha()
        usuario = input('\nUsuário:')
        senha = input('Senha:')
        Linha()

        if (usuario in vendedor.keys() and senha == vendedor[usuario]['Senha']):
            print('\nLogin efetuado com sucesso!')

            op2 = 99
            while (op2 != 0):
                Menu()
                print('1- Atualizar senha')
                print('2- Adicionar produto')
                print('3- Atualizar produto')
                print('4- Remover produto')
                print('5- Buscar produto')
                print('0- Sair')
                Linha()

                op2 = int(input('\nDigite a opção desejada:'))

                if (op2 == 1):
                    nova_senha = input('\nDigite uma nova senha:')
                    vendedor[usuario]['Senha'] = nova_senha
                    print('\nSenha atualizada com sucesso!')

                elif (op2 == 2):
                    Linha()
                    nome_produto = input('\nDigite o nome do seu produto:')
                    preco_produto = float(input('Digite o preço do seu produto: R$'))
                    codigo_produto = input('Digite o código do produto: ')
                    descricao_produto = input('Digite a descrição do produto: ')
                    Linha()
                    vendedor[usuario]['Produtos'][nome_produto] = {'Preço': preco_produto, 'Código': codigo_produto, 'Descrição': descricao_produto}
                    print(f'\nProduto {nome_produto} adicionado com sucesso!')

                elif (op2 == 3):
                    nome_produto = input('\nDigite o nome do produto que deseja atualizar:')
                    if nome_produto in vendedor[usuario]['Produtos']:
                        novo_preco = float(input('Digite o novo preço do seu produto: R$'))
                        vendedor[usuario]['Produtos'][nome_produto]['Preço'] = novo_preco
                        print(f'\nProduto {nome_produto} atualizado com sucesso!')
                    else:
                        print(f'\nProduto {nome_produto} não encontrado.')

                elif (op2 == 4):
                    nome_produto = input('\nDigite o nome do produto a ser removido:')
                    if nome_produto in vendedor[usuario]['Produtos']:
                        del vendedor[usuario]['Produtos'][nome_produto]
                        print(f'\nProduto {nome_produto} removido com sucesso!')
                    else:
                        print(f'\nProduto {nome_produto} não encontrado.')

                elif (op2 == 5):
                    nome_produto = input('\nDigite o nome do produto a ser buscado: ')
                    if nome_produto in vendedor[usuario]['Produtos']:
                        produto = vendedor[usuario]['Produtos'][nome_produto]
                        Linha()
                        print(f'Nome: {nome_produto} / Código: {codigo_produto} / Preço: R${preco_produto}'
                              f'\nDescrição: {descricao_produto}')
                        Linha()

                    else:
                        print(f'O produto "{nome_produto}" não foi encontrado.')

                elif (op2 == 0):
                    Linha()
                    print('Saindo do menu de opções...')
                    Linha()
                else:
                    Linha()
                    print('Opção inválida.')
                    Linha()
        else:
            Linha()
            print('Opção inválida!')
            Linha()

    elif (op == 3):
        op3 = 99
        while (op3 != 0):
            Menu()
            print('1- Buscar produto por nome')
            print('2- Comprar produto')
            Linha()

            op3 = int(input('\nDigite a opção desejada:'))

            if (op3 == 1):
                nome_produto = input('\nDigite o nome do produto a ser buscado: ')
                produto_encontrado = False
                for v in vendedor.values():
                    if nome_produto in v['Produtos']:
                        produto = v['Produtos'][nome_produto]
                        Linha()
                        print(f'Nome: {nome_produto} / Código: {codigo_produto} Preço: R${preco_produto:.2f}'
                              f'\nDescrição: {descricao_produto}')
                        Linha()
                        produto_encontrado = True
                        break
                if not produto_encontrado:
                    print(f'O produto "{nome_produto}" não foi encontrado.')

            elif (op3 == 2):
                codigo_produto = input('Depois de analisar os produtos na opção "1", digite aqui o código do produto que deseja fazer a compra: ')
                produto_encontrado = False
                for v in vendedor.values():
                    for p in v['Produtos'].values():
                        if codigo_produto == p['Código']:
                            print(f'\nProduto "{p["Nome"]}" comprado com sucesso!')
                            produto_encontrado = True
                            break
                    if produto_encontrado:
                        break
                if not produto_encontrado:
                    print(f'O produto com código "{codigo_produto}" não foi encontrado.')

        else:
            Linha()
            print('Opção inválida.')
            Linha()
