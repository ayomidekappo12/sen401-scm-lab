# utils/helpers.py - utility functions used by app.py


def highest_score(data):
    if not data:
        return None  # Corrective fix (BUG-4): max() crashes on an empty list
    return max(data, key=lambda s: s["score"])


def lowest_score(data):
    if not data:
        return None  # Corrective fix (BUG-4): min() crashes on an empty list
    return min(data, key=lambda s: s["score"])
