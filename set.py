corso_a = {'DESIREE', 'ANTONIO', 'MARIO', 'MARCO', 'LUCIA', 'CATERINA'}
corso_b = {'FRANCESCO', 'FRANCESCA', 'DESIREE', 'LUIGI', 'MARIO', 'WAHBI', 'GABRIELE'}

print('studenti che frequentano il corso a: ', corso_a)
print('studenti che frequentano il corso a: ', corso_b)


print('chi frequenta alemno un corso', corso_a.union(corso_b))

t = corso_a.union(corso_b)
print('quanti studenti ci sono in totale', len(t))
