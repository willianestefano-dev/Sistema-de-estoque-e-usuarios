# 🧸 Sistema de Estoque e Usuários

Sistema completo de gerenciamento de estoque desenvolvido em Python com controle de usuários e níveis de acesso.

## ✨ Funcionalidades

- 🔐 **Login seguro** com níveis de acesso (Admin e Funcionário)
- 📦 **CRUD de produtos** (cadastrar, listar, buscar, alterar, remover)
- 👤 **CRUD de usuários** (apenas administradores)
- 📊 **Relatórios gerenciais**:
  - Valor total do estoque
  - Quantidade total de produtos
  - Produtos com estoque baixo (menos de 5 unidades)
- 💾 **Persistência em JSON** (dados salvos automaticamente)
- ✅ **Validações robustas** em todos os campos

## 👥 Tipos de Usuário

| Tipo | Permissões |
|------|------------|
| **Admin** | Acesso total: CRUD produtos, CRUD usuários, relatórios |
| **Funcionário** | Cadastrar produtos e buscar produtos |

## 🛠️ Tecnologias

- Python 3.x
- JSON (persistência de dados)
- Programação Orientada a Objetos (POO)

## 📂 Estrutura do Projeto

Sistema-de-estoque-e-usuarios/
├── sistema_de_estoque_e_usuarios.py # Código principal
├── dados/ # Pasta de dados (criada automaticamente)
│ ├── usuarios.json # Dados dos usuários
│ └── brinquedos.json # Dados dos produtos
└── README.md

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/willianestefano-dev/Sistema-de-estoque-e-usuarios.git

# Entre na pasta
cd Sistema-de-estoque-e-usuarios

# Execute o sistema
python sistema_de_estoque_e_usuarios.py

🔧 Melhorias Futuras

    Interface gráfica (Tkinter/PyQt)

    Banco de dados (SQLite/PostgreSQL)

    Sistema de vendas integrado

    Gerar relatórios em PDF

    Validação real de CPF (algoritmo)

    Upload de imagens para produtos

    Criptografia de senhas
