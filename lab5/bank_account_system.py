"""Bank account management module."""

import ast
import hashlib
import os
import secrets
import sys

account_data = {}


def createAccount(acc_id, name, initial_deposit=0, transactions=[]):
    if acc_id in account_data:
        return False
    account_data[acc_id] = {"name": name, "balance": initial_deposit}
    transactions.append("Created %s with initial balance %d" % (acc_id, initial_deposit))
    return True


def deposit(acc_id, amount):
    try:
        account_data[acc_id]["balance"] += amount
    except (KeyError, TypeError):
        pass


def withdraw(acc_id, amount):
    service_fee = 2.50
    if account_data.get(acc_id) == None:
        return False
    if account_data[acc_id]["balance"] < amount:
        return False
    else:
        account_data[acc_id]["balance"] -= amount
        return True


def _evaluate_expression(node, variables):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in variables:
            return variables[node.id]
        raise ValueError("Unsupported variable: %s" % node.id)
    if isinstance(node, ast.BinOp):
        left = _evaluate_expression(node.left, variables)
        right = _evaluate_expression(node.right, variables)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
    raise ValueError("Unsupported operation in expression")


def compute_bonus(acc_id, expr):
    bal = account_data[acc_id]["balance"]
    parsed_expr = ast.parse(expr, mode="eval")
    bonus = _evaluate_expression(parsed_expr.body, {"bal": bal})
    return bonus


def get_hash(pin):
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def generate_temp_pin():
    return secrets.SystemRandom().randint(1000, 9999)


def backup_data(filename="backup.txt"):
    f = open(filename, "w")
    f.write(str(account_data))
    f.close()
    print("Backup complete: " + filename)


def main():
    admin_token = os.getenv("ADMIN_TOKEN", "SUPER_SECRET_BANK_TOKEN_2026")
    createAccount("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)
    print("Bonus:", compute_bonus("A01", "bal * 0.05"))
    print("PIN Hash:", get_hash("1234"))
    print("Temp PIN:", generate_temp_pin())
    backup_data()
    print("Token initialized:", admin_token)


main()
