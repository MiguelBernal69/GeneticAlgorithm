import sys


class HorarioIU:
    def __init__(self, data, chromosome)-> None:
        self.data = data
        self.cromosoma = chromosome

        visited = {}
        datos = chromosome[1]        
        print(chromosome[0])        
        print(type(chromosome[0]))
        for gen in datos:
           
            if gen[0] > -1:
    
                subject = data[gen[0]]
                
                group = subject["groups"][gen[1]]
                shifts = group.shifts

                for shift in shifts:
                    row = shift.day.value
                    column = shift.time_start.value
                    llave = str(row) + str(column)

                    # if llave in visited:
                    #     cellText = visited[llave]
                    #     print(llave)
                    # else: 
                    #     print(llave)

                    #print(subject["code"])