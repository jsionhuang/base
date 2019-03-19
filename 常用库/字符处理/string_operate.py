site_url = 'https://www.shein.com/ca'
site_tp = 'shein'
str = 'm'
if 'm' is str :
    print('yes')

print(site_tp is 'shein')
print(not(site_url.split('//')[1].startswith('m')))
if (site_tp is 'shein') and not (site_url.split('//')[1].startswith('m')):
#if 's' in 'async ' and not ('s' is 'd'):
    print('执行')
