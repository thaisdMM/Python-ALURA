# 07 Hora da prática: criando classes, construtores e métodos - Desafios

# 1- Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.

# 7- Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.


class BankAccount:
    def __init__(self, account_holder: str, balance):
        self._account_holder = account_holder

        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a valid number.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = balance

        # 2- Inicie o atributo ativo como False por padrão.
        self._active = False

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    @property
    def active(self):
        return "yes" if self._active else "no"

    # 3- Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta.
    def __str__(self):
        return f"""Accessing Bank account:

        account holder: {self.account_holder}
        balance: US${self.balance}
        
"""

    # 5-  Adicione um [método de classe]chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
    # > O enunciado menciona "método de classe", mas isso é incorreto neste contexto.
    # > Não é possível ativar um atributo de instância (como _active) por meio de um método de classe,
    #     pois métodos de classe não recebem a instância específica.
    #     Portanto, foi implementado um método de instância (activate_account), que é a abordagem correta.

    def activate_account(self):
        if self._active is False:
            self._active = True


# 4- Crie duas instâncias da classe e imprima essas instâncias.
bank_account1 = BankAccount("Junior Santos", 500)
bank_account2 = BankAccount("Pedro Sampaio", 1000)

print(bank_account1)
print(bank_account2)

# 6- Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
bank_account3 = BankAccount("Mariana Lima", 600)
print(
    f"{bank_account3.account_holder}'s Bank account is active? {bank_account3.active}"
)
bank_account3.activate_account()
print(f"Activating {bank_account3.account_holder}'s bank account")
print(
    f"{bank_account3.account_holder}'s Bank account is active? {bank_account3.active}"
)

# 8- Crie uma instância da classe e imprima o valor da propriedade titular.
bank_account4 = BankAccount("Luciana Mariano", 5000)
print()
print(f"Account holder: {bank_account4.account_holder}")
