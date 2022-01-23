from python_excel2json import parse_excel_to_json
import copy
import glob

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
                    'name': 'full_name',
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
        }
    ]
}


def parse(path):
    files = glob.glob(path+'/*.xlsx')
    if len(files) == 0 or len(files) > 1:
        raise Exception('Должен быть 1 .xlsx файл')

    result = parse_excel_to_json(excel_sheets_format, filename=files[0])
    return result[0]['results']


def parse_applicants(applicants):
    copy_applicants = copy.deepcopy(applicants)
    extra = []

    for applicant in copy_applicants:
        full_name = applicant['full_name'].strip()
        names = full_name.split(' ')

        if len(names) == 3:
            last_name, first_name, middle_name = names
            applicant['last_name'] = last_name
            applicant['first_name'] = first_name
            applicant['middle_name'] = middle_name
        elif len(names) == 2:
            last_name, first_name = names
            applicant['last_name'] = last_name
            applicant['first_name'] = first_name
        else:
            raise Exception(f'Надо указать имя и фамилию (отчество опционально) у {full_name}')

        extra.append(
            {
                "full_name": full_name,
                "comment": applicant['comment'],
                "status": applicant['status']
            }
        )

        del applicant['full_name']
        del applicant['comment']
        del applicant['status']

    return copy_applicants, extra
