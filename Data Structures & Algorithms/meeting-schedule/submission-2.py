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
        ordenadas = sorted(intervals, key=lambda x: x.start)

        # Revisar solapamientos
        for i in range(len(ordenadas) - 1):
            if ordenadas[i].end > ordenadas[i+1].start:
                return False
        return True

