# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import sys

SPREADSHEET_ID = "19vBtt1j64Au01vJaVjyiNB5CiCqSlG7juUc6_VSALbg"

def init_sheet(SPREADSHEET_ID):

    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    data_sheet = client.open_by_key(SPREADSHEET_ID).worksheet("data")
    return data_sheet

def encode_line(line_name):
    lines = {
        'azul':'1',
        'verde':'2',
        'vermelha':'3',
        'amarela':'4',
        'lilas':'5',
        'rubi':'7',
        'diamante':'8',
        'esmeralda':'9',
        'turquesa':'10',
        'coral':'11',
        'safira':'12',
        'prata':'15'
    }
    return lines[line_name]

def encode_status(status):
    status = status.lower()
    statuses = {
        'normal':'0',
        'velocidade reduzida':'1',
        'operação encerrada':'2',
        'paralisada':'3',
        'operação parcial':'4',
    }
    if(status in statuses):
        return statuses[status]
    else:
        raise Exception

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def export_text_files(data_sheet, initial_row, final_row):

    with open('inputs.txt', 'w') as inputs_file:
            with open('outputs.txt', 'w') as outputs_file:

                times = data_sheet.col_values(1)
                lines = data_sheet.col_values(2)
                states = data_sheet.col_values(3)

                inputs_file.write('ano mes dia dia_sem hora minuto linha\n')
                outputs_file.write('estado\n')

                for row in range(initial_row - 1 , final_row):
                    time = times[row]
                    line = lines[row]
                    stat = states[row]

                    time = datetime.strptime(time, '%d/%m/%Y %H:%M')
                    line = encode_line(line)
                    try:
                        stat = encode_status(stat)
                    except:
                        uprint(u"Unknown status ({}) detected in row {}. Skipping...".format(stat, row))
                        continue
                    
                    #print('writing row {}'.format(row))
                    inputs_file.write(" ".join(( str(time.year), str(time.month), str(time.day), str(time.weekday()), str(time.hour), str(time.minute), line)) + '\n')
                    outputs_file.write(stat + '\n')

def main():

    data_sheet = init_sheet(SPREADSHEET_ID)
    last_row = data_sheet.row_count
    export_text_files(data_sheet, 1, last_row)

main()