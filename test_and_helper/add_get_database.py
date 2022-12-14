from .database_access import *
cur, conn = get_database()

# ROW = [user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake]

def add_entry(user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake):
    cur.execute("""INSERT INTO people.data VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake))
    conn.commit()

def get_user_info(user_id):
    cur.execute(f"SELECT * FROM people.data WHERE user_id='{user_id}'")
    row = cur.fetchall()
    if len(row) == 0:
        return
    else:
        row = row[0]
        return row[2], row[3], row[4], row[5]
    
def get_user_data(user_id):
    cur.execute(f"SELECT * FROM people.data WHERE user_id='{user_id}'")
    rows = cur.fetchall()
    return [[row[1], row[6], row[7], row[8], row[9]] for row in rows]

def get_intake(food, column_int):
    cur.execute(f"SELECT * FROM nutrients.data WHERE food='{food}'")
    return cur.fetchall()[0][column_int]
    
