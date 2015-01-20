#!/usr/bin/env python
from __future__ import print_function
import csv
from math import log, fabs
from jinja2 import Template

results = {}

times = []
t_bo = 0
altitudes = []
velocitys = []
masses = []
machs = []
thrusts = []
temps = []
pressures = []
accels = []
qs = []
with open('sim.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        time = row[0]
        if time[0] == '#':
            if 'BURNOUT' in time:
                t_bo = time.split('t=')[1].split(' ')[0]
                t_bo = float(t_bo)
            continue

        times.append(float(time))
        altitudes.append(float(row[ 1]))
        velocitys.append(float(row[ 2]))
        accels.append(   float(row[ 3]))
        masses.append(   float(row[19]))
        machs.append(    float(row[26]))
        thrusts.append(  float(row[28]))
        temps.append(    float(row[49]))
        pressures.append(float(row[50]))

for i, p in enumerate(pressures):
    rho = p / (287.058*temps[i])
    v = velocitys[i]
    qs.append(0.5*rho*v*v)

i_max_q = qs.index(max(qs))

i_t_bo = times.index(t_bo)

Isp      =   230.0      # s       Specific Impulse
g_0      =     9.80665  # kg.m/s/s
thrust   =  thrusts[10]

m_r = masses[0]/masses[-1]
dv_pure =  g_0 * Isp * log(m_r)
dv_grav = (g_0 * Isp * log(m_r)) - (g_0 * t_bo)

impulse = thrust*t_bo
nar_i = int(log(impulse/2.5)/log(2))
nar_percent = impulse/(2.5*2**(nar_i+1))


results['thrust'] = thrust/1000.0
results['isp'] = Isp
results['altitude'] = max(altitudes)
results['a_peak'] = max(accels[0:i_t_bo])/g_0
results['v_burnout'] = velocitys[i_t_bo]
results['v_burnout_m'] = machs[i_t_bo]
results['burntime'] = times[i_t_bo]
results['alt_bo'] = altitudes[i_t_bo]
results['impulse'] = impulse
results['nar'] = '**%s** (%0.0f%%)' % (chr(66+nar_i), nar_percent*100)
results['m_0'] = masses[0]
results['m_1'] = masses[-1]
results['prop'] = masses[0] - masses[-1]
results['m_r'] = m_r
results['dv_ideal'] = dv_pure
results['dv_grav'] = fabs(dv_grav - dv_pure)
results['dv_drag'] = fabs(dv_grav - velocitys[i_t_bo])
results['imp_ratio'] = (max(altitudes)*1000)/impulse
results['max_q'] = qs[i_max_q]/1000.0
results['max_q_t'] = times[i_max_q]
results['max_q_v'] = velocitys[i_max_q]
results['max_q_a'] = altitudes[i_max_q]

with open('./templates/readme.markdown', 'r') as t:
    template = Template("_Note: This is a generated file, do not edit directly._\n\n"+t.read())

with open('./README.markdown', 'w') as readme:
    readme.write(template.render(results))
