# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
class Field:
	def __init__(self,  type, text, emoji):
		##type: plain_text
		self.type = type
		#text: text to be displayed
		self.text = text
		#emoji: boolean
		self.emoji = emoji