# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:36:59 2016

@author: Administrator
"""

import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import time as ti
import datetime as dt

def parse_offline_test_data():
    columns = ['User_id', 'Merchant_id' , 'Coupon_id' , 'Discount_rate' , 'Distance' , 'Date_received']
    offline_test_data = pd.read_csv('../data/ccf_offline_stage1_test_revised.csv', header = None)
    offline_test_data.columns = columns
    offline_test_data['Date_received'] = pd.to_datetime(offline_test_data['Date_received'],format = '%Y%m%d')
    return offline_test_data

def parse_offline_train_data():
    columns = ['User_id', 'Merchant_id' , 'Coupon_id' , 'Discount_rate' , 'Distance' , 'Date_received' , 'Date']
    offline_train_data = pd.read_csv('../data/ccf_offline_stage1_train.csv',header = None)
    offline_train_data.columns = columns

    offline_train_data.loc[offline_train_data['Date'] == 'null','Date'] = '20000101'
    offline_train_data.loc[offline_train_data['Coupon_id'] == 'null','Date_received'] = '20000101'

    offline_train_data['Date'] = pd.to_datetime(offline_train_data['Date'],format = '%Y%m%d')
    offline_train_data['Date_received'] = pd.to_datetime(offline_train_data['Date_received'],format = '%Y%m%d')

    return offline_train_data


def parse_online_train_data():
    columns = ['User_id', 'Merchant_id' , 'Action' , 'Coupon_id' , 'Discount_rate' , 'Date_received' , 'Date']
    online_train_data = pd.read_csv('../data/ccf_online_stage1_train.csv',header = None)
    online_train_data.columns = columns


    online_train_data[online_train_data.loc['Date'] == 'null','Date'] = '20000101'
    online_train_data[online_train_data.loc['Date_received'] == 'null','Date_received'] = '20000101'

    online_train_data['Date'] = pd.to_datetime(online_train_data['Date'],format = '%Y%m%d')
    online_train_data['Date_received'] = pd.to_datetime(online_train_data['Date_received'],format = '%Y%m%d')

    return online_train_data


#读入数据
print 'reading data'
offline_test_data = parse_offline_test_data()
offline_train_data = parse_offline_train_data()
#online_train_data = parse_online_train_data()
print len(offline_test_data)
print len(offline_train_data)
print 'reading data   done'
