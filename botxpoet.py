#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version 0.2, 31.3.2015

# Python-Implementierung des Programms zur Herstellung "Stochastische[r] Texte" wie von Theo Lutz in einem Aufsatz beschrieben -
# Theo Lutz: Stochastische Texte, in: Barbara Büscher, Hans-Christian von Herrmann, Christoph Hoffmann: ästhetik als programm. Max Bense / daten und streuungen, Berlin 2004, S. 165-169.
# Im Anschluss an diesen Nachdruck des Aufsatzes (Erstdruck 1959) findet sich ein Faksimile des originalen Fernschreiberausdrucks (das Ergebnis der Versuche von
# Theo Lutz und Rul Gunzenhäuser). Beim Vergleich der im Aufsatz wiedergegebenen Texte mit dem Fernschreiberausdruck fallen, abgesehen von der vorgenommenen
# Auswahl, fünf Unterschiede ins Auge:
# 1. Das Leerzeichen vor dem Punkt, der die beiden Elementarsätze trennt, und das Fehlen eines Leerzeichens nach diesem Punkt
# 2. Die fehlende Deklination von "FREMDE" im Fernschreiberausdruck, dort heißt es "KEIN FREMDE IST NEU", weil eine Flexion der Nomen nicht vorgesehen war.
#    Dabei ist der FREMDE das einzige Wort, bei dem für die die Negation mit den unbestimmten Artikeln (ein, kein) eine Flexion erforderlich wäre.
# 3. Auf dem Fernschreiberausdruck fehlt der Punkt am Ende jeder Zeile
# 4. Die Reduktion von Umlauten auf den Stammlaut (WUTEND statt WÜTEND usw.).
# 5. Die Zusammenschreibung von SOGILT (im redigierten Text getrennt)

# Das vorliegende Programm ist eine Re-Implementierung des Textgenerators, die stillschweigenden Korrekturen am Text des Fernschreiberausdruck wurden
# zur Verbesserung der Lesbarkeit implementiert. Ausgenommen davon ist der FREMDE. Um hier grammatische Korrektheit zu erreichen, ohne eine Flexion
# extra zu programmieren, und um das gendering im Text zu reflektieren, wurde schlicht von Maskulinum auf Femininum geschaltet.

# Die folgende Implementierung generiert einzelne Sätze, die dann vom Bot botXpoet bei Twitter gepostet werden (Frequenz: zweimal pro Stunde).
# Insgesamt können 4 * (4 * 16 * 16)**2 = 4.194.304 Sätze generiert werden. Der Bot muss bei ununterbrochener Tätigkeit also 2.097.152 Stunden oder
# 87381 Tage (gerundet) oder 12.483 Wochen oder 2.912 Monate oder 239.4 Jahre arbeiten - vorausgesetzt jede Kombination erscheint nur einmal,
# was sehr unwahrscheinlich ist.
# Eine Möglichkeit wäre gewesen, sämtliche Kombinationen im Vorhinein zu berechnen und dann via Twitter zeilenweise auszugeben. Mir erschien aber der
# Zufall im Moment interessanter. Eine komplette Ausrechnung des Algorithmus wird es dann als E-Book geben.

import random

# satzmuster definieren

# kein haus ist nah und ein bauer ist fern.
# = op + n + ist + adj + opSatz + op + n + ist + adj + .

# vokabulare definieren
# das flexionsproblem wird über die stelle in der liste gelöst: m=liste[0], f=liste[1], n=liste[2]

operatoren = [["ein","eine","ein"], ["jeder","jede","jedes"], ["kein","keine","kein"], ["nicht jeder", "nicht jede", "nicht jedes"]]

subjekte = ["graf", "fremde", "blick", "kirche", "schloss", "bild", "auge", "dorf", "turm", "bauer", "weg", "gast", "tag", "haus", "tisch", "knecht"]
subjektGeschlecht = {"graf":0, "fremde":1, "blick":0, "kirche":1, "schloss":2, "bild":2, "auge":2, "dorf":2, "turm":0, "bauer":0, "weg":0, "gast":0, "tag":0, "haus":2, "tisch":0, "knecht":0}

praedikate = ["offen","still","stark","gut","schmal","nah","neu","leise","fern","tief","spaet","dunkel","frei","gross","alt","wuetend"]

satzOperatoren = [" und "," oder "," so gilt ",". ",". ",". ",". ",". "] # wahrscheinlichkeiten über anzahl der elemente in der liste gelöst

# elementarsatz zusammenstellen

# elemente auswählen und elementarsatz zusammenstellen
def elementarSatz(operatoren, subjekte, subjektGeschlecht, praedikate):
    '''
    wählt aus den gegebenen mengen die notwendigen Elemente aus und generiert eine Zeile (
    '''
    subjekt1 = random.choice(subjekte)
    subjekt2 = random.choice(subjekte)
    operator1 = random.choice(operatoren)[subjektGeschlecht[subjekt1]]
    operator2 = random.choice(operatoren)[subjektGeschlecht[subjekt2]]
    praedikat1 = random.choice(praedikate)
    praedikat2 = random.choice(praedikate)

    elementarSatz = operator1 + " " + subjekt1 + " ist " + praedikat1 + random.choice(satzOperatoren) + operator2 + " " + subjekt2 + " ist " + praedikat2 + "."
    return elementarSatz.upper()

print elementarSatz(operatoren, subjekte, subjektGeschlecht, praedikate)
    
