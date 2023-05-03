#!/usr/bin/env ruby
"""
This is a Ruby script that accepts one argument and pass it to a regular expression matching method which uses regexp to match a string that starts with h ends with n and can have any single character in between Using the project instructions.
"""

puts ARGV[0].scan(/h[A-Za-z0-9]n/).join
