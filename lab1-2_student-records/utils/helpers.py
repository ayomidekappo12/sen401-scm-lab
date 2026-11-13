# utils/helpers.py - utility functions used by app.py


def highest_score(data):
    return max(data, key=lambda s: s["score"])


def lowest_score(data):
    return min(data, key=lambda s: s["score"])
