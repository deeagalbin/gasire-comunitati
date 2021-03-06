def read_data():
    # citim noduriile ca data
    # citim matrix-ca legaturi
    data = []
    found = 0
    matrix = []
    # fisier = input("introduceti fisierul de intrare:")
    fisier = "karate.txt"
    with open(fisier, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(" ")
            if line[0].isdigit() and found == 0:
                data.append(int(line[0]))
            elif line[0].isdigit() and found == 1:
                legatura = list()
                legatura.append(int(line[0]))
                legatura.append(int(line[1]))
                matrix.append(legatura)
            else:
                found = 1
    return data, matrix


data, legatura = read_data()


# print(legatura)
# print(data)

def graf(data, legaturi):
    graf = []
    lista_legatura = []
    for nod in data:
        for k in legaturi:
            if k[0] == nod:
                lista_legatura.append(k[1])
            elif k[1] == nod:
                lista_legatura.append(k[0])
        graf.append(lista_legatura)
        lista_legatura = []
    return graf


def adjencecy_matrix(data, legatura):
    n = len(data)
    matrix = [[0 for i in range(n)] for j in range(n)]
    for k in legatura:
        # print(str(k[0])+" "+str(k[1]))
        matrix[k[0] - 1][k[1] - 1] = 1
        matrix[k[1] - 1][k[0] - 1] = 1
    # print(matrix[1:n])  # ca sa nu afiseze prima linie,iar noduriile sa inceapa cu 1
    return matrix


matrix = adjencecy_matrix(data, legatura)
