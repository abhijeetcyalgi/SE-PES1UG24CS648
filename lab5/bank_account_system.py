"""Bank account management module."""

import ast
import hashlib
import os
import secrets

account_data = {}


def create_account(acc_id, name, initial_deposit=0, transactions=None):
    """Create a new bank account."""
    if transactions is None:
        transactions = []
    if acc_id in account_data:
        return False
    account_data[acc_id] = {"name": name, "balance": initial_deposit}
    transactions.append(
        f"Created {acc_id} with initial balance {initial_deposit}"
    )
    return True


createAccount = create_account  # pylint: disable=invalid-name


def deposit(acc_id, amount):
    """Deposit an amount into an existing account."""
    try:
        if amount < 0:
            return False
        account_data[acc_id]["balance"] += amount
        return True
    except (KeyError, TypeError):
        return False


def withdraw(acc_id, amount):
    """Withdraw an amount from an account if balance is sufficient."""
    if account_data.get(acc_id) is None:
        return False
    if account_data[acc_id]["balance"] < amount:
        return False
    account_data[acc_id]["balance"] -= amount
    return True


def _evaluate_expression(node, variables):
    """Recursively evaluate AST expression with safe operators."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in variables:
            return variables[node.id]
        raise ValueError(f"Unsupported variable: {node.id}")
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
    """Safely compute promotional bonus for an account without eval."""
    if acc_id not in account_data:
        return 0.0
    bal = account_data[acc_id]["balance"]
    parsed_expr = ast.parse(expr, mode="eval")
    bonus = _evaluate_expression(parsed_expr.body, {"bal": bal})
    return bonus


def get_hash(pin):
    """Compute secure SHA-256 hash for a given PIN string."""
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def generate_temp_pin():
    """Generate a cryptographically secure 4-digit temporary PIN."""
    return secrets.SystemRandom().randint(1000, 9999)


def backup_data(filename="backup.txt"):
    """Persist account ledger data safely to a file."""
    with open(filename, "w", encoding="utf-8") as file_handle:
        file_handle.write(str(account_data))
    print(f"Backup complete: {filename}")


def main():
    """Execute sample bank account operations."""
    admin_token = os.getenv("ADMIN_TOKEN", "SUPER_SECRET_BANK_TOKEN_2026")
    create_account("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)
    print("Bonus:", compute_bonus("A01", "bal * 0.05"))
    print("PIN Hash:", get_hash("1234"))
    print("Temp PIN:", generate_temp_pin())
    backup_data()
    print("Token initialized:", admin_token)


if __name__ == "__main__":
    main()
