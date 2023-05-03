#!/usr/bin/env ruby
"""
This is a Ruby Script using regexp to match cases as shown in the example that accepts one argument and pass it to a regular expression matching method
"""

puts ARGV[0].scan(/hbt*n/).join
