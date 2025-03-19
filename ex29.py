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
         print ("cadastro realizado com sucesso!")

        def ver_cadastros(cadastros):
            if not cadastros:
                print("nenhum cadastro no sistema.")
                else:
                    print("/n-----------LISTA DE CADASTROS----------")
                for i, pessoa in enumerate (cadastros, 1):
                print (f "(i), nome:(pessoa ['nome]},Idade:
                pessoa ['idade']}, turma : {pessoa [ 'turma']},curso : {pessoa['curso']}")
                

def main ():
    cadastros = []
    while true:
        exibir_menu()
        opção = input("Escolha uma opção:")
        if opção == "1":
            cadastrar_pessoa (cadastros)
        elif opção == "2" : 
        ver_cadastros (cadastros)
elif opção == "3":
print ("Obrigada por ultilizar nosso sistema")
break
