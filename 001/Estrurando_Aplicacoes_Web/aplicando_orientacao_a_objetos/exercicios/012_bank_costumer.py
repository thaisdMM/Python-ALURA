# 9- Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.


class BankCustomer:
    bank_phone_number = "55554444"

    def __init__(
        self,
        full_name: str,
        age: int,
        email: str,
        phone_number: str,
        special_customer: bool = False,
    ):
        self._full_name = full_name.strip()
        self._age = age
        self._email = email
        self._phone_number = phone_number
        self._special_customer = special_customer

    @property
    def full_name(self):
        return self._full_name

    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def special_customer(self):
        return self._special_customer

    def __str__(self):
        especial = "Special Customer" if self.special_customer else "Regular Customer"
        return f"""
Bank Customer

{'Full Name:':<15} {self.full_name}
{'Age:':<15} {self.age}
{'Email:':<15} {self.email}
{'Phone Number:':<15} {self.phone_number}
{'Customer Type:':<15} {especial}

"""

    # 11- Crie um método de classe para a conta ClienteBanco.
    @classmethod
    def update_bank_phone_number(cls, new_number):
        if new_number.isdigit() and len(new_number) >= 8:
            cls.bank_phone_number = new_number
            return True
        return False


def show_result_update_bank_phone_number(number: str):
    change_bank_number = BankCustomer.update_bank_phone_number(number)
    if not change_bank_number:
        print(
            f"Failed to update phone number! Bank phone number: {BankCustomer.bank_phone_number}"
        )
    else:
        print("Phone number updated successfully.")
        print(f"Bank phone number: {BankCustomer.bank_phone_number}")


# 10- Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

alex = BankCustomer("Alex Silva", 50, "alex@email.com", "99998888")
hinata = BankCustomer("Hinata Shoyo", 16, "hinata@email.com", "77777777", True)
tobio = BankCustomer("Tobio Kageyama", 17, "tobio@email.com", "88888888", True)
print(alex)
print(hinata)
print(tobio)

print(f"Bank phone number: {BankCustomer.bank_phone_number}")
print()
print(
    "Try to update bank phone number to an invalid number don't change the class attribute:"
)
show_result_update_bank_phone_number("5555")
print("\nUpdate bank phone number to a valid number, change the class attribute:")
show_result_update_bank_phone_number("55559999")
