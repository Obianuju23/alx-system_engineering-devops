#!/usr/bin/env ruby
"""
This is a Ruby Script using regular expression to match only capital letters
"""

puts ARGV[0].scan(/[A-Z]/).join
