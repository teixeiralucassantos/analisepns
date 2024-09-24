# Análise de Dados da Pesquisa Nacional de Saúde 2019

Este projeto tem como objetivo analisar os dados da Pesquisa Nacional de Saúde (PNS) de 2019, utilizando Python para processar e transformar os dados brutos em um formato mais acessível e significativo. A PNS é uma importante pesquisa realizada pelo Instituto Brasileiro de Geografia e Estatística (IBGE), que fornece informações sobre as condições de saúde da população brasileira.

## Funcionalidades

O código realiza as seguintes etapas:

1. **Carregamento dos Dados**: O dicionário de dados e a base da PNS são carregados a partir de arquivos Excel e texto, respectivamente.
2. **Limpeza dos Dados**: O código remove linhas vazias e converte as colunas para tipos numéricos adequados, facilitando a análise posterior.
3. **Transformação de Variáveis**: As variáveis são renomeadas e categorizadas, como a classificação do tipo de residência, estado civil, etnia, e grau de instrução.
4. **Criação de Novas Colunas**: O código adiciona novas colunas ao dataframe, como siglas dos estados e informações sobre planos de saúde.
5. **Filtragem de Dados**: Apenas os registros relevantes são mantidos, e as colunas são reorganizadas para melhor visualização.
6. **Análise de Dados Ausentes**: O código contabiliza valores ausentes, permitindo que os analistas identifiquem quais variáveis precisam ser tratadas.
7. **Exportação dos Resultados**: Os dataframes processados são salvos em arquivos CSV, prontos para análises adicionais ou visualizações.

## Lógica do Código

A lógica por trás do código se baseia na manipulação de dados com a biblioteca Pandas, que é amplamente utilizada para análise de dados em Python. O fluxo do código é estruturado para garantir que os dados sejam carregados, processados e exportados de forma eficiente. Cada etapa foi projetada para ser modular e clara, facilitando futuras modificações e adições.

## Importância da Análise

A análise dos dados da PNS é crucial para entender a saúde da população brasileira, identificar desigualdades no acesso aos serviços de saúde e planejar políticas públicas mais eficazes. Com os dados processados, pesquisadores e analistas podem realizar análises estatísticas, visualizações e relatórios que ajudam a informar decisões no setor de saúde.

## Como Usar

1. Clone o repositório para o seu computador.
2. Certifique-se de ter as bibliotecas necessárias instaladas:
   ```bash
   pip install pandas openpyxl
