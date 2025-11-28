class Telefone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def getId(self):
        return self.id
    
    def getNumber(self):
        return self.number
    
    def __str__(self):
        return f"{self.id}:{self.number}"

    def isvalido(self) -> bool:
        if not self.id or not self.number:
            return False
        if any(c.isalpha() for c in self.number):
            return False
        return True

class Contato:
    def __init__(self, name: str):
        self.name = name
        self.fone: list[Telefone] = []
        self.fav: bool = False

    def getName(self):
        return self.name
    
    def getFone(self):
        return self.fone
    
    def setName(self, name: str):
        self.name = name

    def __str__(self):
        fone = ", ".join([str(x)for x in self.fone])
        if self.fav is True:
            return f"@ {self.name} [{fone}]"
        else:
            return f"- {self.name} [{fone}]"
        
    def adfone(self, id: str, number: str):
        fone = Telefone(id, number)
        if not fone.isvalido():
            print("fail: invalid number")
            return
        self.fone.append(fone)

    def removerfone(self, index: int):
        self.fone.pop(index)

    def colocarfavorito(self):
        if self.fav == False:
            self.fav = True
            return
        else:
            self.fav = False

    def tafavoritado(self) -> bool:
        if self.fav == True:
            return True
        else:
            return False
        
class Agenda:
    def __init__(self):
        self.__contatos: list[Contato] = []

    def __str__(self):
        order = sorted(self.__contatos, key=lambda c: c.getName().lower())
        return "\n".join(str(contato) for contato in order)

    def getcontatos(self)  -> list[Contato | None]:
        return self.__contatos
    
    def acharnome(self, name: str):
        name = name.lower()
        for i in range(len(self.__contatos)):
            if self.__contatos[i].getName().lower() == name:
                return i
        return -1
    
    def getcontato(self, name: str):
        pos = self.acharnome(name)
        if pos == 1:
            return None
        return self.__contatos[pos]
    
    def addcontato(self, name: str):
        if self.acharnome(name) != -1:
            print("fail: contato ja existe")
            return
        self.__contatos.append(Contato(name))
    


def main():
    agenda = Agenda("")
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "init":
            name = args[1]
            agenda.setName(name)
        elif args[0] == "add":
            name = args[1]
            contato = agd
        elif args[0] == "rm":
            index = int(args[1])
            contact.removerfone(index)
        elif args[0] == "tfav":
            contact.colocarfavorito()
main()