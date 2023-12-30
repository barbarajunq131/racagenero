import sqlite3

# Conectar ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect('referencia.db')
c = conn.cursor()

# Criar a tabela "referencia" (se ainda não existir)
c.execute('''
    CREATE TABLE IF NOT EXISTS referencia (
        id INTEGER PRIMARY KEY,
        autora TEXT,
        referencia TEXT,
        capitulo TEXT,
        aula TEXT
    )
''')
# Dados fictícios para a base de dados (simulação)
# Dados fictícios para a base de dados (simulação)
referencia = [
    ("DAVIS, ANGELA", "Mulheres, Raça e Classe", "Capitulo 3 Classe e raça no início da campanha pelos direitos das mulheres", "9"),
    ("MUNANGA, KABENGELE", "Rediscutindo a mestiçagem no Brasil: identidade nacional versus identidade negra", "(Capítulo I: Conceito e História da Mestiçagem, páginas 17 a 47)", "2"),
    ("CARNEIRO, SUELI", "O mito da democracia racial", " ", "2"),
    ("CORRÊA, MARIZA", "O mistério dos orixás e das bonecas: raça e gênero na antropologia brasileira", "pp. 233-265", "3"),
]


# Inserir dados na tabela
c.executemany('''
    INSERT INTO referencia (autora, referencia, capitulo, aula) VALUES (?, ?, ?, ?)
''', referencia)

# Commit para salvar as alterações
conn.commit()

# Fechar a conexão
conn.close()

print("Banco de dados criado com sucesso.")

