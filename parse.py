from python_excel2json import parse_excel_to_json

excel_sheets_format = {
    'start_row_sheet_parsing': 1,
    'start_column_sheet_parsing': 0,
    'sheet_formats': [
        {
            'sheet_index': 0,
            'column_names': [
                {
                    'name': 'position',
                    'type': 'str'
                },
                 {
                    'name': 'fio',
                    'type': 'str'
                },
                {
                    'name': 'money',
                    'type': 'str'
                },
                {
                    'name': 'comment',
                    'type': 'str'
                },
                {
                    'name': 'status',
                    'type': 'str'
                },
            ],
            'is_ordered': True
        }
    ]
}

file = 'test/Тестовая база.xlsx'
result = parse_excel_to_json(excel_sheets_format, filename=file)

print(result)
