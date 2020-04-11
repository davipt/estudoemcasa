#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce
import uuid

# https://www.rtp.pt/estudoemcasa-apresentacao/#
periods = [
    ("0900", "0930"), ("0940", "1010"), ("1020", "1050"), ("1100", "1130"),
    ("1140", "1210"), ("1220", "1250"), ("1300", "1330"), ("1400", "1430"),
    ("1440", "1510"), ("1520", "1550"), ("1600", "1630"), ("1640", "1710"),
    ("1720", "1750"),
]

programs = [
    [
        ("Português", "1º e 2º Anos"),
        ("Hora de Leitura", "1º e 2º Anos"),
        ("Português", "3º e 4º Anos"),
        ("Matemática", "3º e 4º Anos"),
        ("Ciências Naturais", "5º e 6º Anos"),
        ("Português", "5º e 6º Anos"),
        ("Português Língua não materna (iniciação)", "1º ao 9º Ano"),
        ("Português", "7º e 8º Anos"),
        ("História e Cidadania", "7º e 8º Anos"),
        ("Espanhol", "3º Ciclo"),
        ("Português", "9º Ano"),
        ("Inglês", "9º Ano"),
        ("História", "9º Ano"),
    ], [
        ("Estudo do Meio e Cidadania", "1º e 2º Anos"),
        ("Educação Artística", "1º ao 9º Ano"),
        ("Estudo do Meio e Cidadania", "3º e 4º Anos"),
        ("Educação Física", "3º e 4º Anos"),
        ("Matemática", "5º e 6º Anos"),
        ("Educação Física", "5º e 6º Anos"),
        ("Português Língua não materna (iniciação)", "1º ao 9º Ano"),
        ("Inglês", "7º e 8º Anos"),
        ("Matemática", "7º e 8º Anos"),
        ("Alemão", "3º Ciclo"),
        ("Matemática", "9º Ano"),
        ("Ciências Naturais e Físico-Química", "9º Ano"),
        ("Educação Física", "9º Ano"),
    ], [
        ("Português", "1º e 2º Anos"),
        ("Matemática", "1º e 2º Anos"),
        ("Português", "3º e 4º Anos"),
        ("Matemática", "3º e 4º Anos"),
        ("Ciências Naturais e Cidadania", "5º e 6º Anos"),
        ("História e Geografia de Portugal", "5º e 6º Anos"),
        ("Português Língua não materna (iniciação)", "1º ao 9º Ano"),
        ("Ciências Naturais", "7º e 8º Anos"),
        ("Geografia e Cidadania", "7º e 8º Anos"),
        ("Francês", "3º Ciclo"),
        ("Ciências Naturais e Físico-Química", "9º Ano"),
        ("Matemática", "9º Ano"),
        ("Geografia e Cidadania", "9º Ano"),
    ], [
        ("Estudo do Meio", "1º e 2º Anos"),
        ("Educação Artística", "1º ao 9º Ano"),
        ("Hora de Leitura", "3º e 4º Anos"),
        ("Estudo do Meio", "3º e 4º Anos"),
        ("Matemática", "5º e 6º Anos"),
        ("Português", "5º e 6º Anos"),
        ("Português Língua não materna (iniciação)", "1º ao 9º Ano"),
        ("Físico-Química", "7º e 8º Anos"),
        ("Educação Física", "7º e 8º Anos"),
        ("Espanhol", "3º Ciclo"),
        ("Inglês", "9º Ano"),
        ("Matemática e Físico-Química", "9º Ano"),
        ("Português", "9º Ano"),
    ], [
        ("Matemática", "1º e 2º Anos"),
        ("Educação Física", "1º e 2º Anos"),
        ("Inglês", "3º e 4º Anos"),
        ("Oficina de Escrita", "5º e 6º Anos"),
        ("Inglês", "5º e 6º Anos"),
        ("História e Geografia de Portugal", "5º e 6º Anos"),
        ("Português Língua não materna (iniciação)", "1º ao 9º Ano"),
        ("Matemática", "7º e 8º Anos"),
        ("Português", "7º e 8º Anos"),
        ("Leitura e Literatura", "3º Ciclo"),
        ("Escrita", "3º Ciclo"),
        ("Francês", "3º Ciclo"),
        ("Alemão", "3º Ciclo"),
    ]
]

anos = list(map(lambda x: x[1], sum(programs, [])))
anos = list(set(anos))
anos.sort()
anos = ["tudo"] + anos


# DAY_OF_WEEK
DOW = ["MO", "TU", "WE", "TH", "FR"]

for ano in anos:
    file = ano.replace(" ", "_")
    f = open(f"cal_{file}.ics", "w")

    f.write("""
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:#estudoemcasa
X-WR-TIMEZONE:Europe/Lisbon
BEGIN:VTIMEZONE
TZID:Europe/Lisbon
X-LIC-LOCATION:Europe/Lisbon
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0000
TZNAME:WET
DTSTART:19701025T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+0000
TZOFFSETTO:+0100
TZNAME:WEST
DTSTART:19700329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
END:VTIMEZONE
""")

    for day in range(0, 5):
        for i in range(0, len(periods)):
            program = programs[day][i]
            if ano != 'tudo' and ano != program[1]: continue

            id = uuid.uuid4()
            dom = "%02d" % (20 + day)
            period = periods[i]
            f.write(f"""
BEGIN:VEVENT
DTSTART;TZID=Europe/Lisbon:202004{dom}T{period[0]}00
DTEND;TZID=Europe/Lisbon:202004{dom}T{period[1]}00
SUMMARY:{program[0]} ({program[1]})
STATUS:CONFIRMED
RRULE:FREQ=WEEKLY;UNTIL=20200731T225959Z;INTERVAL=1;BYDAY={DOW[day]}
SEQUENCE:1
TRANSP:TRANSPARENT
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC
BEGIN:VALARM
ACTION:AUDIO
TRIGGER:-PT5M
X-WR-ALARMUID:{id}
UID:{id}
ATTACH;VALUE=URI:Chord
END:VALARM
END:VEVENT
""")

    f.write("""
END:VCALENDAR
""")

    f.close()
