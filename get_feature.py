# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:52:31 2016

@author: Administrator
"""

import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import time as ti
import datetime as dt

#此函数用于浏览数据的大致情况
def glance_at_data(offline_train_data,offline_test_data):

#    #offline_train_data
#    print '==========================='
#    print 'offline_train_data describe'
#    print '==========================='
#    print offline_train_data.describe()
#
#
#    print '==========================='
#    print 'offline_train_data dtypes'
#    print '==========================='
#    print offline_train_data.dtypes
#
#
#    print '==========================='
#    print 'offline_train_data info'
#    print '==========================='
#    print offline_train_data.info()

    train_User_ids = pd.unique(offline_train_data['User_id'])
    train_Merchant_ids = pd.unique(offline_train_data['Merchant_id'])
    train_Coupon_ids = pd.unique(offline_train_data['Coupon_id'])
    train_User_ids_cnt = len(train_User_ids)
    train_User_Merchant_ids = len(train_Merchant_ids)
    train_User_Coupon_ids = len(train_Coupon_ids)
    print '==========================='
    print 'offline_train_data user,merchant,coupon num'
    print '==========================='
    print 'train_User_ids_cnt:' + str(train_User_ids_cnt)
    print 'train_User_Merchant_ids:' + str(train_User_Merchant_ids)
    print 'train_User_Coupon_ids:' + str(train_User_Coupon_ids)

#    #offline_test_data
#    print '==========================='
#    print 'offline_test_data describe'
#    print '==========================='
#    print offline_test_data.describe()
#
#
#    print '==========================='
#    print 'offline_test_data dtypes'
#    print '==========================='
#    print offline_test_data.dtypes
#
#
#    print '==========================='
#    print 'offline_test_data info'
#    print '==========================='
#    print offline_test_data.info()

    test_User_ids = pd.unique(offline_test_data['User_id'])
    test_Merchant_ids = pd.unique(offline_test_data['Merchant_id'])
    test_Coupon_ids = pd.unique(offline_test_data['Coupon_id'])
    test_User_ids_cnt = len(test_User_ids)
    test_User_Merchant_ids = len(test_Merchant_ids)
    test_User_Coupon_ids = len(test_Coupon_ids)
    print '==========================='
    print 'offline_train_data user,merchant,coupon num'
    print '==========================='
    print 'test_User_ids_cnt:' + str(test_User_ids_cnt)
    print 'test_User_Merchant_ids:' + str(test_User_Merchant_ids)
    print 'test_User_Coupon_ids:' + str(test_User_Coupon_ids)

    print '================================='
    #观察这训练集和测试集之间的交集
    print 'User intersection:' + str(len(set(test_User_ids) & set(train_User_ids)))
    print 'Merchant intersection:' + str(len(set(train_Merchant_ids) & set(test_Merchant_ids)))
    print 'Coupon intersection:' + str(len(set(train_Coupon_ids) & set(test_Coupon_ids)))

    return


#切分数据将数据分为训练集合测试集
def split_train_data(offline_train_data,offline_test_data):
    offline_test_data_size = len(offline_test_data)
    offline_train_data1 = offline_train_data[:-offline_test_data_size]
    offline_train_data2 = offline_train_data[-offline_test_data_size:]

    return (offline_train_data1 , offline_train_data2)

#对于数据进行一些需要的操作 产生正负样本
def process_data(data):
    #设定null 时间为 20010101
    null_time = pd.to_datetime('20000101',format = '%Y%m%d')
    #获得正负样本
    #负样本 领取优惠劵但没有使用
    received_but_not_used = (data['Date'] == null_time) & (data['Coupon_id']!= 'null')
    #print(len(received_but_not_used[received_but_not_used==True]))
    received_and_used_but_expired = (data['Date'] != null_time) & (data['Coupon_id']!= 'null')\
                                    & ((data['Date'] - data['Date_received']) >= dt.timedelta(days = 15))
    #print(len(received_and_used_but_expired[received_and_used_but_expired==True]))
    negtive_samples = data[received_but_not_used|received_and_used_but_expired]


    #正样本 领取额优惠券并且使用
    received_and_used_not_expired = (data['Date'] != null_time) & (data['Date_received'] != null_time)\
                                    & (data['Coupon_id']!= 'null')\
                                    & ((data['Date'] - data['Date_received']) < dt.timedelta(days = 15))
    positive_samples = data[received_and_used_not_expired]
    return (negtive_samples,positive_samples)

#简单的观察一下数据
#glance_at_data(offline_train_data,offline_test_data)
#将数据划分为训练结和测试集
(offline_train_data1 , offline_train_data2) = split_train_data( offline_train_data , offline_test_data )
(negtive_samples,positive_samples) = process_data(offline_train_data1)
