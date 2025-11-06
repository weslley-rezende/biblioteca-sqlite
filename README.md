# Projeto Biblioteca – Python + SQLite

# Parte 1: Explicação do Código

O código executa uma sequência de 12 etapas que simulam operações básicas em um banco de dados relacional:
- Criação de tabelas (`Livros` e `Usuario`)
- Inserção de registros
- Atualização de dados
- Consultas (SELECT)
- Ordenação de resultados
- Exclusão de registros e tabelas

# ####################################################################

# Etapas implementadas

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

# ####################################################################


# Como Executar o Projeto


# Passos para rodar

1. **Baixe ou clone** o repositório do projeto:
   ```bash
   git clone https://github.com/weslley-rezende/biblioteca-sqlite.git
   cd meu-projeto-sql
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
# ####################################################################

# QUESTÕES

1. Por que os bancos de dados são essenciais em aplicações modernas? Bancos de dados são essenciais porque permitem o armazenamento persistente, organizado e eficiente de grandes volumes de dados. Eles garantem a integridade, segurança e disponibilidade das informações, permitindo que aplicações realizem consultas complexas, transações seguras (como em bancos ou e-commerce) e análises de dados, que são a base para a tomada de decisão em sistemas modernos. [Fonte: <https://prodest.es.gov.br/voce-sabe-por-que-os-bancos-de-dados-sao-tao-importantes ]

# ####################################################################

2. Quais são as duas principais categorias de bancos de dados existentes? As duas principais categorias são:

Relacionais (SQL): Armazenam dados em tabelas estruturadas (linhas e colunas) com um esquema (schema) predefinido. As relações entre tabelas são estabelecidas por chaves estrangeiras. Ex: MySQL, PostgreSQL, SQLite.

Não Relacionais (NoSQL): São mais flexíveis e não usam esquemas fixos. Existem vários tipos, como:

Documento: Armazenam dados em documentos (ex: JSON). Ex: MongoDB.

Chave-Valor: Armazenam dados em pares simples de chave e valor. Ex: Redis.

Grafos: Focados em relações complexas entre dados. Ex: Neo4j.

Colunares (Wide-Column): Otimizados para consultas em grandes volumes de dados por colunas. [Fonte: <https://kondado.com.br/blog/blog/2022/09/13/banco-de-dados-o-que-e-e-quais-sao-os-principais-tipos/]

# ####################################################################


3. Em quais cenários é recomendado utilizar um banco de dados relacional?
 É recomendado usar bancos de dados relacionais (SQL) quando a consistência e a integridade dos dados são cruciais (propriedades ACID), quando os dados são altamente estruturados e quando as relações entre eles são bem definidas. São ideais para sistemas financeiros, de reservas, acadêmicos e qualquer aplicação que dependa de transações seguras e confiáveis. [Fonte: <https://aws.amazon.com/pt/compare/the-difference-between-relational-and-non-relational-databases/]

# ####################################################################

 4. De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados?

CPU: Afeta a velocidade de processamento das consultas, especialmente cálculos, junções (joins) e ordenações complexas.

Memória (RAM): É crucial. Bancos de dados usam RAM para "cache" de dados frequentemente acessados. Quanto mais RAM, menos o sistema precisa ler do disco (que é muito mais lento), aumentando drasticamente a velocidade de leitura e escrita.

Disco (Armazenamento): A velocidade de leitura/escrita do disco (ex: SSD vs. HDD) impacta diretamente o tempo que o banco leva para buscar dados que não estão em cache ou para salvar alterações (persistência). [Fonte: <https://csbc.sbc.org.br/2023/wp-content/uploads/2023/08/JAI-4-Bancos-de-Dados-em-Memoria-e-suas-Estrategias-de-Recuperacao-Apos-Falhas.pdf]

# ####################################################################


5. O que significa escalabilidade no contexto de bancos de dados? Escalabilidade é a capacidade do banco de dados de lidar com um aumento na carga de trabalho (mais dados ou mais usuários/requisições). Existem duas formas principais:

Escalabilidade Vertical (Scale-up): Adicionar mais recursos a uma única máquina (mais CPU, mais RAM, SSD mais rápido). Tem um limite físico e custo elevado.

Escalabilidade Horizontal (Scale-out): Adicionar mais máquinas (servidores) ao sistema, distribuindo a carga entre elas. É a base dos sistemas NoSQL e de aplicações web modernas. [Fonte: <https://www.sysvision.global/blog/escalabilidade-de-dados]

# ####################################################################


6. Qual a relevância de organizar corretamente os dados em bancos relacionais? A organização correta, geralmente alcançada pela normalização, é vital para:

Minimizar a Redundância: Evita que a mesma informação seja armazenada múltiplas vezes, economizando espaço.

Garantir a Integridade: Previne "anomalias" de inserção, atualização ou exclusão. Por exemplo, se um cliente muda de endereço, você só precisa atualizar em um local.

Facilitar Consultas: Embora a normalização excessiva possa complicar algumas consultas (exigindo mais joins), ela torna o modelo de dados mais lógico e previsível. [Fonte: <https://www.web.coletum.com/post/qual-a-import%C3%A2ncia-de-organizar-dados-de-forma-estrat%C3%A9gica]

# ####################################################################


7. Como escolher entre SQL e NoSQL para um novo projeto? A escolha depende dos requisitos da aplicação:

Escolha SQL (Relacional) se: Você precisa de consistência transacional forte (ACID), seus dados são estruturados e as relações são fundamentais.

Escolha NoSQL (Não Relacional) se: Você precisa de altíssima escalabilidade horizontal, seus dados são não estruturados ou semiestruturados (JSON, etc.), a flexibilidade do esquema é importante e a "consistência eventual" é aceitável. [Fonte: <https://appwrite.io/blog/post/sql-vs-nosql]

# ####################################################################


# Comandos SQL

1. Qual é a finalidade do comando SELECT em SQL? O SELECT é usado para consultar ou recuperar dados de uma ou mais tabelas do banco de dados. É o comando mais usado em SQL, permitindo especificar quais colunas retornar, de quais tabelas, e aplicar filtros (com WHERE), ordenação (com ORDER BY) e agrupamentos. [Fonte: <https://www.alura.com.br/artigos/sql-consultas-com-select?utm_term=&utm_campaign=topo-aon-search-gg-dsa-artigos_conteudos&utm_source=google&utm_medium=cpc&campaign_id=11384329873_164212380672_703829166693&utm_id=11384329873_164212380672_703829166693&hsa_acc=7964138385&hsa_cam=topo-aon-search-gg-dsa-artigos_conteudos&hsa_grp=164212380672&hsa_ad=703829166693&hsa_src=g&hsa_tgt=dsa-425656816943&hsa_kw=&hsa_mt=&hsa_net=google&hsa_ver=3&gad_source=1&gad_campaignid=11384329873&gbraid=0AAAAADpqZIDT3G7XCjYmpGP7edYWmvvuS&gclid=Cj0KCQiAiKzIBhCOARIsAKpKLAM9ip5J-mZHOHbemGjYbpy-jGUHVOVIhxZRntMo4aIG2dN8c8Qcn-QaAoZsEALw_wcB]

# ####################################################################


2. O que significam as siglas DML e DDL em bancos de dados?

DDL (Data Definition Language / Linguagem de Definição de Dados): Comandos usados para definir ou modificar a estrutura do banco de dados e seus objetos (tabelas, índices, etc.). Principais comandos: CREATE, ALTER, DROP.

DML (Data Manipulation Language / Linguagem de Manipulação de Dados): Comandos usados para interagir com os dados dentro das tabelas. Principais comandos: SELECT, INSERT, UPDATE, DELETE. [Fonte: <https://www.dio.me/articles/o-que-sao-as-siglas-ddl-dml-dql-dtl-e-dcl]

# ####################################################################


3. Para que serve a cláusula WHERE em consultas SQL? A cláusula WHERE é usada para filtrar registros. Ela especifica as condições que uma linha deve atender para ser incluída nos resultados de um comando SELECT, ou para ser afetada por um UPDATE ou DELETE. [Fonte: <https://www.devmedia.com.br/sql-clausula-where/37645]

# ####################################################################


4. Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas? A Chave Primária (PRIMARY KEY) é fundamental porque ela identifica de forma única e inequívoca cada linha (registro) em uma tabela. Ela garante que não haja duplicidade de registros e serve como o principal "endereço" para relacionar dados entre tabelas (através de chaves estrangeiras). Além disso, ela é automaticamente indexada, o que torna as buscas por esse campo extremamente rápidas. [Fonte: <https://www.ibm.com/br-pt/think/topics/primary-key]

# ####################################################################

5. Como funciona o comando UPDATE e qual sua sintaxe básica? O comando UPDATE é usado para modificar registros existentes em uma tabela. Sua sintaxe básica é: UPDATE nome_da_tabela SET coluna1 = novo_valor1, coluna2 = novo_valor2 WHERE condicao; Atenção: Se a cláusula WHERE for omitida, o UPDATE será aplicado a todas as linhas da tabela. [Fonte: <https://www.alura.com.br/artigos/como-utilizar-os-comandos-insert-select-update-e-delete-em-sql?utm_term=&utm_campaign=topo-aon-search-gg-dsa-artigos_conteudos&utm_source=google&utm_medium=cpc&campaign_id=11384329873_164212380672_703829166693&utm_id=11384329873_164212380672_703829166693&hsa_acc=7964138385&hsa_cam=topo-aon-search-gg-dsa-artigos_conteudos&hsa_grp=164212380672&hsa_ad=703829166693&hsa_src=g&hsa_tgt=aud-527303763294:dsa-425656816943&hsa_kw=&hsa_mt=&hsa_net=google&hsa_ver=3&gad_source=1&gad_campaignid=11384329873&gbraid=0AAAAADpqZIDT3G7XCjYmpGP7edYWmvvuS&gclid=Cj0KCQiAiKzIBhCOARIsAKpKLAOtu-YMNyN7n44-inzJ1_KJKhzsAEtkzsE6c6qyK57qYIJp3RhWgGgaAlc7EALw_wcB]

# ####################################################################

6. Qual a função do comando DELETE em SQL? (Diferença entre DELETE e DROP)

DELETE: É um comando DML usado para remover uma ou mais linhas (registros) de uma tabela, geralmente com base em uma condição WHERE.

DROP: É um comando DDL usado para apagar completamente um objeto do banco de dados, como uma tabela inteira (DROP TABLE), um banco de dados (DROP DATABASE) ou um índice. O DROP é muito mais drástico que o DELETE. [Fonte: <https://learnsql.com.br/blog/truncate-table-vs-delete-vs-drop-table-excluindo-tabelas-e-dados-em-sql/]

# ####################################################################


7. Como a cláusula ORDER BY organiza os resultados de uma consulta? A cláusula ORDER BY é usada para classificar/ordenar os resultados de uma consulta SELECT com base em uma ou mais colunas. Por padrão, a ordem é ascendente (ASC). Para inverter a ordem, usa-se a palavra-chave descendente (DESC). [Fonte: <https://www.devmedia.com.br/sql-order-by/41225]

# ####################################################################


8. Para que serve o comando LIMIT em consultas SQL? O LIMIT (ou TOP em alguns bancos) é usado para restringir o número de linhas que uma consulta retorna. É muito usado para paginação (ex: "mostrar os 10 primeiros resultados") ou para encontrar os "N" maiores/menores valores (em conjunto com ORDER BY). [Fonte: <https://www.devmedia.com.br/sql-limit/41216]

# ####################################################################


# Outros Conceitos

1. Por que é importante integrar o banco de dados com a camada de back-end da aplicação? O back-end (camada do servidor) atua como o "cérebro" da aplicação e o intermediário entre o usuário (front-end) e o banco de dados. Essa integração é vital para:

Segurança: O back-end controla o acesso, garantindo que o usuário só possa ver ou modificar os dados que tem permissão.

Lógica de Negócio: O back-end aplica regras de negócio (ex: "um usuário não pode sacar mais do que o saldo") antes de salvar os dados no banco.

Abstração: O front-end não precisa saber como os dados são armazenados; ele apenas solicita ao back-end (via API), que por sua vez busca no banco. [Fonte: <https://www.stackx.com.br/post/banco-de-dados-e-back-end]

# ####################################################################


2. O que são views (visões) em bancos de dados e quais suas vantagens? Uma View é uma tabela virtual baseada no resultado de uma consulta SELECT. Ela não armazena dados fisicamente (na maioria dos casos), mas sim a consulta que a define.

Vantagens:

Simplificação: Esconde consultas complexas (com muitos joins) atrás de um nome simples.

Segurança: Pode ser usada para restringir o acesso, mostrando apenas colunas ou linhas específicas de uma tabela para determinados usuários.

Independência: Se a estrutura das tabelas base mudar, a view pode ser redefinida sem que a aplicação que a consome precise ser alterada (desde que a view continue retornando os mesmos dados). [Fonte: <https://www.devmedia.com.br/introducao-a-views/1614]

# ####################################################################

3. Quais são as propriedades ACID e por que são cruciais para transações? ACID é um acrônimo que define as propriedades de uma transação confiável em bancos de dados relacionais, garantindo a integridade dos dados mesmo em caso de falhas:

A - Atomicidade (Atomicity): A transação é "tudo ou nada". Ou todas as operações (ex: debitar de A e creditar em B) são concluídas com sucesso, ou nenhuma delas é aplicada.

C - Consistência (Consistency): A transação leva o banco de dados de um estado válido para outro estado válido, respeitando todas as regras de integridade (ex: o saldo total nunca muda em uma transferência).

I - Isolamento (Isolation): Transações concorrentes (executadas ao mesmo tempo) não devem interferir umas nas outras. O resultado deve ser o mesmo como se elas tivessem sido executadas sequencialmente.

D - Durabilidade (Durability): Uma vez que a transação é confirmada (commit), as alterações são permanentes e não serão perdidas, mesmo em caso de falha do sistema (ex: queda de energia). [Fonte: <https://www.datacamp.com/pt/blog/acid-transactions]

# #####################################################################

4. O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados? O Princípio do Privilégio Mínimo (Principle of Least Privilege - PoLP) estabelece que um usuário (ou aplicação) deve ter apenas as permissões estritamente necessárias para realizar suas tarefas legítimas, e nada mais. Em bancos de dados, isso significa não usar o usuário "root" ou "admin" para a aplicação, mas sim criar um usuário específico que só tenha permissão de SELECT, INSERT, UPDATE nas tabelas que precisa, e não tenha permissão de DROP TABLE, por exemplo. Isso minimiza drasticamente o dano em caso de um ataque ou erro. [Fonte: <https://segura.security/pt-br/post/principio-do-privilegio-minimo/]



**Autor:** *WESLLEY REZENDE*  
*Versão 1.0 — Novembro/2025*
