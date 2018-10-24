# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:02:12 2018

@author: Publico
"""

# -*- coding: utf-8 -*-
"""
Generador de funciones Tektronix AFG 3021B
Manual U (web): https://github.com/hgrecco/labosdf-bin/raw/master/manuals/TektronixAFG3000.pdf
Manual P (web): https://github.com/hgrecco/labosdf-bin/raw/master/manuals/TektronixAFG3000_p.pdf
Manual U (local): \\Srvlabos\manuales\Tektronix\AFG3012B (M Usuario).pdf
Manual P (local): \\Srvlabos\manuales\Tektronix\AFG3012B (Prog Manual).pdf
"""

from __future__ import division, unicode_literals, print_function, absolute_import

import time

import numpy as np
import visa
import matplotlib.pyplot as plt
from pyvisa import resources, util
from pyvisa.resources import MessageBasedResource
print(__doc__)

# Este string determina el intrumento que van a usar.
# Lo tienen que cambiar de acuerdo a lo que tengan conectado.
resource_name = 'GPIB0::11::INSTR'

rm = pyvisa.ResourceManager()
print(rm.list_resources())
# Abre la sesion VISA de comunicacion
fungen = rm.open_resource(resource_name, resource_pyclass=MessageBasedResource)

print(fungen.query('*IDN?'))

# %%
#numpoint = 20
#values = np.uint16([int(x) for x in np.linspace(0, 16000, num=numpoint)])
values = np.arange(2**14-1, dtype=np.uint32)

#fungen.write('trace:define ememory, ' + str(numpoint))
fungen.write_binary_values('trace ememory, ', values, datatype='H', is_big_endian=True)
plt.plot(values)
fungen.write('FREQ %f' % 1)
fungen.write('VOLT %f' % 2)
fungen.write('VOLT:OFFS %f' % 0)
fungen.write('output1 on')
#fungen.write('output1 off')
#fungen.close()
