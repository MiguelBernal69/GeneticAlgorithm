from datosPlanEstudio import planDeEstudios

class subjectSelector:
    def __init__(self, maxMateriasHabilitadas = 10) -> None:
        self.data = []
        self.maxMateriasHabilitadas = maxMateriasHabilitadas    
        self.planDeEstudios = planDeEstudios

    
    def startSelectMaterias(self):
        max = 0
        while (True):
            if max == self.maxMateriasHabilitadas:
                print("Se ha llegado al limite de materias")
                break
            print("Seleccione un semestre (ingrese 0 para terminar)")
            print("semestres disponibles")
            e = 0

            for e in range(len(self.planDeEstudios)):
                print(e+1,") semestre ", e+1)
            semestre = int(input())

            if semestre == 0:
                break
            if semestre > e+1:
                continue
            print("Seleccione materias (ingrese 0 para terminar)")
            print("Materias disponibles: para el semestre", semestre )
            semestre -= 1

            while (max < self.maxMateriasHabilitadas):
                cont = 1
                for i in self.planDeEstudios[semestre]:
                    print(cont,")", i["name"])
                    cont += 1
                materia = int(input())
                if materia == 0:
                    break
                if materia > cont-1:
                    continue
                materia -= 1

                self.data.append(self.planDeEstudios[semestre].pop(materia))
                max += 1

    def getData(self):
        return self.data