# Synchronous machine connected to infinite bus

# Make sure to change parameters according to hand calculations!

def load():
    return {
        'base_mva': 50,
        'f': 50,
        'slack_bus': 'B3',

        'buses': [
            ['name',    'V_n'],
            ['B1',       100],
            ['B2',      100],
            ['B3',      100],
        ],

        'lines': [
            ['name',    'from_bus', 'to_bus',   'length',   'S_n',  'V_n',  'unit', 'R',    'X',      'B'],
            ['L2-3',    'B2',       'B3',       100,         100,    100,     'PF',   0,   0.2,     0],
        ],

        'transformers': [
            ['name', 'from_bus', 'to_bus', 'S_n', 'V_n_from', 'V_n_to', 'R', 'X'],
            ['T1',      'B1',     'B2',     100,     100,         100,     0,   0.2],
        ],

        'loads': [
            ['name', 'bus', 'P', 'Q', 'model'],
            ['L1', 'B2', 100, 0, 'Z'],
        ],

        'generators': {
            'GEN': [
                ['name',    'bus',  'S_n',  'V_n',  'P',    'V',        'H',        'D',    'X_d',  'X_q',  'X_d_t',    'X_q_t',    'X_d_st',   'X_q_st',   'T_d0_t',   'T_q0_t',   'T_d0_st',  'T_q0_st'],
                ['G1',      'B1',   2200,   24,     1998,   1,      3.5,    0,      1.81,   1.76,   0.3,        0.65,       0.23,        0.23,      8.0,        1,          0.03,       0.07],
                ['IB',      'B3',   2200*100, 24,    -1998,  0.995,  3.5e7,  0,      1.8,    1.8,    0.3,        0.65,       0.23,        0.23,      8,          1,          0.03,       0.07],
            ],
        }
    }
