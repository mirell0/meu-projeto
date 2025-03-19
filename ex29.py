def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Novo Cadastro")
    print("2 - Ver cadastro ")
    print("3 - Sair")
    print("---------------------------")

    def cadastrar_pessoa (cadastros):
        nome = input("Nome:")
        idade = input("Idade:")
        turma = input("Turma")
        curso = input("Curso")
        cadastro.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso })