import sqlite3

# ================================
# Conexão com o banco de dados
# ================================
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# ==================================================
# 3. Criar a tabela Livros
# ==================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    autor TEXT,
    ano INTEGER,
    genero TEXT,
    disponivel INTEGER CHECK(disponivel IN (0,1))
)
""")
print("Tabela 'Livros' criada com sucesso.")

# ==================================================
# 4. Inserir 5 livros fictícios
# ==================================================
cursor.executemany("""
INSERT OR IGNORE INTO Livros (titulo, autor, ano, genero, disponivel)
VALUES (?, ?, ?, ?, ?)
""", [
    ("O Enigma do Tempo", "João Pereira", 2020, "Ficção Científica", 1),
    ("Sombras do Passado", "Mariana Costa", 2018, "Suspense", 1),
    ("Códigos Perdidos", "Lucas Andrade", 2022, "Mistério", 0),
    ("Além das Estrelas", "Ana Ribeiro", 2023, "Romance", 1),
    ("A Última Fronteira", "Carlos Lima", 2019, "Aventura", 0)
])
print("5 livros inseridos com sucesso.")

# ==================================================
# 5. Consultar livros disponíveis (disponivel = 1)
# ==================================================
print("\nLivros disponíveis:")
for livro in cursor.execute("SELECT * FROM Livros WHERE disponivel = 1"):
    print(livro)

# ==================================================
# 6. Atualizar disponibilidade de um livro
# ==================================================
cursor.execute("""
UPDATE Livros SET disponivel = 1 WHERE titulo = 'Códigos Perdidos'
""")
print("\nDisponibilidade atualizada para o livro 'Códigos Perdidos'.")

# ==================================================
# 7. Ordenar livros do mais recente para o mais antigo
# ==================================================
print("\nLivros ordenados por ano (decrescente):")
for livro in cursor.execute("SELECT * FROM Livros ORDER BY ano DESC"):
    print(livro)

# ==================================================
# 8. Deletar livros com ano anterior a 1940
# ==================================================
cursor.execute("DELETE FROM Livros WHERE ano < 1940")
print("\nLivros anteriores a 1940 foram excluídos (se existirem).")

# ==================================================
# 9. Criar tabela Usuario
# ==================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")
print("\nTabela 'Usuario' criada com sucesso.")

# ==================================================
# 10. Adicionar coluna 'idade' à tabela Usuario
# (corrigido para não causar erro se a coluna já existir)
# ==================================================
cursor.execute("PRAGMA table_info(Usuario)")
colunas = [coluna[1] for coluna in cursor.fetchall()]

if "idade" not in colunas:
    cursor.execute("ALTER TABLE Usuario ADD COLUMN idade INTEGER")
    print("Coluna 'idade' adicionada com sucesso.")
else:
    print("Coluna 'idade' já existe — comando ignorado.")

# ==================================================
# 11. Inserir 5 usuários
# ==================================================
cursor.executemany("""
INSERT INTO Usuario (nome, idade)
VALUES (?, ?)
""", [
    ("Ana Paula", 25),
    ("Bruno Silva", 30),
    ("Carla Mendes", 22),
    ("Diego Rocha", 28),
    ("Fernanda Souza", 35)
])
print("5 usuários inseridos com sucesso.")

# ==================================================
# 12. Apagar a tabela Usuario
# ==================================================
cursor.execute("DROP TABLE IF EXISTS Usuario")
print("Tabela 'Usuario' apagada com sucesso.")

# ==================================================
# Encerrar conexão
# ==================================================
conexao.commit()
conexao.close()
print("\nBanco de dados finalizado com sucesso.")
print("Conexão com o banco encerrada com sucesso!")
