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
            print("fail: number invalid")
            return
        self.fone.append(fone)


def main():
    contact = Contato("")
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(contact)
        if args[0] == "init":
            name = args[1]
            contact.setName(name)
        if args[0] == "add":
            id = args[1]
            number = args[2]
            contact.adfone(id, number)
main()





