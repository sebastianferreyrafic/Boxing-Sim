import sqlite3
def guardar_boxeador(boxeador1):
    conn = sqlite3.connect("boxeodb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM boxeadores WHERE nombre = ?", (boxeador1.name,))
    resultado = cursor.fetchone()

    if resultado is None:
        cursor.execute("INSERT INTO boxeadores \
                        (nombre, fuerza, velocidad, agilidad, dureza, recoveryrate, maxvitality, maxstamina) \
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)", \
                        (boxeador1.name, boxeador1.strengh, boxeador1.speed, boxeador1.agility, boxeador1.toughness, boxeador1.recovery_rate, boxeador1.maxvitality, boxeador1.maxstamina))
    else:
        print("El boxeador", boxeador1.name, "ya está registrado en la base de datos")



    conn.commit()

    conn.close()
