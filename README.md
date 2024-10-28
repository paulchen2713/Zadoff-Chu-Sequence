# Zadoff-Chu-Sequence

## Python
Try running ```zadoff_chu_sequence``` on [Online Numpy Compiler](https://python-fiddle.com/saved/qAQ5sacqokXsoDJm4UF8?run=true)

Sample output of ```zadoff_chu_sequence(10, 7, 1)```:
```
[ 1.00000000e+00+0.00000000e+00j  9.51056516e-01-3.09016994e-01j
  3.09016994e-01+9.51056516e-01j -4.90477700e-16-1.00000000e+00j
 -8.09016994e-01-5.87785252e-01j -5.88139954e-15-1.00000000e+00j
  3.09016994e-01+9.51056516e-01j  9.51056516e-01-3.09016994e-01j
  1.00000000e+00+6.85802208e-15j -5.87785252e-01+8.09016994e-01j]
```


## MATLAB
Sample output of ```zadoff_chu_sequence(10, 7, 1)```:
```
zc_sequence =
   1.0000 + 0.0000i   0.9511 - 0.3090i
   0.3090 + 0.9511i  -0.0000 - 1.0000i
  -0.8090 - 0.5878i   0.0000 - 1.0000i
   0.3090 + 0.9511i   0.9511 - 0.3090i
   1.0000 + 0.0000i  -0.5878 + 0.8090i
```

Output of ```print_sequence(zc_sequence)```:
```
#01   1.0000 +  0.0000j, r = 1.0, theta =  0.0000 =  0.0
#02   0.9511 + -0.3090j, r = 1.0, theta = -0.3142 = -18.0
#03   0.3090 +  0.9511j, r = 1.0, theta =  1.2566 =  72.0
#04  -0.0000 + -1.0000j, r = 1.0, theta = -1.5708 = -90.0
#05  -0.8090 + -0.5878j, r = 1.0, theta = -2.5133 = -144.0
#06   0.0000 + -1.0000j, r = 1.0, theta = -1.5708 = -90.0
#07   0.3090 +  0.9511j, r = 1.0, theta =  1.2566 =  72.0
#08   0.9511 + -0.3090j, r = 1.0, theta = -0.3142 = -18.0
#09   1.0000 +  0.0000j, r = 1.0, theta =  0.0000 =  0.0
#10  -0.5878 +  0.8090j, r = 1.0, theta =  2.1991 =  126.0
```

Output figure of the phase and the magnitude: \
![螢幕擷取畫面 2024-10-26 165129](https://github.com/user-attachments/assets/93d7bbe8-3521-4ef7-be55-fa4de9b96a2f)


