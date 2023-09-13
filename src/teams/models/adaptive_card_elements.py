# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
class factSet:
    def __init__(self, facts):
        self.type = 'FactSet'
        self.height = 'stretch'
        self.facts = facts
        
class fact:
    def __init__(self, title, value):
        self.title = title
        self.value = value
        
class textBlock:
    def __init__(self, text, separator, weight):
        self.text = text
        self.separator = separator
        self.type = 'TextBlock'
        self.size = 'Medium'
        self.weight = 'Bolder'