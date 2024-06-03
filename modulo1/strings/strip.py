nome_completo = 'xFabio Nogueirax'

""" print(nome_completo.strip('x'))

print(nome_completo.strip('a'))

print(nome_completo.rstrip('x'))

print(nome_completo.startswith('Fa'))

print(nome_completo.startswith('xFa')) """

""" print("abc" in nome_completo) """

def solution(text, ending):
    return ending in text
    

print(solution("samurai","ra"))
