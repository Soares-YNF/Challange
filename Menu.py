pacientes = []  # Lista para armazenar os pacientes

# Função para cadastrar o paciente
def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF do paciente: ")
    idade = input("Digite a idade do paciente: ")

    # Verificando se a idade é um número inteiro
    while not idade.isdigit():
        idade = input("Idade inválida! Digite uma idade válida: ")

    idade = int(idade)  # Convertendo para inteiro

    paciente = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade
    }

    pacientes.append(paciente)  # Adicionando paciente à lista

    print(f"Paciente {nome} cadastrado com sucesso!")

#Criando a lista de pacientes
def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        print("\n Lista de Pacientes: ")
        for paciente in pacientes:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Idade: {paciente['idade']}")

#Criando a busca do paciente pelo CPF
def buscar_paciente_por_cpf(cpf):
    for paciente in pacientes:
        if paciente["cpf"] == cpf:
            return paciente
    return None

#Criando o Alterar Dados do paciente
def alterar_dados_paciente(cpf):
    paciente_encontrado = buscar_paciente_por_cpf(cpf)
    if paciente_encontrado:
        nome = input("Digite o novo nome do paciente: ")
        cpf = input("Digite o novo CPF do paciente: ")
        Nova_idade = input("Digite a nova idade do paciente: ")
        while not Nova_idade.isdigit():
                        Nova_idade = input("Idade Inválida! Digite uma idade válida: ")
        idade = int(Nova_idade)
        paciente_encontrado["nome"] = nome
        paciente_encontrado["cpf"] = cpf
        paciente_encontrado["idade"] = idade
        print("Dados alterados com sucesso!")
        return paciente_encontrado

        #Criando o Excluir paciente
def excluir_paciente(cpf):
    paciente_encontrado = buscar_paciente_por_cpf(cpf)
    pacientes.remove(paciente_encontrado)
    if paciente_encontrado:
        print("Paciente excluido com sucesso")
    else:
        print("Paciente não encotrado")


# Função para exibir o menu
def exibir_menu(cpf=None):
    opcao = ""
    while opcao != "0":
        print("\n---Menu Do Hospital Das Clínicas---")
        print("1- Cadastrar Paciente")
        print("2- Listar Paciente")
        print("3- Buscar Paciente por CPF")
        print("4- Alterar Dados do Paciente")
        print("5- Excluir Paciente")
        print("0- Sair")

        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            cadastrar_paciente()

        elif opcao == "2":
            listar_pacientes()


        elif opcao == "3":
            cpf = input("Digite o CPF que deseja procurar: ")
            paciente_encontrado  = buscar_paciente_por_cpf(cpf)

            if pacientes:
                print(f"Paciente encontrado!: Nome {paciente_encontrado[0]['nome']}, CPF {paciente_encontrado[0]['cpf']}, Idade {pacientes[0]['idade']}")
            else:
                print("Paciente não encontrado")

        elif opcao == "4":
            print("Alterando Dados do Paciente")
            cpf = input("Digite o CPF do paciente que deseja alterar: ")
            paciente_encontrado = buscar_paciente_por_cpf(cpf)
            if paciente_encontrado:
                alterar_dados_paciente(cpf)
            else:
                print("Nenhum paciente encontrado!")


        elif opcao == "5":
            print("Excluindo Paciente")
            cpf = input("Digite o CPF do paciente que deseja excluir: ")
            excluir_paciente(cpf)


        elif opcao == "0":
            print("Saindo...")

        else:
            print("Opção inválida! Tente uma opção válida.")

# Inicia o menu
exibir_menu()