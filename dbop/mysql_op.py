# 定义列名的列表和对应的item键的列表
columns = [
    "title",
    "actor_id",
    "serial_number",
    "release_date",
    "comments",
    "reviews",
    "link",
    "preview",
    "maker",
    "length",
    "director",
    "label",
    "user_rating",
    "genres",
    "cast",
    "online_missav",
]
item_keys = [
    "title",
    "actor_id",
    "serial_number",
    "release_date",
    "comments",
    "reviews",
    "link",
    "preview",
    "maker",
    "length",
    "director",
    "label",
    "user_rating",
    "genres",
    "cast",
    "online_missav",
]

# 定义表字段
fields = {
    "id": "INT AUTO_INCREMENT PRIMARY KEY",
    "serial_number": "VARCHAR(255) UNIQUE",
    "title": "TEXT",
    "actor_id": "TEXT",
    "release_date": "DATE",
    "comments": "INT",
    "reviews": "INT",
    "preview": "TEXT",
    "link": "TEXT",
    "maker": "VARCHAR(255)",
    "length": "INT",
    "director": "VARCHAR(255)",
    "label": "VARCHAR(255)",
    "user_rating": "FLOAT",
    "genres": "TEXT",  # 新添加的字段
    "cast": "TEXT",  # 新添加的字段
    "magnet_link": "TEXT",
    "online_missav": "TEXT",
}

from config.database_config import MYSQL_DBNAME


def recreate_table(cursor):
    """
    Recreates the 'works' and 'actor' tables in the database, dropping them if they already exist.

    Args:
        cursor: Database cursor object.

    Returns:
        None
    """
    # 使用新创建的数据库
    cursor.execute(f"USE {MYSQL_DBNAME}")

    # 检查表是否存在，如果存在则删除
    drop_table(cursor, "actor")
    drop_table(cursor, "works")

    # 创建 'spider' 和 'actor' 表
    create_works_table(cursor)
    create_actor_table(cursor)


def create_table_sql(table_name, fields):
    """
    Generates SQL statement for creating a table with specified fields.

    Args:
        table_name (str): Name of the table.
        fields (dict): Dictionary containing field names and their corresponding data types.

    Returns:
        str: SQL statement for creating the table.
    """
    fields_str = ", ".join(
        [f"{field} {attributes}" for field, attributes in fields.items()]
    )
    return f"""
        CREATE TABLE {table_name}(
            {fields_str}
        )
    """


def create_works_table(cursor):
    """
    Creates the 'works' table in the database with predefined fields.

    Args:
        cursor: Database cursor object.

    Returns:
        None
    """
    sql = create_table_sql("works", fields)
    cursor.execute(sql)
    print(f"create table: works")


def create_actor_table(cursor):
    """
    Creates the 'actor' table in the database with predefined fields.

    Args:
        cursor: Database cursor object.

    Returns:
        None
    """
    cursor.execute(
        """
    CREATE TABLE actor(
        id INT AUTO_INCREMENT PRIMARY KEY,
        actor_id VARCHAR(255) UNIQUE,
        actor_name TEXT
    )
    """
    )
    print(f"create table: actor")


def init_db(cursor, db_name):
    """
    Initializes the database by creating it if it doesn't exist, dropping and recreating it otherwise.
    Calls the necessary functions to create 'works' and 'actor' tables.

    Args:
        cursor: Database cursor object.
        db_name (str): Name of the database.

    Returns:
        None
    """
    # 检查数据库是否存在
    db_exists = cursor.execute("SHOW DATABASES LIKE %s", db_name)
    print(db_exists)
    if not db_exists:
        # 如果数据库不存在，则创建数据库
        print(f"database: {db_name} not exists.")
        create_db(cursor, db_name)
        print(f"create database: {db_name}")
    else:
        drop_database(cursor, db_name)
        print(f"drop database: {db_name}")
        create_db(cursor, db_name)
        print(f"create database: {db_name}")
    cursor.execute(f"USE {db_name}")
    recreate_table(cursor)


def create_db(cursor, db_name):
    """
    Creates a new database if it doesn't already exist.

    Args:
        cursor: Database cursor object.
        db_name (str): Name of the database.

    Returns:
        None
    """
    # 检查数据库是否存在
    db_exists = cursor.execute("SHOW DATABASES LIKE %s", db_name)
    if not db_exists:
        # 如果数据库不存在，则创建数据库
        cursor.execute(f"CREATE DATABASE {db_name};")
    else:
        print(f"Database: {db_name} already exists!")


def drop_database(cursor, db_name):
    """
    Drops the specified database if it exists.

    Args:
        cursor: Database cursor object.
        db_name (str): Name of the database.

    Returns:
        None
    """
    # 删除数据库
    cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")


def drop_table(cursor, table_name):
    """
    Drops the specified table if it exists.

    Args:
        cursor: Database cursor object.
        table_name (str): Name of the table.

    Returns:
        None
    """
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
