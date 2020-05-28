import pandas

from sigefes.models import UnidadeGestora, DespesaLiquidada, Credor, Processo, NotaLiquidacao
from sigefes.data_utils import converte_data


def processa_unidade_gestora(codigo, nome):

    queryset = UnidadeGestora.objects.filter(codigo=codigo)

    if not queryset.exists():
        unidade_gestora = UnidadeGestora()
        unidade_gestora.codigo = codigo
        unidade_gestora.nome = nome
        unidade_gestora.save()
    else:
        unidade_gestora = queryset[0]

    return unidade_gestora


def processa_credor(cpf_cnpj, nome):

    queryset = Credor.objects.filter(cpf_cnpj=cpf_cnpj)
    if not queryset.exists():
        credor = Credor()
        credor.cpf_cnpj = cpf_cnpj
        credor.nome = nome
        credor.save()
    else:
        credor = queryset[0]

    return credor


def processa_processo(numero):

    queryset = Processo.objects.filter(numero=numero)
    if not queryset.exists():
        processo = Processo()
        processo.numero = numero
        processo.save()
    else:
        processo = queryset[0]

    return processo


def processa_nota_liquidacao(data, numero):

    queryset = NotaLiquidacao.objects.filter(numero=numero)
    if not queryset.exists():
        nota_liquidacao = NotaLiquidacao()
        nota_liquidacao.numero = numero
        if data != " - ":
            nota_liquidacao.data = converte_data(data)
        nota_liquidacao.save()
    else:
        nota_liquidacao = queryset[0]

    return nota_liquidacao


def processa_arquivo_despesas_liquidadas_exercicio(file):

    df = pandas.read_excel(file, header=None)

    for row in df.values.tolist()[5:-9]:

        despesa_liquidada = DespesaLiquidada()

        unidade_gestora = processa_unidade_gestora(row[0], row[1])

        credor = processa_credor(row[2], row[3])

        processo = processa_processo(row[4])

        nota_liquidacao = processa_nota_liquidacao(row[5], row[6])

        despesa_liquidada.unidade_gestora = unidade_gestora
        despesa_liquidada.credor = credor
        despesa_liquidada.processo = processo
        despesa_liquidada.nota_liquidacao = nota_liquidacao
        despesa_liquidada.historico = row[7]
        despesa_liquidada.valor_liquidado = row[8]
        despesa_liquidada.save()


    return 'Foi'

