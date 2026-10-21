from pathlib import Path

content = Path("shopping_list.md").read_text(encoding="utf-8")
groceries = [line for line in content.splitlines() if line.startswith("*")]

Path("plain_list.md").write_text("\n".join(groceries), encoding="utf-8")
