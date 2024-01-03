#!/usr/bin/env ruby
# The regular expression must be exactly matching to "hbtn, hbttn, hbtttn, hbttttn"
puts ARGV[0].scan(/hbt{1,3}n/).join
