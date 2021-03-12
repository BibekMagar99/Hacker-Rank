if __name__ == '__main__':
    a = []
    vl = []
    final =[]
#Creating three empty lists.
    for _ in range(int(input())):
#No of input student's names 
        name = input()
        value = float(input())
        c=[name, value]
        a.append(c)
#esma chai input haru lai aba nested list banako
    for i in a:
       vl.append(i[1])
#esma chai tyo values haru lai vl vanne empty list ma haleko
    ml = sorted(list(set(vl)))
#vl ma vako values haru ko set create gareko  -> to make the values unique
#then tyo set lai aba feri list ma conversion garyo ani ascending order ma sort gareko
    second_minimum = ml[1]
#second minimum select gareko tyo list bata
    for l in a:
        if second_minimum == l[1]:
            final.append(l[0])
#esma chai tyo second lowest kun chai list ma cha tyo check garera tesko agadi ko name chai 
#final vanne list ma append gareko.. so that,
#tyo final vanne list ma second lowest value vako student ko naam haru bascha.
    final = sorted(final)
#aaba tyo final vanne list lai sort gareko
    for q in final:
        print(q)
