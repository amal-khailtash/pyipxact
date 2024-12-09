eval '(exit $?0)' && eval 'exec perl -S $0 ${1+"$@"}' # -*-perl-*-
& eval 'exec perl -S $0 $argv:q'
if 0;

use strict;

if ($#ARGV == -1) { 
  die "No argument \n";
 }
open(INFILE, $ARGV[0]) || die "Can't open $ARGV[0] ...\n";
open(OUTFILE, ">$ARGV[1]") || die "Can't open $ARGV[1] ...\n";

while (<INFILE>) {
  s/http:\/\/www.spiritconsortium.org\/XMLSchema\/SPIRIT\/1.[24]/http:\/\/www.spiritconsortium.org\/XMLSchema\/SPIRIT\/1.5/g;
 print OUTFILE $_;


}

close(INFILE);
close(OUTFILE);

