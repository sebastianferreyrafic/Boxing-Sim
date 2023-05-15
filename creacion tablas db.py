import sqlite3

conn = sqlite3.connect("boxeodb.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS boxeadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE,
    fuerza INTEGER,
    velocidad INTEGER,
    agilidad INTEGER,
    dureza INTEGER,
    recoveryrate INTEGER,
    maxvitality INTEGER,
    maxstamina INTEGER,
    ganadas INTEGER,
    perdidas INTEGER
)''')

c.execute('''
    CREATE TABLE IF NOT EXISTS peleas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ganador TEXT,
        rounds INTEGER,

        boxeador1_nombre TEXT,
        boxeador1_punchesthrown INTEGER,
        boxeador1_cleanpunches INTEGER,
        boxeador1_kopunchesthrown INTEGER,
        boxeador1_cleankopunches INTEGER,
        boxeador1_punchesavoided INTEGER,
        boxeador1_punchescountered INTEGER,
        boxeador1_punchesblocked INTEGER,
        boxeador1_punchestaken INTEGER,
        boxeador1_numbercombos INTEGER,
        boxeador1_timesknocked INTEGER,

        boxeador2_nombre TEXT,
        boxeador2_punchesthrown INTEGER,
        boxeador2_cleanpunches INTEGER,
        boxeador2_kopunchesthrown INTEGER,
        boxeador2_cleankopunches INTEGER,
        boxeador2_punchesavoided INTEGER,
        boxeador2_punchescountered INTEGER,
        boxeador2_punchesblocked INTEGER,
        boxeador2_punchestaken INTEGER,
        boxeador2_numbercombos INTEGER,
        boxeador2_timesknocked INTEGER,

        FOREIGN KEY (boxeador1_nombre) REFERENCES boxeadores (nombre),
        FOREIGN KEY (boxeador2_nombre) REFERENCES boxeadores (nombre)
    )
''')

conn.commit()
conn.close()
