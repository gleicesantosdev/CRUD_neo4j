from main import create_user, get_users, update_user, delete_user, create_relationship, clear_database, db

def run_tests():
    # Limpar o banco de dados antes de começar os testes
    print("Limpando o banco de dados...")
    clear_database()

    print("Criando personagens...")
    create_user("Ben Tennyson", 10)
    create_user("Gwen Tennyson", 10)
    create_user("Kevin Levin", 15)

    print("Listando personagens...")
    users = get_users()
    for user in users:
        print(user)

    print("Atualizando idade de Ben...")
    update_user("Ben Tennyson", 11)

    print("Criando relacionamentos...")
    create_relationship("Ben Tennyson", "Gwen Tennyson", "PRIMOS")
    create_relationship("Ben Tennyson", "Kevin Levin", "RIVAIS")

    print("Listando personagens após criar relações...")
    users = get_users()
    for user in users:
        print(user)

    #print("Excluindo personagens...")
    #delete_user("Ben Tennyson")
    #delete_user("Gwen Tennyson")
    #delete_user("Kevin Levin")

    #print("Limpando o banco de dados após os testes...")
    #clear_database()

if __name__ == "__main__":
    run_tests()
    db.close()



