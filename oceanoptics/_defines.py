
""" File:           defines.py
    Author:         Andreas Poehlmann

    Python Interface for OceanOptics Spectometer USB2000+
    Some definition stuff...
"""

#----------------------------------------------------------

class OceanOpticsError(Exception):
    pass

OceanOpticsVendorId = 0x2457

OceanOpticsModelConfig = {
    'USB2000'       : { 'ProductId' : [], # XXX: Couldn't find productid
                        'EPout' : 0x02,
                        'EPin0' : 0x87, 'EPin0_size' : 64,
                        'EPin1' : 0x07, 'EPin1_size' : 64, },
    'USB-LS450'     : { 'ProductId' : [], # XXX: Couldn't find productid
                        'EPout' : 0x02,
                        'EPin0' : 0x87, 'EPin0_size' : 64,
                        'EPin1' : 0x07, 'EPin1_size' : 64, },
    'USB-ISS-UVVIS' : { 'ProductId' : [], # XXX: Couldn't find productid
                        'EPout' : 0x02,
                        'EPin0' : 0x87, 'EPin0_size' : 64,
                        'EPin1' : 0x07, 'EPin1_size' : 64, },
    'HR2000'        : { 'ProductId' : [0x100A, 0x1009],
                        'EPout' : 0x02,
                        'EPin0' : 0x87, 'EPin0_size' : 64,
                        'EPin1' : 0x07, 'EPin1_size' : 64, },
    'NIR'           : { 'ProductId' : [0x1010, 0x100C],
                        'EPout' : 0x02,
                        'EPin0' : 0x87, 'EPin0_size' : 64,
                        'EPin1' : 0x07, 'EPin1_size' : 64, },
    'USB2000+'      : { 'ProductId' : [0x101E],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'Torus'         : { 'ProductId' : [0x1040],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'NIRQUEST'      : { 'ProductId' : [0x1026, 0x1028],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 512,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'USB4000'       : { 'ProductId' : [0x1022],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'HR2000+'       : { 'ProductId' : [0x1012],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'HR4000'        : { 'ProductId' : [0x1012, 0x1011],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'Apex'          : { 'ProductId' : [0x1044],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'Maya'          : { 'ProductId' : [0x102A],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'Maya2000pro'   : { 'ProductId' : [0x102A],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'QE65pro'       : { 'ProductId' : [0x1018],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'QE65000'       : { 'ProductId' : [0x1018],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    'Jaz'           : { 'ProductId' : [0x2000],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 512,
                        'EPin1' : 0x82, 'EPin1_size' : 512, },
    # This one has a slightly different interface, but I think we
    # can just communicate everything through EP 0x01 and 0x81,
    # so we can keep most of the abstraction layer intact
    'STS'           : { 'ProductId' : [0x4000],
                        'EPout' : 0x01,
                        'EPin0' : 0x81, 'EPin0_size' : 64,
                        'EPin1' : 0x81, 'EPin1_size' : 64, }, 
        }


OceanOpticsSpectrumConfig = {
    'QE65pro'       : { 0x80 : [  5, 512, lambda x : x^0x80 ],
                        0x00 : [ 40,  64, lambda x : x^0x80 ] },
    'QE65000'       : { 0x80 : [  5, 512, lambda x : x^0x80 ],
                        0x00 : [ 40,  64, lambda x : x^0x80 ] },
    'USB2000+'      : { 0x80 : [  8, 512, lambda x : x      ],
                        0x00 : [ 64,  64, lambda x : x      ] },
    'Torus'         : { 0x80 : [  8, 512, lambda x : x      ],
                        0x00 : [ 64,  64, lambda x : x      ] },
    'HR2000+'       : { 0x80 : [  8, 512, lambda x : x^0x20 ],
                        0x00 : [ 64,  64, lambda x : x^0x20 ] },
    'Apex'          : { 0x80 : [  9, 512, lambda x : x      ],
                        0x00 : [ 66,  64, lambda x : x      ] },
    'Maya'          : { 0x80 : [  9, 512, lambda x : x      ],
                        0x00 : [ 66,  64, lambda x : x      ] },
    'Maya2000pro'   : { 0x80 : [  9, 512, lambda x : x      ],
                        0x00 : [ 66,  64, lambda x : x      ] },
    'USB4000'       : { 0x80 : [ 15, 512, lambda x : x      ],
                        0x00 : [120,  64, lambda x : x      ] },
    'HR4000'        : { 0x80 : [ 15, 512, lambda x : x      ],
                        0x00 : [120,  64, lambda x : x      ] },
    }


OceanOpticsSupportedModels = OceanOpticsSpectrumConfig.keys() + ['STS']



