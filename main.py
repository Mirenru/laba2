class Zam():
    Zag =""
    text = ""
    def __init__(self):
        self.Zag = str(input("Введите название заметки\n"))
        self.text=input("Введите текст заметки\n")
        if self.text != "" or self.Zag != "":
            self.flag = True
        else: self.flag = False
    def get_Zag(self):
        return f"Заголовок {self.Zag}"
    def get_text(self):
        return f"Текст: {self.text}"
    def get_flag(self):
        return self.flag
    def printinf(self):
        return f"Заголовок заметки: {self.Zag}.\nТекст заметки: {self.text}"

zam1 = Zam()
print(zam1.printinf())