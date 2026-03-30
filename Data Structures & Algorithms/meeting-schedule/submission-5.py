"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Ordenar por hora de inicio
        #ordenadas = sorted(intervals, key=lambda x: x.start)

        # Revisar solapamientos
        #for i in range(len(ordenadas) - 1):
        #    if ordenadas[i].end > ordenadas[i+1].start:
        #        return False
        #return True
        ordenadas = sorted(intervals, key=lambda x: x.start)

        # Comparar cada intervalo con el siguiente usando zip
        for actual, siguiente in zip(ordenadas, ordenadas[1:]):
            if actual.end > siguiente.start:  # solo mayor, no >=
                return False
        return True

