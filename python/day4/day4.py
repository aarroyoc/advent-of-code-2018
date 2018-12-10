import re
from collections import defaultdict

def read_file(file):
    with open(file) as f:
        lines = f.readlines()
    lines.sort()
    return lines


def day4(file):
    lines = read_file(file)
    guard_prog = re.compile(r"[* ]+Guard #([0-9]+)")
    time_prog = re.compile(r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)")
    current_guard = 0
    start_time = 0
    end_time = 0
    timetable = defaultdict(lambda: defaultdict(lambda: 0))
    for line in lines:
        # Hay tres tipos de líneas
        # Guardia, Sleep, Wake
        a = guard_prog.match(line.split("]")[1])
        if a != None:
            current_guard = a.group(1)
        elif "falls" in line:
            t = time_prog.match(line.split("]")[0])
            start_time = int(t.group(5))
        elif "wakes" in line:
            t = time_prog.match(line.split("]")[0])
            end_time = int(t.group(5))
            for i in range(start_time,end_time):
                timetable[current_guard][i] += 1

    # Calcular horas dormido
    max_guard = ""
    max_guard_sleeptime = 0
    for guard in timetable:
        s = sum(timetable[guard].values())
        if s > max_guard_sleeptime:
            max_guard_sleeptime = s
            max_guard = guard

    #print("El guardia que más duerme es el %s con %d minutos" % (max_guard,max_guard_sleeptime))

    #Calcular minuto ideal
    max_minute = 0
    max_minute_times = 0
    for minute in timetable[max_guard]:
        if timetable[max_guard][minute] > max_minute_times:
            max_minute = minute
            max_minute_times = timetable[max_guard][minute]

    #print("El guardia duerme más en el minuto %d (%d veces)" % (max_minute,max_minute_times))

    #print("CHECKSUM %d" % (max_minute*int(max_guard)))
    checksum1 = max_minute*int(max_guard)

    # Guarda con el minuto qué mas veces ha estado dormido
    max_guard = ""
    guard_minute = 0
    guard_minutes = 0
    for guard in timetable:
        for minute in timetable[guard]:
            if timetable[guard][minute] > guard_minutes:
                max_guard = guard
                guard_minute = minute
                guard_minutes = timetable[guard][minute]
    #print("El guardia %s se ha dormindo en el minuto %d (%d veces)" % (max_guard,guard_minute,guard_minutes))
    #print("CHECKSUM %d" % (guard_minute*int(max_guard)))
    checksum2 = guard_minute*int(max_guard)
    return checksum1,checksum2