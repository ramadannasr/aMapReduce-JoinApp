#!/usr/bin/env python

import sys

def _format_and_split(line, separator='\t'):
	return line.strip().split(separator)

def _emit(elements, separator='\t'):
	elements_as_string = map(str, elements)
	output_string = separator.join(elements_as_string)
	print output_string

def mapper():
	for line in sys.stdin:
		user_id = ""
		product_id = "-"
		location = "-"

		line_elements = _format_and_split(line)
		if len(line_elements) == 5:
			user_id = line_elements[2]
			product_id = line_elements[1]
			
		elif len(line_elements) == 4:
			user_id = line_elements[0]
			location = line_elements[3]

		else:
			continue

		_emit([user_id, product_id, location])

if __name__ == '__main__':
	mapper()