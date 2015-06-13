#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Externals
import io
import json

# Internals
import generator

__author__ = 'Lennart Grahl <lennart.grahl@gmail.com>'
__status__ = 'Prototype'
__version__ = '1.0.0'


# Get settings
with io.open('settings.json', mode='r', encoding='utf-8') as fd:
    settings = json.load(fd)

# Create random code generator
gen = generator.RandomCodeGenerator()

# Levels
gen.operator_level = '3'  # max: 3
gen.pointer_level = '2'  # max: 2
gen.function_level = '2'  # max: 2

# Booleans
gen.void = False
gen.float_ = True
gen.conditionals = True

# Print generated code
print(gen.code())