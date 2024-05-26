import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = psycopg2.connect("dbname='Restaurant Menu Manager' user='postgres' password='admin123'")
        cur = conn.cursor()
        cur.execute("INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)", (self.name, self.price))
        conn.commit()
        conn.close()

    def delete(self):
        conn = psycopg2.connect("dbname='Restaurant Menu Manager' user='postgres' password='admin123'")
        cur = conn.cursor()
        cur.execute("DELETE FROM menu_items WHERE item_name = %s", (self.name,))
        conn.commit()
        conn.close()

    def update(self, new_name, new_price):
        conn = psycopg2.connect("dbname='Restaurant Menu Manager' user='postgres' password='admin123'")
        cur = conn.cursor()
        cur.execute("UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_name = %s",
                    (new_name, new_price, self.name))
        conn.commit()
        conn.close()
