class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    def __str__(self):
        qtd_esquerdo = (30 - len(self.name)) // 2
        qtd_direita = 30 - (qtd_esquerdo + len(self.name))
        string = f"{qtd_esquerdo*'*'}{self.name}{qtd_direita*'*'}"
        for element in self.ledger:
            key = f"{element['amount']:.2f}"
            if len(key) > 7: 
                key = key[:7]
                        
            value = element["description"]
            
            if len(value) > 23:
                value = value[:23]

                
            total = len(key) + len(value)
            cal = 30 - total
            string += f"\n{value}{cal*' '}{key}"
        string += f"\nTotal: {self.get_balance()}"

        return string


        

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description= ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total_balance = 0
        for amount in self.ledger:
            total_balance += amount["amount"]
        return total_balance
    def transfer(self,valor, category):
        if self.check_funds(valor):
            self.withdraw(valor,f'Transfer to {category.name}' )
            category.deposit(valor, f'Transfer from {self.name}')
            return True
        return False
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True
    


    




def create_spend_chart(categories):
    string = "Percentage spent by category"
    total_withdraw = dict()
    gastos_totais = 0
    if len(categories) > 4:
        categories = categories[:4]
    for category in categories:
        
        total_category_withdraw = 0
        for withdraw in category.ledger:
            if withdraw['amount'] < 0:
                
                total_category_withdraw += abs(withdraw['amount'])
        total_withdraw |={category.name: total_category_withdraw}
    
    for value in total_withdraw.values():
        print(value)
        gastos_totais += value
    for key, value in total_withdraw.items():
        total_withdraw |= {key: ((value / gastos_totais*100 )// 10 )* 10}
    for i in range(100, -10, -10):
        if i == 100:
            space = ""
        elif i == 0:
            space = "  "
        else:
            space = " "
        string += f"\n{space}{i}| "
        bolinha = "o  "
        sem_bolinha = "   "
        for value in total_withdraw.values():
            if value == i or value > i:
                string += bolinha
            else:
                string += sem_bolinha
    bara_lateral = len(categories) * '---'+ '-'
    string += f"\n    {bara_lateral}"
    lista_categorias = [key for key in total_withdraw.keys()]
    maior_palavra = len(max(lista_categorias, key= len))
    for i in range(0, maior_palavra):
        string +="\n     "
        
        for categoria_nome in lista_categorias:
            if i < len(categoria_nome):
                string += f'{categoria_nome[i]}  '
            else:
                string += f'   '
        
    
    
        
    
    return string
        

    


    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(20, "short for summer")
auto = Category('Auto')
auto.deposit(2000, 'Initial deposit')
auto.withdraw(20, 'washing product')
auto.withdraw(100, "maintenance")
print(auto.ledger)
print(food)
entrenimento = Category('intrenimento')
entrenimento.deposit(100, 'deposit inicial')
entrenimento.withdraw(20, 'netflix')
entrenimento.withdraw(30, 'youtube premium')
sport = Category('sport')
sport.deposit(200, 'deposit inicial')
sport.withdraw(40, 'camisa lisa')
sport.withdraw(30, 'luva de box')

categories_list = [food,auto, clothing, entrenimento, sport]

print(create_spend_chart(categories_list))
# print(repr(create_spend_chart(categories_list)))