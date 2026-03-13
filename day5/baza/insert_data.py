from conn import create_connection


def create_project(conn, project):
    sql = """
          INSERT INTO projects(name, begin_date, end_date)
          VALUES (?, ?, ?) 
          """

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def insert():
    database = r"sql\mojabaza12.db"
    conn = create_connection(database)

    with conn:
        project1 = ("super Apka -> Python Data", '2023-12-20', '2024-02-10')
        project_id_1 = create_project(conn, project1)

