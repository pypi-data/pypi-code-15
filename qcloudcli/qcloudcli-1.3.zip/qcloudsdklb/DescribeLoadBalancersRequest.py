#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeLoadBalancersRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'DescribeLoadBalancers', 'lb.api.qcloud.com')

	def get_loadBalancerIds(self):
		return self.get_params().get('loadBalancerIds')

	def set_loadBalancerIds(self, loadBalancerIds):
		self.add_param('loadBalancerIds', loadBalancerIds)

	def get_loadBalancerType(self):
		return self.get_params().get('loadBalancerType')

	def set_loadBalancerType(self, loadBalancerType):
		self.add_param('loadBalancerType', loadBalancerType)

	def get_loadBalancerName(self):
		return self.get_params().get('loadBalancerName')

	def set_loadBalancerName(self, loadBalancerName):
		self.add_param('loadBalancerName', loadBalancerName)

	def get_domain(self):
		return self.get_params().get('domain')

	def set_domain(self, domain):
		self.add_param('domain', domain)

	def get_loadBalancerVips(self):
		return self.get_params().get('loadBalancerVips')

	def set_loadBalancerVips(self, loadBalancerVips):
		self.add_param('loadBalancerVips', loadBalancerVips)

	def get_backendWanIps(self):
		return self.get_params().get('backendWanIps')

	def set_backendWanIps(self, backendWanIps):
		self.add_param('backendWanIps', backendWanIps)

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)

	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)

	def get_searchKey(self):
		return self.get_params().get('searchKey')

	def set_searchKey(self, searchKey):
		self.add_param('searchKey', searchKey)

	def get_orderBy(self):
		return self.get_params().get('orderBy')

	def set_orderBy(self, orderBy):
		self.add_param('orderBy', orderBy)

	def get_orderType(self):
		return self.get_params().get('orderType')

	def set_orderType(self, orderType):
		self.add_param('orderType', orderType)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

