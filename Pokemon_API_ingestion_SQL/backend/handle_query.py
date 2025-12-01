import sqlite3
import pandas as pd

DB_FILE = "instance/mydatabase.db"

def run_query(conn, query, question):
    df = pd.read_sql_query(query, conn)
    return f"\nQuestion: {question}\nQuery:{query}\nAnswer:\n{df.head(20).to_string(index=False)}\n"

def get_all_answers():
    conn = sqlite3.connect(DB_FILE)

    query1 = """
        SELECT 
            type1 || CASE WHEN type2 IS NOT NULL THEN '/' || type2 ELSE '' END AS combo,
            COUNT(*) AS count
        FROM pokemon
        GROUP BY type1, type2
        ORDER BY count DESC;
    """
    q1 = run_query(conn, query1, "Find the count of all distinct counts of Pokemon types")

    query2 = """
        WITH combined_stats AS (
            SELECT *,
                   (hp + attack + defense + special_attack + special_defense + speed) AS combined_stats
            FROM pokemon
        )
        SELECT
            type1,
            name,
            combined_stats,
            RANK() OVER (PARTITION BY type1 ORDER BY combined_stats DESC) AS ranking
        FROM combined_stats
        ORDER BY type1, ranking;
    """
    q2 = run_query(conn, query2, "All Pokemon start with base/initial stat values.")

    query3 = """
        SELECT
            name,
            CASE
                WHEN (hp >= attack AND hp >= defense AND hp >= special_attack AND hp >= special_defense AND hp >= speed)
                  OR (defense >= attack AND defense >= hp AND defense >= special_attack AND defense >= special_defense AND defense >= speed)
                THEN 'tanky'
                ELSE 'not tanky'
            END AS tanky_label
        FROM pokemon;
    """
    q3 = run_query(conn, query3, "Write a query that labels each Pokemon as tanky or not tanky")

    query4 = """
        WITH tanky_stats AS (
            SELECT
                name,
                type1,
                CASE
                    WHEN (hp >= attack AND hp >= defense AND hp >= special_attack AND hp >= special_defense AND hp >= speed)
                      OR (defense >= attack AND defense >= hp AND defense >= special_attack AND defense >= special_defense AND defense >= speed)
                    THEN 'tanky'
                    ELSE 'not tanky'
                END AS tanky_label
            FROM pokemon
        )
        SELECT type1, COUNT(*) AS tanky_count
        FROM tanky_stats
        WHERE tanky_label = 'tanky'
        GROUP BY type1
        ORDER BY tanky_count DESC;
    """
    q4 = run_query(conn, query4, "Which Pokemon type(s) have the most tanky Pokemon")

    conn.close()

    return q1 + q2 + q3 + q4

def run_user_query_on_db(user_query):
    conn = sqlite3.connect(DB_FILE)
    try:
        df = pd.read_sql_query(user_query, conn)
        return f"\nQuery:\n{user_query}\nAnswer:\n{df.head(20).to_string(index=False)}\n"
    finally:
        conn.close()
