import math
import plotly.graph_objects as go
import numpy as np

import sys

sys.stdout = open('DANE', 'w')

y2_fin = np.zeros(1000000)
y3_fin = np.zeros(1000000)
iterate = 0


def rel_err(a, b):
    n = (math.exp(a) - b) / math.exp(a)
    return abs(n)


# ZE WZORU TAYLORA


def taylor_e(x, n):
    a = x
    z = 0
    for i in range(0, n):
        if i == 0:
            z += 1
        else:
            z += x / (math.factorial(i))
            x *= a
    return z


def taylor_e_reverse(x, n):
    a = x
    z = 0
    i = 0
    while i < n - 2:
        x *= a
        i += 1

    for i in range(n - 1, -1, -1):
        if i == 0:
            z += 1
        else:
            z += x / (math.factorial(i))
            x /= a
    return z


# ZE WZORU NA POPRZEDNI WYRAZ


def taylor_e_rec(x, n):
    if n == 0:
        return 1
    else:
        return taylor_e_rec(x, n - 1) * (x / n)


def sum_e_rec(x, n):
    z = 0
    for i in range(0, n):
        z += taylor_e_rec(x, i)
    return z


def sum_e_reverse_rec(x, n):
    z = 0
    for i in range(n - 1, -1, -1):
        z += taylor_e_rec(x, i)
    return z


def precision_test(y11, y22, x):
    global iterate
    flag = True
    print('e^' + str(x) + '\n')
    for j in range(y11.shape[0]):

        y22[j] = math.exp(x) - test_function(x, j, taylor_e)
        if y22[j] < 0.000001 and flag is True:
            print(
                'Przy ' + str(j) + ' wyrazach osiagamy dokladnosc 10^-6, stosunek ilosci wyrazow do argumentu = ' + str(
                    j / x))
            y2_fin[iterate] = j
            y3_fin[iterate] = j / x
            iterate = iterate + 1
            flag = False
            break

    print('\n\n')


def absolute(zabs):
    if zabs < 0:
        zabs = -zabs
    return zabs


x = np.arange(0.0000002, 0.2000002, 0.0000002)
y1 = np.zeros(1000000)
y2 = np.zeros(1000000)
y3 = np.zeros(1000000)
y4 = np.zeros(1000000)

for j in range(x.shape[0]):
    z1 = absolute(taylor_e(x[j], 10)-math.exp(x[j]))
    z2 = absolute(taylor_e_reverse(x[j], 10)-math.exp(x[j]))
    z3 = absolute(sum_e_rec(x[j], 10)-math.exp(x[j]))
    z4 = absolute(sum_e_reverse_rec(x[j], 10)-math.exp(x[j]))
    print(z1, z2, z3, z4)
    y1[j] = z1
    y2[j] = z2
    y3[j] = z3
    y4[j] = z4
    print(j)

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure()
fig5 = go.Figure()

fig1.add_trace(go.Scatter(x=x, y=y1,
                          mode='lines',
                          name='Wzor Taylora'))

fig1.add_trace(go.Scatter(x=x, y=y2,
                          mode='lines',
                          name='Wzor Taylora sumowany odwrotnie'))

fig2.add_trace(go.Scatter(x=x, y=y3,
                           mode='lines',
                           name='Ze wzoru na poprzedni wyraz'))

fig2.add_trace(go.Scatter(x=x, y=y4,
                           mode='lines',
                           name='Ze wzoru na poprzedni, \n sumowany odwrotnie'))

fig3.add_trace(go.Scatter(x=x, y=y1,
                          mode='lines',
                          name='Wzor Taylora'))

fig3.add_trace(go.Scatter(x=x, y=y3,
                           mode='lines',
                           name='Ze wzoru na poprzedni wyraz'))


fig4.add_trace(go.Scatter(x=x, y=y1,
                          mode='lines',
                          name='Wzor Taylora'))


fig5.add_trace(go.Scatter(x=x, y=y3,
                           mode='lines',
                           name='Ze wzoru na poprzedni wyraz'))

fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()

fig1.write_image("C:/Users/Domi/Desktop/prgrmng/fig1.pdf")
fig2.write_image("C:/Users/Domi/Desktop/prgrmng/fig2.pdf")
fig3.write_image("C:/Users/Domi/Desktop/prgrmng/fig3.pdf")

#
# # TEST 2 - HIPOTEZA H1 - TEST ILOSCI SKLADNIKOW
#
#
# y1 = np.arange(1000000)
# y2 = np.zeros(1000000)
# y1_fin = np.arange(1, 5.00000, 0.000004)
#
# for i in np.arange(1, 5.00000, 0.000004):
#     precision_test(y1, y2, i)
#
#
# fig5 = go.Figure()
# fig5.add_trace(go.Scatter(x=y1_fin, y=y2_fin,
#                           mode='lines',
#                           name='Pierwszy z dokladnoscia 10^-6'))
# fig5.add_trace(go.Scatter(x=y1_fin, y=y3_fin,
#                           mode='lines',
#                           name='y/x'))
#
# fig5.show()

# Referencje do kodu:
# https://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-ex/
# https://plot.ly/python/reference/
