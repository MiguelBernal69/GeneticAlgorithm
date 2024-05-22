from app.HorarioGA import HorarioGA
from app.HorarioSelector import subjectSelector
from app.HorarioIU import HorarioIU
selector = subjectSelector()
selector.startSelectMaterias()
data = selector.getData()

if len(data) > 0:
    ga = HorarioGA(data, subject_number=6)
    ga.run()

    HorarioIU(data, ga.bestChromosome())
    horario = HorarioIU(data, ga.bestChromosome())
    horario.show()
    
