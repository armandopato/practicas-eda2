# pip install pandas
import pandas

from parsing import parseCsv
from printBoth import printBothFactory


def analyzeData():
    columns, entries = parseCsv()
    dataFrame = pandas.DataFrame(entries, columns=columns)

    file = open("PracticaResumen/resumenCovid.eda2", "w")
    printBoth = printBothFactory(file)

    printBoth("\nTotal de casos:", len(dataFrame))

    printBoth("\n            Casos por estado")
    casesPerState = dataFrame["Nom_Ent"].value_counts()
    printBoth(casesPerState.to_string())

    printBoth("\nEstado con más casos:", casesPerState.idxmax())
    printBoth("Estado con menos casos:", casesPerState.idxmin())

    printBoth("\nCasos por género")
    casesPerGender = dataFrame["SEXO"].value_counts()
    printBoth(casesPerGender.to_string())

    printBoth("\nPromedio de edad:", dataFrame["EDAD"].mean())
    printBoth("\nEdad máxima:", dataFrame["EDAD"].max())
    printBoth("Edad mínima:", dataFrame["EDAD"].min())

    file.close()
