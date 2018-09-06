import configparser

cf = configparser.ConfigParser()
cf.read('test.ini')

value = cf.get('test','ip')
int_vlaue = cf.getint()
boolean_value = cf.getboolean()
float_value = cf.getfloat()
print(value)