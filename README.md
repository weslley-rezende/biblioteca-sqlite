# Projeto Biblioteca – Python + SQLite

# Parte 1: Explicação do Código

O código executa uma sequência de 12 etapas que simulam operações básicas em um banco de dados relacional:
- Criação de tabelas (`Livros` e `Usuario`)
- Inserção de registros
- Atualização de dados
- Consultas (SELECT)
- Ordenação de resultados
- Exclusão de registros e tabelas

#Etapas implementadas

1. **Criação da tabela Livros**  
   Define os campos `id`, `titulo`, `autor`, `ano`, `genero` e `disponivel`.

2. **Inserção de 5 livros fictícios**

3. **Consulta de livros disponíveis** (`disponivel = 1`)

4. **Atualização de disponibilidade** de um livro específico

5. **Ordenação dos livros por ano** (do mais recente ao mais antigo)

6. **Remoção de livros com ano anterior a 1940**

7. **Criação da tabela Usuario**

8. **Alteração da tabela Usuario** para adicionar a coluna `idade` (com verificação para evitar erro de duplicidade)

9. **Inserção de 5 usuários fictícios**

10. **Exclusão completa da tabela Usuario** com `DROP TABLE`

Cada parte é comentada no código, tornando a leitura e entendimento mais fáceis.

---

# Como Executar o Projeto


# Passos para rodar

1. **Baixe ou clone** o repositório do projeto:
   ```bash
   git clone https://github.com/seu-usuario/projeto-biblioteca.git
   cd projeto-biblioteca
   ```

2. **Execute o script principal:**
   ```bash
   python biblioteca.py
   ```

3. O banco de dados (`biblioteca.db`) será criado automaticamente no mesmo diretório.

4. O terminal exibirá mensagens mostrando o andamento de cada etapa:
   ```
   Tabela 'Livros' criada com sucesso.
   5 livros inseridos com sucesso.
   Livros disponíveis:
   ...
   ```

5. Cada etapa pode ser testada individualmente dentro do código, conforme as instruções e comentários.

---

# Estrutura das Tabelas Criadas

# Tabela `Livros`

| Coluna       | Tipo      | Descrição                                   |
|---------------|-----------|---------------------------------------------|
| `id`          | INTEGER   | Chave primária (auto incremento)            |
| `titulo`      | TEXT      | Nome do livro (único e obrigatório)         |
| `autor`       | TEXT      | Nome do autor                              |
| `ano`         | INTEGER   | Ano de publicação                          |
| `genero`      | TEXT      | Gênero literário                           |
| `disponivel`  | INTEGER   | 1 = disponível / 0 = indisponível           |

# Tabela `Usuario`

| Coluna   | Tipo     | Descrição                              |
|-----------|----------|----------------------------------------|
| `id`     | INTEGER  | Chave primária (auto incremento)       |
| `nome`   | TEXT     | Nome do usuário                        |
| `idade`  | INTEGER  | Idade do usuário (adicionada depois)   |

---

# Estrutura de Arquivos

```
projeto-biblioteca/
│
├── biblioteca.py      # Script principal em Python (com etapas 1–12)
├── biblioteca.db      # Banco de dados SQLite (gerado automaticamente)
└── README.md          # Arquivo de explicação do projeto + Questões
```

# QUESTÕES


**Autor:** *WESLLEY REZENDE*  
*Versão 1.0 — Novembro/2025*
