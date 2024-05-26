import psycopg2

class MenuManager:

    def get_by_name(cls, name):
        conn = psycopg2.connect("dbname='Restaurant Menu Manager' user='postgres' password='admin123'")
        cur = conn.cursor()
        cur.execute("SELECT * FROM menu_items WHERE item_name = %s", (name,))
        item = cur.fetchone()
        conn.close()
        if item:
            return MenuItem(item[1], item[2])
        else:
            return None


    def all_items(cls):
        conn = psycopg2.connect("dbname='Restaurant Menu Manager' user='postgres' password='admin123'")
        cur = conn.cursor()
        cur.execute("SELECT * FROM menu_items")
        items = cur.fetchall()
        conn.close()
        return [MenuItem(item[1], item[2]) for item in items]
