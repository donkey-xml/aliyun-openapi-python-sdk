# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeInstances')

	def get_DeviceAvailable(self):
		return self.get_query_params().get('DeviceAvailable')

	def set_DeviceAvailable(self,DeviceAvailable):
		self.add_query_param('DeviceAvailable',DeviceAvailable)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PublicIpAddresses(self):
		return self.get_query_params().get('PublicIpAddresses')

	def set_PublicIpAddresses(self,PublicIpAddresses):
		self.add_query_param('PublicIpAddresses',PublicIpAddresses)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_Filter4Value(self):
		return self.get_query_params().get('Filter.4.Value')

	def set_Filter4Value(self,Filter4Value):
		self.add_query_param('Filter.4.Value',Filter4Value)

	def get_Filter2Key(self):
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self,Filter2Key):
		self.add_query_param('Filter.2.Key',Filter2Key)

	def get_Filter3Value(self):
		return self.get_query_params().get('Filter.3.Value')

	def set_Filter3Value(self,Filter3Value):
		self.add_query_param('Filter.3.Value',Filter3Value)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_InstanceTypeFamily(self):
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self,InstanceTypeFamily):
		self.add_query_param('InstanceTypeFamily',InstanceTypeFamily)

	def get_Tag5Value(self):
		return self.get_query_params().get('Tag.5.Value')

	def set_Tag5Value(self,Tag5Value):
		self.add_query_param('Tag.5.Value',Tag5Value)

	def get_Tag3Key(self):
		return self.get_query_params().get('Tag.3.Key')

	def set_Tag3Key(self,Tag3Key):
		self.add_query_param('Tag.3.Key',Tag3Key)

	def get_Filter2Value(self):
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self,Filter2Value):
		self.add_query_param('Filter.2.Value',Filter2Value)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Filter1Value(self):
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self,Filter1Value):
		self.add_query_param('Filter.1.Value',Filter1Value)

	def get_Tag1Key(self):
		return self.get_query_params().get('Tag.1.Key')

	def set_Tag1Key(self,Tag1Key):
		self.add_query_param('Tag.1.Key',Tag1Key)

	def get_Tag1Value(self):
		return self.get_query_params().get('Tag.1.Value')

	def set_Tag1Value(self,Tag1Value):
		self.add_query_param('Tag.1.Value',Tag1Value)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Tag4Value(self):
		return self.get_query_params().get('Tag.4.Value')

	def set_Tag4Value(self,Tag4Value):
		self.add_query_param('Tag.4.Value',Tag4Value)

	def get_PrivateIpAddresses(self):
		return self.get_query_params().get('PrivateIpAddresses')

	def set_PrivateIpAddresses(self,PrivateIpAddresses):
		self.add_query_param('PrivateIpAddresses',PrivateIpAddresses)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_InnerIpAddresses(self):
		return self.get_query_params().get('InnerIpAddresses')

	def set_InnerIpAddresses(self,InnerIpAddresses):
		self.add_query_param('InnerIpAddresses',InnerIpAddresses)

	def get_Filter3Key(self):
		return self.get_query_params().get('Filter.3.Key')

	def set_Filter3Key(self,Filter3Key):
		self.add_query_param('Filter.3.Key',Filter3Key)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_InstanceIds(self):
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self,InstanceIds):
		self.add_query_param('InstanceIds',InstanceIds)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Tag5Key(self):
		return self.get_query_params().get('Tag.5.Key')

	def set_Tag5Key(self,Tag5Key):
		self.add_query_param('Tag.5.Key',Tag5Key)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_LockReason(self):
		return self.get_query_params().get('LockReason')

	def set_LockReason(self,LockReason):
		self.add_query_param('LockReason',LockReason)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_Tag2Key(self):
		return self.get_query_params().get('Tag.2.Key')

	def set_Tag2Key(self,Tag2Key):
		self.add_query_param('Tag.2.Key',Tag2Key)

	def get_Filter1Key(self):
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self,Filter1Key):
		self.add_query_param('Filter.1.Key',Filter1Key)

	def get_Filter4Key(self):
		return self.get_query_params().get('Filter.4.Key')

	def set_Filter4Key(self,Filter4Key):
		self.add_query_param('Filter.4.Key',Filter4Key)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_Tag3Value(self):
		return self.get_query_params().get('Tag.3.Value')

	def set_Tag3Value(self,Tag3Value):
		self.add_query_param('Tag.3.Value',Tag3Value)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_Tag2Value(self):
		return self.get_query_params().get('Tag.2.Value')

	def set_Tag2Value(self,Tag2Value):
		self.add_query_param('Tag.2.Value',Tag2Value)

	def get_Tag4Key(self):
		return self.get_query_params().get('Tag.4.Key')

	def set_Tag4Key(self,Tag4Key):
		self.add_query_param('Tag.4.Key',Tag4Key)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)