import configparser

cf = configparser.ConfigParser()
cf.read('test.ini')


TEST_ARGS = {
    'ip':cf.get('test','ip'),
    'int':cf.getint('test','int'),
    'float':cf.getfloat('test','float'),
    'bool':cf.getboolean('test','bool')
}

print(TEST_ARGS)

