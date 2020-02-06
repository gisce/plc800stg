# -*- coding: UTF-8 -*-
from plc800stg.profiles import PlcProfilesParser
from plc800stg.utils import assert_list_dict_eq

with description('Parse profiles from PLC800 with plc800stg'):
    with it('Parsing profiles'):
        input_profiles_plc = "141002118;30/11/2019 02:00:00;0;00001825.0;00000000.0;00001266.0;" \
                             "00000000.0;00000000.0;00000144.0"
        profiles = PlcProfilesParser(input_profiles_plc, "Bascul")
        expected_result = [{'ae': 0,
                            'ai': 1825,
                            'cnc_name': 'Bascul',
                            'magn': 1000,
                            'name': '141002118',
                            'r1': 1266,
                            'r2': 0,
                            'r3': 0,
                            'r4': 144,
                            'season': 'W',
                            'timestamp': '2019-11-30 02:00:00'}]
        assert_list_dict_eq(expected_result, profiles.profiles, 'name')
