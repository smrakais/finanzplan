from texutils import *


def multiply(chain, array):
    array *= 10

actions = (TxtData('data/test.txt', ['I', 'U'], [10 * ureg.mA, ureg.volt])
    .plot('U', 'I')
    .linReg('U', 'I')
    .manipulate(multiply, 'I')
    .linReg('U', 'I')
    .plot('U', 'I')
    .describePlot('U', 'I')
    .savePlot('build/plot.pdf'))

actions.execute()