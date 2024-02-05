# Synchronous machine connected to infinite bus

def load():
    return {
        'base_mva': 50,
        'f': 50,
        'slack_bus': 'B3',

        'buses': [
            ['name',    'V_n'],
            ['B1',       10],
            ['B2',      245],
            ['B3',      245],
        ],

        'lines': [
            ['name',    'from_bus', 'to_bus',   'length',   'S_n',  'V_n',  'unit', 'R',    'X',      'B'],
            ['L2-3',    'B2',       'B3',       250,         50,    245,     'PF',   0,   0.4,     0],
        ],

        'transformers': [
            ['name', 'from_bus', 'to_bus', 'S_n', 'V_n_from', 'V_n_to', 'R', 'X'],
            ['T1',      'B1',     'B2',     50,     10,         245,     0,   0.1],
        ],

        'loads': [
            ['name', 'bus', 'P', 'Q', 'model'],
            ['L1', 'B2', 25, 0, 'Z'],
        ],

        'generators': {
            'GEN': [
                ['name',    'bus',  'S_n',  'V_n',  'P',    'V',        'H',        'D',    'X_d',  'X_q',  'X_d_t',   'X_q_t',    'X_d_st',   'X_q_st',   'T_d0_t',   'T_q0_t',   'T_d0_st',  'T_q0_st'],
                ['G1',      'B1',   50,       10,    40,    0.93,       6.5,         0,     1.05,   0.66,    0.3,      0.66,      0.23,       0.23,        8.0,        1,          0.03,       0.07],
                ['IB',      'B3',   1e10,    245,   0,  0.898,       3.5e7,         0,      1.8,    1.8,    0.3,      0.65,      0.23,       0.23,        8.0,        1,          0.03,       0.07],
            ],
        }
    }