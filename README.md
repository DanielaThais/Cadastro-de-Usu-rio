# Sistema de Autenticação em Python

Este repositório contém uma implementação simples e funcional de um sistema de autenticação, desenvolvido em Python, utilizando hashing SHA-256 para armazenamento seguro de senhas.
O sistema permite cadastrar usuários, realizar login e excluir contas, tudo através de um menu interativo no terminal.

## 🛠️ Funcionalidades

    - Cadastro de usuários
    
    - Armazenamento de matrícula e hash da senha -> Impede cadastro duplicado.
    
    - Login seguro -> As senhas informadas são convertidas em hash e comparadas com o hash armazenado.
    
    - Exclusão de usuários -> Remove contas pelo número de matrícula.
    
    - Menu interativo -> Interface no terminal para uso simplificado.

## 🔐 Segurança

As senhas não são armazenadas em texto puro.
Para gerar o hash da senha antes de salvar, tornando o processo mais seguro e adequado para fins didáticos, o sistema utiliza:

    hashlib.sha256()

## 📁 Estrutura do Código

> Classe SistemaAutenticacao

> Gerencia cadastro, login e exclusão.

> Armazena usuários em um dicionário:

    { matricula: hash_senha }

> Função _gerar_hash_senha

> Converte a senha em hash SHA-256.

> Função menu_interativo

> Exibe o menu e faz a interação com o usuário.

## ▶️ Como Executar

Certifique-se de ter o Python 3.x instalado.

Clone o repositório:

    git clone https://github.com/seu-usuario/seu-repositorio.git

Acesse a pasta:

    cd seu-repositorio

Execute o programa:

    python nome_do_arquivo.py

## 🖥️ Exemplo de Uso

<img width="349" height="203" alt="image" src="https://github.com/user-attachments/assets/2496882b-f217-4c59-8a50-a00a1f0d525b" />

### 📌 Observações

Este sistema utiliza um “banco de dados” em memória (um dicionário). Ao encerrar o programa, os dados são perdidos. Para uma aplicação real, seria necessário integrar com um banco de dados persistente (que está em andamento).

O projeto é ideal para fins educacionais: estudo de hashing, classes e interação via terminal.
