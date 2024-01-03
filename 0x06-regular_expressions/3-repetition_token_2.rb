#!/usr/bin/env ruby
# The regular expression must be exactly matching to "hbtn, hbttn, hbtttn, hbttttn"
puts ARGV[0].scan(/hbt{2,5}n/).join
