import csv
import json
import pandas
from django.core.files.storage import FileSystemStorage

from sigefes.models import UnidadeGestora


def processa_arquivo_despesas_pagas_exercicio(file):

    df = pandas.read_excel(file, header=None)

    for row in df.values.tolist()[1:]:
        unidade_gestora = UnidadeGestora()
        unidade_gestora.codigo = row[0]
        print(unidade_gestora.codigo)
        unidade_gestora.save()

    return 'Foi'
    # for chunk in f.chunks():
    #     print(chunk)
    #     pandas.read_csv(chunk, sep='\t', engine='python')
        # with open(chunk, encoding='windows-1252') as csvFile:
        #     csvReader = csv.DictReader(csvFile)
        #     for rows in csvReader:
        #         id = rows['id']
        #         data[id] = rows

    #print('tesete' + data)
    # jsonFilePath = 'drive2.json'
    #
    # data = {}
    #
    # with open(arquivo['file']) as csvFile:

    #
    # with open(jsonFilePath, 'w') as jsonFile:
    #     jsonFile.write(json.dumps(data, ident=4))


