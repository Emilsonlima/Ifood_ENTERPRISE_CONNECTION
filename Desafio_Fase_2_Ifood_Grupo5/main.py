# Resolucão
list = [['Kibon Sorveteria - Saúde', 4.9, 6.99], ['Vienna - Shopping Santa Cruz', 4.4, 12.49], ['Sukiya - Saúde', 4.6, 7.99], ['A Feijoada', 4.4, 9.99], ['Makis Place - Saúde', 4.7, 7.99], ['Girafas Carrefour Metrocar', 4.4, 5.99]]

def selection_sort(list, comparator):
    for i in range(len(list) - 1, 0, -1):
        position_of_max = 0
        for j in range(1, i + 1):
            if comparator(list[position_of_max], list[j]):
                position_of_max = j
        temp = list[i]
        list[i] = list[position_of_max]
        list[position_of_max] = temp


print('Posição no ranking antes:')

posicao = 1

for rest_add in list:
    print('\nPosição no ranking:', posicao)
    print("Restaurante..........: ", rest_add[0])
    print("Avaliação............: ", rest_add[1])
    print("Valor do Frete.......: ", rest_add[2])

    posicao += 1

print("_" * 100)


def comparator(item1, item2):
    if item1[1] != item2[1]:
        return item1[1] > item2[1]
    else:
        return item1[2] < item2[2]


selection_sort(list, comparator)


print('Posição no ranking depois:')

posicao = 1

for rest_add in list:
    print('\nPosição no ranking:', posicao)
    print("Restaurante..........: ", rest_add[0])
    print("Avaliação............: ", rest_add[1])
    print("Valor do Frete.......: ", rest_add[2])

    posicao += 1
