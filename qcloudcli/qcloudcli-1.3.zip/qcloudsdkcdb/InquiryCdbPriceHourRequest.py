#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class InquiryCdbPriceHourRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdb', 'qcloudcliV1', 'InquiryCdbPriceHour', 'cdb.api.qcloud.com')

	def get_cdbType(self):
		return self.get_params().get('cdbType')

	def set_cdbType(self, cdbType):
		self.add_param('cdbType', cdbType)

	def get_goodsNum(self):
		return self.get_params().get('goodsNum')

	def set_goodsNum(self, goodsNum):
		self.add_param('goodsNum', goodsNum)

	def get_memory(self):
		return self.get_params().get('memory')

	def set_memory(self, memory):
		self.add_param('memory', memory)

	def get_volume(self):
		return self.get_params().get('volume')

	def set_volume(self, volume):
		self.add_param('volume', volume)

	def get_zoneId(self):
		return self.get_params().get('zoneId')

	def set_zoneId(self, zoneId):
		self.add_param('zoneId', zoneId)

