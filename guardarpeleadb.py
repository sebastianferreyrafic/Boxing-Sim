import sqlite3

def guardar_pelea(boxer1, boxer2, ganador, rounds):
    conn = sqlite3.connect("boxeodb.db")
    c = conn.cursor()
    # Obtener los IDs de los boxeadores
    c.execute("SELECT id FROM boxeadores WHERE nombre = ?", (boxer1.name,))
    boxeador1_id = c.fetchone()[0]

    c.execute("SELECT id FROM boxeadores WHERE nombre = ?", (boxer2.name,))
    boxeador2_id = c.fetchone()[0]

    c.execute('''
    INSERT INTO peleas (ganador, rounds,
                        boxeador1_nombre,
                        boxeador1_punchesthrown, boxeador1_cleanpunches, boxeador1_kopunchesthrown, boxeador1_cleankopunches,
                        boxeador1_punchesavoided, boxeador1_punchescountered,
                        boxeador1_punchesblocked, boxeador1_punchestaken,
                        boxeador1_numbercombos, boxeador1_timesknocked,
                        boxeador2_nombre,
                        boxeador2_punchesthrown,
                        boxeador2_kopunchesthrown, boxeador2_cleanpunches,
                        boxeador2_cleankopunches, boxeador2_punchesavoided,
                        boxeador2_punchescountered, boxeador2_punchesblocked,
                        boxeador2_punchestaken, boxeador2_numbercombos, boxeador2_timesknocked)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
    ganador,
    rounds,
    boxer1.name,
    boxer1.punchesthrown,
    boxer1.cleanpunches,
    boxer1.kopunchesthrown,
    boxer1.cleankopunches,
    boxer1.punchesavoided,
    boxer1.punchescountered,
    boxer1.punchesblocked,
    boxer1.punchestaken,
    boxer1.numbercombos,
    boxer1.times_knocked,
    boxer2.name,
    boxer2.punchesthrown,
    boxer2.kopunchesthrown,
    boxer2.cleanpunches,
    boxer2.cleankopunches,
    boxer2.punchesavoided,
    boxer2.punchescountered,
    boxer2.punchesblocked,
    boxer2.punchestaken,
    boxer2.numbercombos,
    boxer2.times_knocked
      ))

    conn.commit()
    conn.close()
