# Importando bibliotecas necessárias
import pandas as pd
import numpy as np

# Lendo o arquivo do dicionário de dados, ignorando a primeira linha
data_dict = pd.read_excel(r'C:\Users\User\Documents\portfolio\dicionario.xlsx', skiprows=1)

# Removendo linhas vazias na coluna 'Tamanho'
sizes = data_dict.Tamanho.dropna().values
sizes_int = sizes.astype(int)

# Obtendo os nomes das variáveis a partir do dicionário
variable_names = data_dict.iloc[:, 2].dropna()

# Lendo a base de dados a partir de um arquivo de texto
data_frame = pd.read_fwf(r'C:\Users\User\Documents\portfolio\PNS_2019.txt', header=None, dtype=str, widths=sizes_int)

# Coletando a descrição das variáveis
variable_desc = data_dict.iloc[1:, 4].dropna()

# Atribuindo as descrições como cabeçalhos das colunas do dataframe
data_frame.columns = variable_desc

# Selecionando algumas colunas de interesse
selected_columns = [0, 1, 2, 3, 6, 11, 58, 60, 61, 65, 66, 67, 76, 87,
                    164, 165, 166, 169, 170, 171, 172, 173, 174, 175, 176, 178, 179, 191,
                    202, 203, 205, 206, 215, 216, 221, 223, 
                    395, 397, 399,
                    450, 453, 489, 547, 555, 577, 590, 599,
                    615, 633, 646, 647, 655, 673,
                    806, 807, 810, 811, 812]

filtered_df = data_frame.iloc[:, selected_columns]

# Renomeando as colunas com novos nomes
filtered_df.columns = ['estado', 'estrato', 'UPA', 'ordem', 
                       'n_moradores', 'tipo_residencia',
                       'pessoas_residencia', 'condicao_residencia', 'genero', 'idade', 'etnia',
                       'coabita', 'estado_civil', 'educacao',
                       'plano_odonto', 'plano_saude',
                       'num_planos',
                       'duracao_plano',
                       'avaliacao_plano',
                       'plano_publico',
                       'plano_consultas',
                       'plano_exames',
                       'plano_internacao',
                       'plano_parto',
                       'custo',
                       'avaliacao_saude',
                       'estado_geral',
                       'consumo_12_meses',
                       'servicos_saude',
                       'servicos_cobertos',
                       'atendimento_sus',
                       'natureza_atendimento',
                       'internacao_12_meses',
                       'num_internacoes_12_meses',
                       'ultima_internacao_plano',
                       'ultima_internacao_sus',
                       'fumante',
                       'fumou_anteriormente',
                       'num_cigarros',
                       'hipertensao',
                       'monitoramento_hipertensao',
                       'diabetes',
                       'colesterol_alto',
                       'doenca_cardiaca',
                       'asma',
                       'artrite',
                       'problemas_coluna',
                       'depressao',
                       'saude_mental',
                       'enfisema',
                       'bronquite',
                       'cancer',
                       'insuficiencia_renal',
                       'moradores_15m',
                       'nivel_educacional',
                       'renda_residencial',
                       'renda_per_capita',
                       'faixa_renda_per_capita']

# Convertendo todas as colunas para tipo numérico
filtered_df = filtered_df.apply(pd.to_numeric)

# Criando uma nova coluna com siglas dos estados
state_abbreviations = {11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO',
                       21: 'MA', 22: 'PI', 23: 'CE', 24: 'RN', 25: 'PB', 
                       26: 'PE', 27: 'AL', 28: 'SE', 29: 'BA', 
                       31: 'MG', 32: 'ES', 33: 'RJ', 35: 'SP', 
                       41: 'PR', 42: 'SC', 43: 'RS', 
                       50: 'MS', 51: 'MT', 52: 'GO', 53: 'DF'}
filtered_df['sigla_estado'] = filtered_df['estado'].map(state_abbreviations)

# Salvando o dataframe filtrado em um arquivo CSV
filtered_df.to_csv(r'C:\Users\User\Documents\portfolio\pns_reduzido_2019.csv', sep='\t', encoding='utf-8')

# Contagem de valores ausentes em cada coluna
missing_values_count = filtered_df.isna().sum()

# Classificando o tipo de residência
filtered_df['tipo_residencia'] = filtered_df['tipo_residencia'].replace({1: 'casa',
                                                                         2: 'apartamento',
                                                                         3: 'outro',
                                                                         9: 'ignorado'})

# Agrupando as condições no domicílio
filtered_df['condicao_residencia'] = filtered_df['condicao_residencia'].replace({1: 'responsável',
                                                                                 2: 'cônjuge',
                                                                                 3: 'cônjuge',
                                                                                 4: 'filho(a)',
                                                                                 5: 'filho(a)', 
                                                                                 6: 'filho(a)',
                                                                                 7: 'parente',
                                                                                 8: 'parente',
                                                                                 9: 'parente',
                                                                                 10: 'parente', 
                                                                                 11: 'parente',
                                                                                 12: 'parente',
                                                                                 13: 'parente',
                                                                                 14: 'parente',
                                                                                 15: 'outro', 
                                                                                 16: 'outro',
                                                                                 17: 'outro',
                                                                                 18: 'outro',
                                                                                 19: 'outro'})

# Classificando o gênero
filtered_df['genero'] = filtered_df['genero'].replace({1: 'M', 2: 'F'})

# Classificando a etnia
filtered_df['etnia'] = filtered_df['etnia'].replace({1: 'branca', 
                                                      2: 'preta',
                                                      3: 'amarela',
                                                      4: 'parda',
                                                      5: 'indígena',
                                                      9: 'ignorado'})

# Estado civil
filtered_df['estado_civil'] = filtered_df['estado_civil'].replace({1: 'casada(o)',
                                                                    2: 'divorciada(o)',
                                                                    3: 'viúva(o)',
                                                                    4: 'solteira(o)', 
                                                                    9: 'ignorado'})

# Grau mais elevado de instrução
filtered_df['nivel_educacional'] = filtered_df['nivel_educacional'].replace({1: 'sem instrução',
                                                                           2: 'fundamental I',
                                                                           3: 'fundamental II',
                                                                           4: 'médio I', 
                                                                           5: 'médio II',
                                                                           6: 'superior I',
                                                                           7: 'superior II'})

# Faixa de renda per capita
filtered_df['faixa_renda_per_capita'] = filtered_df['faixa_renda_per_capita'].replace({1: 'até 1.4',
                                                                                          2: '1.4 a 1.2',
                                                                                          3: '1.2 a 1',
                                                                                          4: '1.2', 
                                                                                          5: '2 a 3',
                                                                                          6: '3 a 5',
                                                                                          7: 'mais de 5'})

# Último curso realizado
filtered_df['educacao'] = filtered_df['educacao'].replace({1: 'creche',
                                                             2: 'pré-escola',
                                                             3: 'alfabetização',
                                                             4: 'alfabetização jovens/adultos', 
                                                             5: 'primário antigo',
                                                             6: 'ginasial antigo',
                                                             7: 'fundamental',
                                                             8: 'EJA fundamental',
                                                             9: 'científico antigo',
                                                             10: 'médio',
                                                             11: 'EJA médio',
                                                             12: 'graduação',
                                                             13: 'especialização',
                                                             14: 'mestrado',
                                                             15: 'doutorado'})

# Plano de saúde - 1 - Sim, 2 - Não
filtered_df['plano_saude'] = filtered_df['plano_saude'].replace({1: '1', 2: '0'})

# Mantendo apenas os registros que informaram sobre o plano de saúde
filtered_df = filtered_df[filtered_df['plano_saude'].notnull()]

# Contagem de valores ausentes
missing_values_count = filtered_df.isna().sum()

# Organizando as colunas do dataframe
ordered_columns = ['estado', 'sigla_estado', 'estrato', 'UPA', 'ordem', 
                   'tipo_residencia', 'n_moradores', 'moradores_15m', 'pessoas_residencia', 
                   'condicao_residencia', 'renda_residencial', 'renda_per_capita', 'faixa_renda_per_capita',
                   'genero', 'idade', 'etnia', 'coabita', 
                   'estado_civil', 'educacao', 'nivel_educacional', 
                   'plano_odonto', 'plano_saude', 'num_planos', 
                   'duracao_plano', 'avaliacao_plano', 'plano_publico', 
                   'plano_consultas', 'plano_exames', 'plano_internacao', 
                   'plano_parto', 'custo', 'avaliacao_saude',
                   'estado_geral', 'consumo_12_meses', 'servicos_saude', 
                   'servicos_cobertos', 'atendimento_sus', 'natureza_atendimento', 
                   'internacao_12_meses', 'num_internacoes_12_meses', 
                   'ultima_internacao_plano', 'ultima_internacao_sus', 
                   'fumante', 'fumou_anteriormente', 'num_cigarros', 
                   'hipertensao', 'monitoramento_hipertensao', 
                   'diabetes', 'colesterol_alto', 'doenca_cardiaca', 
                   'asma', 'artrite', 'problemas_coluna', 
                   'depressao', 'saude_mental', 'enfisema', 
                   'bronquite', 'cancer', 'insuficiencia_renal']

# Reorganizando o dataframe de acordo com a nova ordem
filtered_df = filtered_df.loc[:, ordered_columns]

# Salvando o dataframe organizado em um arquivo CSV
filtered_df.to_csv(r'C:\Users\User\Documents\portfolio\pns_limpo_2019.csv', sep='\t', encoding='utf-8')

# Filtrando variáveis com muitos valores ausentes
final_df = filtered_df.loc[:, ['n_moradores', 'tipo_residencia', 'pessoas_residencia', 
                                 'condicao_residencia', 'genero', 'idade', 
                                 'etnia', 'estado_civil', 'plano_odonto', 
                                 'plano_saude', 'avaliacao_saude', 
                                 'estado_geral', 'moradores_15m', 
                                 'nivel_educacional', 'renda_residencial', 
                                 'renda_per_capita', 'faixa_renda_per_capita']]

# Removendo linhas com dados ausentes
final_df.dropna(inplace=True)

# Contando valores ausentes novamente
missing_values_count_final = final_df.isna().sum()

# Salvando o dataframe final em um arquivo CSV
final_df.to_csv(r'C:\Users\User\Documents\portfolio\pns_r_2019.csv', sep='\t', encoding='utf-8')
