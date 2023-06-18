from ExtractTable import ExtractTable


def extract_table(file):
    et_sess = ExtractTable(api_key="aQNt1rjVeFXM3OTDd79TMLGROCpe2jonNPegSTE2")
    table_data = et_sess.process_file(filepath=file, output_format="df")
    et_sess.save_output("../csvs", output_format="csv")
    return table_data
