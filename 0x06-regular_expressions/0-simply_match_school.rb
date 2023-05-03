#!/usr/bin/env ruby
"""
This is a Ruby regexp that must match School,accepts one argument and pass it to a regular expression matching method
"""

puts ARGV[0].scan(/School/).join
