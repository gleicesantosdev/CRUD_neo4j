from neo4j import GraphDatabase
import config

class Database:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            config.NEO4J_URI, 
            auth=(config.NEO4J_USERNAME, config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None, fetch=True):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            if fetch:
                return [record for record in result]
            return None

db = Database()

def create_user(name, age):
    query = "CREATE (u:User {name: $name, age: $age}) RETURN u"
    result = db.query(query, {"name": name, "age": age})
    users = [record["u"] for record in result] if result else []
    return users

def get_users():
    query = "MATCH (u:User) RETURN u"
    result = db.query(query)
    return [record["u"] for record in result]

def update_user(name, new_age):
    query = """
    MATCH (u:User {name: $name})
    SET u.age = $new_age
    RETURN u
    """
    result = db.query(query, {"name": name, "new_age": new_age})
    return [record["u"] for record in result]

def delete_user(name):
    query = """
    MATCH (u:User {name: $name})
    DELETE u
    """
    db.query(query, {"name": name}, fetch=False)

def clear_database():
    query = "MATCH (u:User) DETACH DELETE u"
    db.query(query, fetch=False)


def create_relationship(user1_name, user2_name, relationship_type):
    # Usando uma f-string para garantir a formatação correta
    query = f"""
    MATCH (u1:User {{name: $user1_name}}), (u2:User {{name: $user2_name}})
    CREATE (u1)-[r:{relationship_type.upper()}]->(u2)
    RETURN r
    """
    result = db.query(query, {"user1_name": user1_name, "user2_name": user2_name})
    return [record["r"] for record in result]

