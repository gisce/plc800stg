# -*- coding: UTF-8 -*-
from plc800stg.measure_events import PlcMeasureEventsParser
from plc800stg.utils import assert_list_dict_eq

with description('Parse meter events from PLC800 with plc800stg'):
    with it('Parsing profiles'):
        input_events_plc = "141004375;01/11/2019 00:11:53;14;Sincronitzation event"
        meter_events = PlcMeasureEventsParser(input_events_plc, "Bascul")
        expected_result = [{'active': True,
                            'cnc_name': 'Bascul',
                            'event_code': 98,
                            'event_code_desc': 'Sincronitzation event',
                            'event_group': 1,
                            'name': '141004375',
                            'season': 'W',
                            'timestamp': '2019-11-01 00:11:53',
                            'type': 'M'}]
        assert_list_dict_eq(expected_result, meter_events.events, 'name')
