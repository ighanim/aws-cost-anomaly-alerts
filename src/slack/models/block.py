# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
class Block:
	##def __init__(self, type,  text=None, fields=None):
	def __init__(self, type, **kwargs):
		##type: section
		self.type = type
		##fields: an array of fields in the section
		if kwargs.get("fields"):
			self.fields = kwargs.get("fields")
		if kwargs.get("text"):
			self.text = kwargs.get("text")
