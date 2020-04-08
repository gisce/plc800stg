# -*- coding: UTF-8 -*-
from plc800stg.billings import PlcMonthlyBillingsParser, PlcDailyBillingsParser
from plc800stg.utils import assert_list_dict_eq
from ast import literal_eval

with description('Parse billings from PLC800 with plc800stg'):
    with it('Parsing monthly billings'):
        input_billing_plc = open('spec/data/02BIBascul200201.txt').read()
        billings = PlcMonthlyBillingsParser(input_billing_plc, "Bascul")
        expected_result = literal_eval(open('spec/data/02BIBascul200201_result.txt').read())
        assert_list_dict_eq(expected_result, billings.billings, 'name')

    with it('Parsing daily billings'):
        input_billing_plc = open('spec/data/02DIBascul200304.txt').read()
        billings = PlcDailyBillingsParser(input_billing_plc, "Bascul")
        expected_result = literal_eval(open('spec/data/02DIBascul200304_result.txt').read())
        assert_list_dict_eq(expected_result, billings.billings, 'name')
