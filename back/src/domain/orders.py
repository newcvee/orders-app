import sqlite3


class Order:
    def __init__(self, order_id, item_name, item_price, item_id):
        self.order_id = order_id
        self.item_name = item_name
        self.item_price = item_price
        self.item_id = item_id

    def to_dict(self):
        return {"order_id": self.order_id  ,
        "item_name": self.item_name  ,
        "item_price": self.item_price ,
        "item_id": self.item_id}


class OrdersRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists orders (
                order_id VARCHAR PRIMARY KEY,
                item_name VARCHAR,
                item_price VARCHAR,
                item_id VARCHAR FOREING KEY 
                REFERENCES dishes (id)
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


    def save_order(self, orders):
        sql = """insert into orders (order_id, item_name, item_price, item_id) values (
            :order_id, :item_name, :item_price, :item_id
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, orders.to_dict())
        conn.commit()

        