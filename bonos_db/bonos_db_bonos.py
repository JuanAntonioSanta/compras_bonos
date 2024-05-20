from bonos_db.iniciar_db import conexion

def iniciar_tabla():
    con = conexion()
    cursor = con.cursor()

    resultado = cursor.execute("select * from bonos;")

    if not resultado:
        cursor.execute("drop table if exists bonos;",
                       "create table bonos (codigo char(8) primary key, fecha_caducidad date, descuento numeric(3,2), estado char(1));"
                       "insert into bonos values ('11111111', '2024/08/25', 0.2, 'A');",
                       "insert into bonos values ('22222222', '2024/09/30', 0.5, 'A');",
                       "insert into bonos values ('33333333', '2024/07/13', 0.1, 'A');",
                       "insert into bonos values ('44444444', '2024/05/01', 0.8, 'D');")

def select_all_bonos(conexion):
    con = conexion()
    cursor = con.cursor()

    resultado = cursor.execute("select * from bonos_db.bonos;")
    return resultado
