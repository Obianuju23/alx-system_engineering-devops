#!/usr/bin/env ruby
"""
This Ruby Script uses The regular expression to match a 10 digit phone number
"""

puts ARGV[0].scan(/^[0-9]{10}$/).join  
