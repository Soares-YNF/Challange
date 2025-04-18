# 🏥 Sistema de Gerenciamento de Pacientes - Hospital das Clínicas

Este é um projeto em Python desenvolvido com o objetivo de gerenciar pacientes de forma simples e interativa por meio de um menu no terminal. O sistema permite **cadastrar, listar, buscar, alterar e excluir pacientes** utilizando o CPF como identificador.

## 📋 Funcionalidades

O sistema possui as seguintes funcionalidades:

### 1. Cadastrar Paciente
- O usuário insere o **nome**, **CPF** e **idade**.
- A idade é validada para garantir que seja um número.

### 2. Listar Pacientes
- Mostra todos os pacientes cadastrados com seus dados: nome, CPF e idade.
- Se não houver pacientes, informa que a lista está vazia.

### 3. Buscar Paciente por CPF
- O usuário digita o CPF desejado.
- O sistema procura o paciente correspondente e exibe seus dados, se encontrado.

### 4. Alterar Dados do Paciente
- Busca o paciente pelo CPF.
- Permite atualizar nome, CPF e idade com validação da nova idade.
- Caso o paciente não seja encontrado, exibe uma mensagem apropriada.

### 5. Excluir Paciente
- Busca o paciente pelo CPF.
- Remove o paciente da lista se for encontrado.
- Exibe confirmação da exclusão ou mensagem caso o CPF não seja encontrado.

### 0. Sair
- Finaliza o programa.

## 🧠 Tecnologias utilizadas

- **Python 3**: Linguagem principal do projeto.
- **Estrutura de dados (listas e dicionários)**.
- **Funções** para modularização do código.
- **Laços de repetição e validações** para entrada do usuário.

## 🚀 Como executar

1. Certifique-se de que o Python 3 está instalado em seu computador.
2. Clone este repositório ou copie o código para um arquivo `.py`.
3. Execute o arquivo no terminal com o comando:

```bash
python nome_do_arquivo.py
