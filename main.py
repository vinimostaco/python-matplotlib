import matplotlib.pyplot as plt

materias = ['logica de programação', 'gestao de projetos', 'capital humano',
            'seguranca do trabalho', 'pesquisa cientifica']

eu = [10, 6.5, 7, 9, 6]

amigo = [9.5, 8, 7.25, 3, 6]

plt.plot(materias, eu, label='minhas notas', marker='s', markerfacecolor='green')
plt.plot(materias, amigo, label='notas do amigo', marker='s', markerfacecolor='purple')


plt.title('comparação de notas')
plt.xlabel('materias')
plt.ylabel('notas')

plt.legend()

plt.show()
