import os
import ast
import base64

from datetime import datetime
from importdata.models import PatentCode, Patent, PatentAuthor, InterPatentCode, LawStatusEvent
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "import data to use"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('begin import'))
        write_database()
        self.stdout.write(self.style.SUCCESS('end import'))

def write_database():
    data = []

    PA = []
    LSE = []
    IPC = []
    PCode = []

    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    data_path = os.path.join(basedir, 'static_files')

    data_file = os.path.join(data_path, 'H04-100.txt')

    with open(data_file) as f:
        for line in f.readlines():
            data_line = ast.literal_eval(line.strip())

            data_dict = {}

            for item in data_line.items():
                if item[1] != '':
                    if item[0] == 'id':
                        data_dict[item[0]] = item[1]
                    else:
                        data_dict[item[0]] = base64.b64decode(item[1]).decode('unicode_escape')

                    if item[0] == 'PA':
                        tmp = data_dict[item[0]].split('&&&')
                        if 'GOOGLE公司' in tmp:
                            tmp[tmp.index('GOOGLE公司')] = '谷歌公司'
                            data_dict[item[0]] = '&&&'.join(tmp)
                        PA.extend(tmp)
                    elif item[0] == 'CDN' or item[0] == 'CTN':
                        tmp = data_dict[item[0]].split('&&&')
                        PCode.extend(tmp)

                    elif item[0] == 'IPC':
                        tmp = data_dict[item[0]].split('&&&')
                        IPC.extend(tmp)
                    elif item[0] == 'LSE':
                        tmp = data_dict[item[0]].split(';')

                        if 'PATENT GRANT' in tmp:
                            tmp[tmp.index('PATENT GRANT')] = '授权'

                        tmp = list(set(tmp))
                        data_dict[item[0]] = '&&&'.join(tmp)

                        LSE.extend(tmp)
                else:
                    data_dict[item[0]] = ''
            data.append(data_dict)

    PA = list(set(PA))
    LSE = list(set(LSE))
    IPC = list(set(IPC))
    PCode = list(set(PCode))

    print('read completely')

    PatentCode.objects.all().delete()
    Patent.objects.all().delete()
    LawStatusEvent.objects.all().delete()
    InterPatentCode.objects.all().delete()
    PatentAuthor.objects.all().delete()

    print('Deleted successfully')

    for name in PA:
        pa = PatentAuthor()
        pa.name = name
        pa.save()

    print('PA added!')

    for name in LSE:
        lse = LawStatusEvent()
        lse.name = name
        lse.save()

    print('LSE added!')

    for code in IPC:
        ipc = InterPatentCode()
        ipc.code = code
        ipc.firstcode = code.split('/')[0]
        ipc.seccode = code.split('/')[1]
        ipc.save()

    print('IPC added!')

    for code in PCode:
        pc = PatentCode()
        pc.code = code
        pc.save()

    print('PCode added!')

    for item in data:
        patent = Patent()
        patent.ab = item['AB']
        patent.ti = item['TI']
        patent.clm = item['CLM']
        patent.pid = item['id']
        patent.an = item['AN']
        patent.pn = item['PN']
        patent.ls = item['LS']
        patent.ad = datetime.strptime(item['AD'], '%Y%m%d').date()
        patent.pd = datetime.strptime(item['PD'], '%Y%m%d').date()
        tmp_pa = item['PA'].split('&&&')
        patent.save()

        for x in tmp_pa:
            if x == '':
                break
            pa = PatentAuthor.objects.get(name=x)
            patent.pa.add(pa)
        patent.save()

        tmp_ipc = item['IPC'].split('&&&')
        for x in tmp_ipc:
            if x == '':
                break
            ipc = InterPatentCode.objects.get(code=x)
            patent.ipc.add(ipc)
        patent.save()

        tmp_lse = item['LSE'].split('&&&')
        for x in tmp_lse:
            if x == '':
                break
            lse = LawStatusEvent.objects.get(name=x)
            patent.lse.add(lse)
        patent.save()

        tmp_pc = item['CDN'].split('&&&')
        for x in tmp_pc:
            if x == '':
                break
            cdn = PatentCode.objects.get(code=x)
            patent.cdn.add(cdn)
        patent.save()


        tmp_pc = item['CTN'].split('&&&')
        for x in tmp_pc:
            if x == '':
                break
            ctn = PatentCode.objects.get(code=x)
            patent.ctn.add(ctn)
        patent.save()
