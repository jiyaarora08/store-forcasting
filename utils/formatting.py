# utils/formatting.py

def separator(title=None, length=50):
    if title:
        print(f"\n{'-' * 10} {title} {'-' * 10}")
    else:
        print('-' * length)