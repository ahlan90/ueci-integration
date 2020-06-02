import pandas

from segregacao_funcao.models import DespesaPrevidenciariaPatronal, ContaContribuicao
from sigefes.processa_dados import processa_unidade_gestora


def processa_conta(codigo, descricao):

    queryset = ContaContribuicao.objects.filter(codigo=codigo)
    if not queryset.exists():
        conta = ContaContribuicao()
        conta.codigo = codigo
        conta.descricao = descricao
        conta.save()
    else:
        conta = queryset[0]

    return conta


def processa_arquivo_contribuicao_patronal(file):

    df = pandas.read_excel(file, header=None)

    for row in df.values.tolist()[5:-12]:

        despesa_previdenciaria_patronal = DespesaPrevidenciariaPatronal()

        unidade_gestora = processa_unidade_gestora(row[0], row[1])

        conta = processa_conta(row[3], row[4])

        despesa_previdenciaria_patronal.mes = row[2]
        despesa_previdenciaria_patronal.unidade_gestora = unidade_gestora
        despesa_previdenciaria_patronal.conta = conta
        despesa_previdenciaria_patronal.saldo = row[5]

        despesa_previdenciaria_patronal.save()

    return 'Foi'

