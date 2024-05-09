import random
from pyeasyga import pyeasyga

class HorarioGA:
    def __init__(self, data, subject_number = 6  ) -> None:
        
        def createIndividual(data):
        
            subjects = MAX_SUBJECT_NUMBER
            if len(data) < subjects:
                subjects = len(data)
            
            indixesChosen = random.sample(indexList, subjects)
            individual = []

            for index in indixesChosen:
                if index == -1:
                    individual.append([index, 0])

                else:
                    groupNumbers = data[index]["groups_available"]
                    chosenGroup = random.randrange(0, groupNumbers)
                    individual.append([index, chosenGroup])
            return individual
        
        def cruceUniforme(parent1, parent2):
            
            def add(newElement, child):
                if isinstance(newElement, (list, tuple)) and newElement[0] == -1:
                    child.append(newElement)
                elif elemRepited(newElement, child):
                    child.append([-1, 0])
                else:
                    child.append(newElement)
            
            def elemRepited(element, child):
                if isinstance(child, (list, tuple)) and hasattr(child, '__getitem__'):
                    return element in child
                return False 

            def createMask():
                mask = []

                while sum(mask) == 0 or sum(mask) == len(parent1): #que la mascara no sea 1 o 0
                    mask = [random.randint(0,1) for i in range(len(parent1))]
                return mask
            

            if len(parent1) > 1:
                mask = createMask()
                child1 = []
                child2 = []
                index = 0

                for value in mask:
                    if value == 0:
                        add(parent1[index], child1)
                        add(parent2[index], child2)
                    else:
                        add(parent2[index], child1)
                        add(parent1[index], child2)
                    index += 1
                return child1, child2
            else:
                return parent1, parent2
        
        def funcionFitness(individuos, data):
            fitness = 0
            semana = [[], [], [], [], [], []]
            for cromo in individuos:
                if isinstance(cromo, (list, tuple)) and len(cromo) > 0:
                    if cromo[0] > -1:
                        fitness += 10
                        grupos_disponibles = data[cromo[0]]["groups"]
                        grupo_seleccionado = cromo[1]
                        periodos = grupos_disponibles[grupo_seleccionado].shifts
                        for periodo in periodos:
                            semana[periodo.day.value].append(periodo.time_start.value) 
        
            for dia in semana:
                dia.sort()
                anteriorPeriodo = -1
                if len(dia) > 0:
                    for periodo in dia:
                        if anteriorPeriodo >= -1:
                            if anteriorPeriodo == periodo:
                                fitness -= 150

                        tamPuente = periodo- anteriorPeriodo - 1


                        if tamPuente > 0:
                            if tamPuente == 1:
                                fitness += 10
                            elif tamPuente == 2:
                                fitness += 6
                            elif tamPuente == 3:
                                fitness += 4
                            elif tamPuente == 4:
                                fitness += 2
                            else:
                                fitness -= 10
                        
                        else:
                            fitness += 12
                    
                    anteriorPeriodo = periodo
            return fitness

        def mutacionRandom(individual):

            def exists(idx, individual):
                repited = False
                for elem in individual:
                    if elem[0] > -1:
                        repited = idx == elem[0]
                        if repited:
                            break
                return repited
            
            def createOption(idx):
                subject = data[idx]
                groupNumber = subject["groups_available"]
                chosenGroup = random.randrange(0, groupNumber)
                return [idx, chosenGroup]

            def createAllAvailableGroups(candidates, idxSubject, lastGroup):
                subject = data[idxSubject]
                groupNumber = subject["groups_available"]
                i = 0
                while i < groupNumber -1:
                    if lastGroup != i:
                        candidates.append([idxSubject, i])
                    i += 1
            
            index = random.randrange(0, len(individual))
            elem = individual[index]
            newIndexList = indexList[1:]
            candidates = []
            if elem[0] == -1:
                for idxSubject in newIndexList:
                    if not exists(idxSubject, individual):
                        alleloOption = createOption(idxSubject)
                        candidates.append(alleloOption)
            else:
                candidates.append([-1,0])
                for idxSubject in newIndexList:
                    if idxSubject == elem[0]:
                        createAllAvailableGroups(candidates, idxSubject, elem[1])
                    elif not exists(idxSubject, individual):
                        alleloOption = createOption(idxSubject)
                        candidates.append(alleloOption)
            if len(candidates) > 0:
                newGen = random.choice(candidates)
                individual[index] = newGen 
        
        self.ga = pyeasyga.GeneticAlgorithm(data)
        MAX_SUBJECT_NUMBER = subject_number
        lengeth = len(data)
        indexList = list(range(-1, lengeth))
        self.ga.create_individual = createIndividual
        self.ga.crossover_function = cruceUniforme
        self.ga.fitness_function = funcionFitness
        self.ga.mutation_function = mutacionRandom
    
    def run(self):
        self.ga.run()
    
    def bestChromosome(self):
        return self.ga.best_individual()
    
    def lastGeneration(self):
        return self.ga.last_generation()