# -*- coding: UTF-8 -*-
from plc800stg.profiles import PlcProfilesParser
from plc800stg.utils import assert_list_dict_eq
from ast import literal_eval

with description('Parse profiles from PLC800 with plc800stg'):
    with it('Parsing profiles'):
        input_profiles_plc = open('spec/data/02CHBascul2002110245.txt').read()
        profiles = PlcProfilesParser(input_profiles_plc, "Bascul")
        expected_result = literal_eval(open('spec/data/02CHBascul2002110245_result.txt').read())
        assert_list_dict_eq(expected_result, profiles.profiles, 'name')
