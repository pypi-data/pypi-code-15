#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetCdbInitInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdb', 'qcloudcliV1', 'GetCdbInitInfo', 'cdb.api.qcloud.com')

	def get_jobId(self):
		return self.get_params().get('jobId')

	def set_jobId(self, jobId):
		self.add_param('jobId', jobId)

