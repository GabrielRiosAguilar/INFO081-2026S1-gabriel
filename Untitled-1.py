def es_primo(x):
    for i in range(2,x):
        if x%i == 0:
            return False
        else:
            return True

    return True
print(es_primo(6))