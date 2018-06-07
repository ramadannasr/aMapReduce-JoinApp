#!/usr/bin/env python
import sys

def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)

def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print output_string

def _key_changed(key_of_previous_line, key_of_current_line):
    return not (key_of_previous_line) or (key_of_previous_line != key_of_current_line)

def reducer():
    last_product_id = None
    cur_location = ""
    count_locations=0

    for line in sys.stdin:
        line_elements = _format_and_split(line)
        if len(line_elements) != 2:
            continue
        product_id, location = line_elements

        if _key_changed(last_product_id, product_id):
            if last_product_id == None:
                last_product_id = product_id
                cur_location = location
                count_locations = 1
            else:
                _emit([last_product_id, count_locations])
                last_product_id = product_id
                cur_location = location
                count_locations = 1
            
        elif product_id == last_product_id:
            if location != cur_location:
                count_locations += 1
                cur_location = location

    _emit([last_product_id, count_locations])

if __name__ == '__main__':
    reducer()