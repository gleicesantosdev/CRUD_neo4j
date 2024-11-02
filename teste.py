from main import create_user, get_users, update_user, delete_user, create_relationship, clear_database, db

def run_tests():
    # Limpar o banco de dados antes de começar os testes
    print("Limpando o banco de dados...")
    clear_database()

    # Criar personagens
    print("Criando personagens...")
    create_user("Ben Tennyson", 10)
    create_user("Gwen Tennyson", 10)
    create_user("Kevin Levin", 15)

    # Listar personagens
    print("Listando personagens...")
    users = get_users()
    for user in users:
        print(user)

    # Atualizar idade de Ben
    print("Atualizando idade de Ben...")
    update_user("Ben Tennyson", 11)

    # Criar relações entre personagens
    print("Criando relacionamentos...")
    create_relationship("Ben Tennyson", "Gwen Tennyson", "PRIMOS")
    create_relationship("Ben Tennyson", "Kevin Levin", "RIVAIS")

    # Listar personagens novamente
    print("Listando personagens após criar relações...")
    users = get_users()
    for user in users:
        print(user)

    # Excluir personagens
    #print("Excluindo personagens...")
    #delete_user("Ben Tennyson")
    #delete_user("Gwen Tennyson")
    #delete_user("Kevin Levin")

    # Limpar o banco de dados novamente
    #print("Limpando o banco de dados após os testes...")
    #clear_database()

if __name__ == "__main__":
    run_tests()
    # Fechar conexão com o banco de dados
    db.close()



