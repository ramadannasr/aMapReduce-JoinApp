#!/usr/bin/env python
import sys
import string

def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)

def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string

def _key_changed(key_of_previous_line, key_of_current_line):
    return not (key_of_previous_line) or (key_of_previous_line != key_of_current_line)

def reducer():
	last_user_id = None
	cur_location = "-"

	for line in sys.stdin:
		line_elements = _format_and_split(line)
		if len(line_elements) != 3:
			continue
		user_id,product_id,location = line_elements
		
		if _key_changed(last_user_id, user_id):
			last_user_id = user_id
			cur_location = location
		elif user_id == last_user_id:
			location = cur_location
			_emit([product_id,location])

if __name__ == '__main__':
    reducer()