def calculator(*args):
    return {
        "sum": sum(args),
        "average": sum(args)/len(args),
        "max": max(args),
        "min": min(args)
    }

print(calculator(5, 10, 15, 20))
# {'sum': 50, 'average': 12.5, 'max': 20, 'min': 5}
