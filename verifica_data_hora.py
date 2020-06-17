# 
# verifica_data_hora.py
# 
# libs: requests, time, sys, ntplib, os
# 
# Atencao!
# Para modificar data/hora no terminal, 
# WIN - necessário executar como 'administrador'.
# LNX - necessário executar 'sudo'.
# 
# *** os.system('date {}/{}/{}'.format(t.tm_mday, t.tm_mon, t.tm_year))
# *** os.system('time {}:{}:{}'.format(t.tm_hour, t.tm_min, t.tm_sec))

import requests, time, sys, ntplib, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # srv_ntp_br = ['a.ntp.br', 'b.ntp.br', 'c.ntp.br', 'gps.ntp.br']
    srv_ntp_br = 'a.ntp.br'
    # clear()
    print('Mauricio Portela Pires - 2020')
    print('Vitoria da Conquista - BA-BRA\n')
    try:
        m = ntplib.NTPClient().request(srv_ntp_br, version=4).tx_time
        t = time.localtime(m)
        print('{} - {}'.format(srv_ntp_br,str(time.ctime(m))))
        print('date {}/{}/{}'.format(t.tm_mday, t.tm_mon, t.tm_year))
        print('time {}:{}:{}'.format(t.tm_hour, t.tm_min, t.tm_sec))
    except Exception as e:
        print(e)
