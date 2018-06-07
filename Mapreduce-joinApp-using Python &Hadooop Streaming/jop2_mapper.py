#!/usr/bin/env python
import sys
import string

def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)

def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string

def mapper():
	for line in sys.stdin:
		line_elements = _format_and_split(line)
		product_id,location = line_elements
		_emit([product_id,location])

if __name__ == '__main__':
    mapper()
