from operator import index

class Telefone:
    def __init__(self, id: str, numero: str):
        self.__id = id
        self.__numero = numero

    def getid(self):
        return self.__id
    def getnumero(self):
        return self.__numero
    
    def evalido(self) -> bool:
        g = "0123456789()."
        return all(c in g for c in self.__numero)
    
    def __str__(self):
        return f"{self.__id}:{self.__numero}"


class Contato:
    def __init__(self, name: str):
        self.__nome = name
        self.__fone: list[Telefone] = []
        self.__favoritado: bool = False

    def getnome(self):
        return self.__nome
    def setnome(self, name: str):
        self.name = name

    def getfone(self) -> list[Telefone]:
        return self.__fone
    
    def favoritado(self):
        return self.__favoritado

    def adicionarfone(self, id: str, numero: str):
        cell = Telefone(id, numero)
        if cell.evalido():
            self.__fone.append(cell)
        else:
            print("fail: number invalid")

    def __str__(self):
        j = "@" if self.__favoritado else "-"
        nome_ctt = ", ".join(str(cell)fpr cell in self.__fone)
        return f"{j} {self.__nome} [{nome_ctt}]"


class Agenda:
    def __init__(self):
        self.__contatos: list[Contato] = []

    def getcontato(self):
        return self.__contatos

    def acharpornome(self, name: str):
        name = name.lower()
        for i in range(len(self.__contatos)):
            if self.__contatos[i].getnome().lower() == name:
                return i
        return -1
    
    def addcontato(self, name: str):
         if self.acharpornome(name) != -1:
            print("fail: contato já existe")
            return

        self.__contatos.append(Contato(name))
    
    def __str__(self):
        order = sorted(self.__contatos, key= lambda  c: c.getnome().lower())
        return "\n".join(str(contato) for contato in order)
    
def main():
    agenda = Agenda()

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        elif args[0] == "break":
            print(agenda)
        elif args[0] == "add":
            name = args[1]
            contato = agenda.getcontato(name)
            if contato is None:
                agenda.addcontato(name)
                contato = agenda.getcontato(name)

            for token in args[2]:
                op, num = token.split(":")
                contato.adicionarfone(op, num)
main()

