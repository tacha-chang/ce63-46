from parinya import LINE
token_kmitl = 'SuWZzmcKMMH5RvFaglsCT8jWlIDEBltqjEwhNR7aepd'
line = LINE(token_kmitl)
msg ='''Morning report 3/19/2021
Name    Arrival Status
Tachrat 9.00    on time
Kree    9.45    late
'''
line.sendtext(msg)
