#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
作者:             zy

创建时间：         2018/11/6 下午4:42

文件:             debugtalk.py
"""
import pdb
default_request = {
    "base_url": "http://preview.airwallex.com:30001",
    "headers": {
        "Content-Type": "application/json"
    }
}


# 删除mandatory parameter
def pop_parameter(in_request,r_p):
    if r_p == '':
        pass
    else:
        in_request['json'].pop(r_p)

# string to int
def str2int(in_str):

    return int(in_str)

# string to eval(string)
def eval_str(in_str):

    return eval(in_str)

#
def format_content(payment_method,in_parameter,bank_country_code=''):

    if in_parameter == 'status_code':
        if payment_method == 'LOCAL':
            if bank_country_code == 'US':
                result_content = 400
            elif bank_country_code == 'AU':
                result_content = 400
            else:
                result_content = 200
        if payment_method == 'SWIFT':
            result_content = 400
    if in_parameter == 'content':
        if payment_method == 'LOCAL':
            if bank_country_code == 'US':
                result_content = {"error": "'aba' is required when bank country code is 'US'"}
            elif bank_country_code == 'AU':
                result_content = {"error": "'bsb' is required when bank country code is 'AU'"}
            else:
                result_content = {"success": "Bank details saved"}
        if payment_method == 'SWIFT':
            result_content = {"error": "'swift_code' is required when payment method is 'SWIFT'"}

    return result_content

def format_swift_code(bank_country_code,length,y = ''):
    swift_code = '1111111111111111'[:length]
    if y == 1:
        swift_code = swift_code[:4] + bank_country_code + swift_code[6:]

    return swift_code

def format_error_message(bank_country_code):
    error_message = "The swift code is not valid for the given bank country code: " + bank_country_code

    return error_message

def format_swift_code_response(bank_country_code,in_type):
    if in_type == 'status_code':
        if bank_country_code == "CN":
            result = 200
        else:
            result = 400
    if in_type == 'content':
        if bank_country_code == "US":
            result = {"error": "'aba' is required when bank country code is 'US'"}
        if bank_country_code == "AU":
            result = {"error": "'bsb' is required when bank country code is 'AU'"}
        else:
            result = {'success': 'Bank details saved'}

    return result