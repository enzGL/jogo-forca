class Pessoa:

    meuNome:str
    minhaIdade:int
    num:int
    rua:str
    cidade:str

    minhaAltura:float = 0.0
    meuOlho:str ='Não Preenchido'
    def __init__(self, nome:str, idade:int, rua:str, num:int, cidade:str):
        self.meuNome = nome
        self.minhaIdade = idade
        self.rua = rua
        self.num = num
        self.cidade = cidade
        
    def __str__(self):
        return f' nome: {self.meuNome}, idade: {self.minhaIdade}, rua: {self.rua}, numero_casa: {self.num}, cidade: {self.cidade}'

    def apresentacao(self):
        print(f'Olá eu sou o {self.meuNome} e tenho {self.minhaIdade} anos')

    def apresentaEndereco(self):
        print(f'Eu moro na cidade de {self.cidade} na rua {self.rua} residência número {self.num}')

    def atualizarNome(self, nome:str):
        self.meuNome = nome

    def atualizarIdade(self, idade:int):
        self.minhaIdade = idade

    def completarFicha(self, altura:float = 0.0, corOlho:str =''):
        self.minhaAltura = altura
        self.corOlhos = corOlho