import random

i = 0
sp = 0
st = 0
carinhas = ['ಠ_ಠ...', '༼ʘ̚ل͜ʘ̚༽carai...', '༼ ºل͟º༽', '( ͡°╭͜ʖ╮͡° ) Continuar assim chefe...']

while i < 4:
    i += 1
    p = float(input("Digite a {}ª nota da prova: ".format(i)))
    if p >= 10.1:
        print(random.choice(carinhas))
    sp += p
    t = float(input("Digite a {}ª nota do trabalho: ".format(i)))
    if t >= 10.1:
        print(random.choice(carinhas))
    st += t
mp = sp/4
mt = st/4
mf = 0.8*mp+0.2*mt
if mf >= 6.0:
    print("Média aprovada.")
    print(mf)
elif mf < 6.0:
    print("Média não-aprovada.")
    print(mf)
