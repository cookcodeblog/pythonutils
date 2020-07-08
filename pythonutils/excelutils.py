# Excel utils
import xlrd
import xlwt


def get_excel_sheet_records(sheet, include_header):
    records = []
    for row_index in range(sheet.nrows):
        if not include_header and row_index == 0:
            continue
        record = sheet.row_values(row_index)
        records.append(record)

    return records


def read_excel_sheet1(file_name, include_header=False):
    """
    Read the first sheet of Excel (*.xls)

    :param file_name: Excel file name (*.xls)
    :param include_header: If include header, default is False
    :return: Record list, each record is a row of Excel
    """
    return read_excel_sheet_by_index(file_name, 0, include_header)


def read_excel_sheet_by_index(file_name, sheet_index, include_header=False):
    """
    Read a given sheet of Excel (*.xls)

    :param file_name: Excel file name (*.xls)
    :param sheet_index: Index of sheet, from 0
    :param include_header: If include header, default is False
    :return: Record list, each record is a row of Excel
    """
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_index(sheet_index)
    return get_excel_sheet_records(sheet, include_header)


def read_excel_sheet_by_name(file_name, sheet_name, include_header=False):
    """
    Read a given sheet of Excel(*.xls) by sheet name

    :param file_name: Excel file name (*.xls)
    :param sheet_name: Sheet name
    :param include_header: If include header, default is False
    :return: Record list, each record is a row of Excel
    """
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_name(sheet_name)
    return get_excel_sheet_records(sheet, include_header)


def get_excel_sheet_headers(sheet):
    for row_index in range(sheet.nrows):
        if row_index == 0:
            return sheet.row_values(row_index)
    return list()


def read_excel_headers_by_index(file_name, sheet_index):
    """
    Read Excel (*.xls) headers by sheet index
    :param file_name: Excel file name (*.xls)
    :param sheet_index: Sheet Index
    :return: Headers, first row of sheet
    """
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_index(sheet_index)
    return get_excel_sheet_headers(sheet)


def read_excel_headers_sheet1(file_name):
    """
    Read Excel (*.xls) headers of the first sheet
    :param file_name: Excel file name (*.xls)
    :return: Headers, first row of sheet
    """
    return read_excel_headers_by_index(file_name, 0)


def write_excel_one_sheet(file_name, sheet_name, headers, records, encoding='GB18030'):
    """
    Write an Excel(*.xls) on one sheet

    :param file_name: Excel file name (*.xls)
    :param sheet_name: Sheet name
    :param headers: Headers, array, first row of sheet
    :param records: Records, array, data rows of sheet
    :param encoding: File encoding, default is GB18030
    :return:
    """
    workbook = xlwt.Workbook(encoding=encoding)
    sheet = workbook.add_sheet(sheet_name)

    for col_index in range(len(headers)):
        sheet.write(0, col_index, label=headers[col_index])

    for row_index in range(len(records)):
        record = records[row_index]
        for col_index in range(len(record)):
            value = record[col_index]
            sheet.write(1 + row_index, col_index, label=value)

    workbook.save(file_name)
