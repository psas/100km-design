# LV3.1 Design

The current rocket `psas_LV3.1.ork` is a back-of-the-envelope liquid fuel design.


## Performance

### Altitude: {{ altitude | round }} km

Notable metrics:

 Metric            | Number                               | Units
 ----------------- |------------------------------------- | -----
 Thrust            | {{ '%36.3f' | format(thrust)      }} | kN
 Burn time         | {{ '%36d' | format(burntime | int)}} | s
 Total Impulse     | {{ '%36d' | format(impulse | int) }} | N&middot;s
 Impulse Class     | {{ '%36s' | format(nar)           }} | -
 Peak Acceleration | {{ '%36.1f' | format(a_peak)      }} | g
 Burnout Velocity  | {{ '%36.1f' | format(v_burnout)   }} | m/s
 Burnout Mach      | {{ '%36.2f' | format(v_burnout_m) }} | Mach
 Burnout Altitude  | {{ '%36.2f' | format(alt_bo)      }} | km
 Liftoff Mass      | {{ '%36.1f' | format(m_0)         }} | kg
 Propellent Mass   | {{ '%36.1f' | format(prop)        }} | kg
 Dry Mass          | {{ '%36.1f' | format(m_1)         }} | kg
 Mass Ratio        | {{ '%36.2f' | format(m_r)         }} | -


## Motor

 Metric            | Number                               | Units
 ----------------- |------------------------------------- | -----
 Thrust            | {{ '%36.3f' | format(thrust)      }} | kN
 Isp               | {{ '%36d' | format(isp | int)     }} | s
 Design &Delta;V   | {{ '%36.1f' | format(dv_ideal)    }} | m/s
 Actual &Delta;V   | {{ '%36.1f' | format(v_burnout)   }} | m/s
 Gravity loss      | {{ '%36.1f' | format(dv_grav)     }} | m/s
 Drag loss         | {{ '%36.1f' | format(dv_drag)     }} | m/s
 Mass Ratio        | {{ '%36.2f' | format(m_r)         }} | -


## Figures Of Merit

Altitude per impulse is a figure of merit suggested by Ken Biba in his paper
outlining the successful Carmack prize wining two stage rocket. For reference
ARCAS sounding rocket had a ratio of 1.5 and GoFast was 0.2. Bigger is better.


 Metric            | Number                               | Units
 ----------------- |------------------------------------- | -----
 Altitude/Impulse  | {{ '%36.2f' | format(imp_ratio)   }} | m/N&middot;s
 Gravity loss      | {{ '%36.1f' | format(dv_grav)     }} | m/s
 Drag loss         | {{ '%36.1f' | format(dv_drag)     }} | m/s


## Aerodynamic Loading

 Metric            | Number                               | Units
 ----------------- |------------------------------------- | -----
 Max Q             | {{ '%36.2f' | format(max_q)       }} | kPa
 Time of Max Q     | {{ '%36.1f' | format(max_q_t)     }} | s
 Velocity at Max Q | {{ '%36.1f' | format(max_q_v)     }} | m/s
 Altitude at Max Q | {{ '%36.1f' | format(max_q_a)     }} | km
