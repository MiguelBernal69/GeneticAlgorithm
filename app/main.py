from HorarioGA import HorarioGA
from HorarioSelector import subjectSelector

selector = subjectSelector()
selector.startSelectMaterias()
data = selector.getData()

if len(data) > 0:
    ga = HorarioGA(data, subject_number=6)
    ga.run()

    print(data)
    print(ga.bestChromosome())