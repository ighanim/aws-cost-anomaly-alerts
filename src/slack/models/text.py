# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
class Text:
	#def __init__(self, type, text, emoji):
	def __init__(self, type, text, **kwargs):
		##type: plain_text
		self.type = type
		#text: text to be displayed
		self.text = text
		#emoji: boolean
		if kwargs.get("emoji"):
			self.emoji = kwargs.get("emoji")
