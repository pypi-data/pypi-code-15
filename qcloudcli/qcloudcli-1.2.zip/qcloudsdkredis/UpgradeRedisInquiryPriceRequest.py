#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpgradeRedisInquiryPriceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'redis', 'qcloudcliV1', 'UpgradeRedisInquiryPrice', 'redis.api.qcloud.com')

	def get_redisId(self):
		return self.get_params().get('redisId')

	def set_redisId(self, redisId):
		self.add_param('redisId', redisId)

	def get_memSize(self):
		return self.get_params().get('memSize')

	def set_memSize(self, memSize):
		self.add_param('memSize', memSize)

