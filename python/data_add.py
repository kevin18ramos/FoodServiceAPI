from gcc_postgres import task as t
from gcc_postgres import pcn


def connection():
    cn = pcn.d_cn(__file__)
    return cn


def quiz_input(value_dict,table_name='default_quiz',caller_file=__file__,schema_name='papasitos'):
    t.di_table(caller_file, schema_name, table_name, value_dict)



