# -*- coding: UTF-8 -*-
from plc800stg.measure_events import PlcMeasureEventsParser
from plc800stg.utils import assert_list_dict_eq
from ast import literal_eval

with description('Parse meter events from PLC800 with plc800stg'):
    with it('Parsing events'):
        input_events_plc = open('spec/data/09EVMarmol2003140245.txt').read()
        meter_events = PlcMeasureEventsParser(input_events_plc, "Marmol")
        expected_result = literal_eval(open('spec/data/09EVMarmol2003140245_result.txt').read())
        assert_list_dict_eq(expected_result, meter_events.events, 'name')
