#!/usr/bin/perl 
use strict;
use warnings;

use Scalar::Util qw(looks_like_number);

my $N = 200;

my $debug;
my $moving;
my $scores = 'scores.txt';
my ($min, $max);
if (open my $in, '<', $scores) {
    ($min, $max) = <$in>;
    chomp ($min, $max);
}
help();

GAME:
while (1) {
    my $hidden = 1 + int rand $N;
    my $count = 0;
    while (1) {
        print "Please guess between 1 and $N :";
        if ($debug) {
            print " ($hidden) ";
        }
        print "\n";
        my $guess = <STDIN>;
        chomp $guess;
        if ($guess eq '') {
            print "Need some input";
			help();
			next;
        }
        $count++;
        if ($guess eq 'x' or $guess eq 'q') {
            last GAME;
        }
        if ($guess eq 'n') {
            last;
        }
        if ($guess eq 'd') {
            $debug = not $debug;;
            next;
        }
        if ($guess eq 'm') {
            $moving = not $moving;
            next;
        }
        if ($guess eq 'h') {
			help();
            next;
        }
        if ($guess eq "s") {
            print "The hidden value is $hidden\n";
            next;
            # is it fair to let the player keep playing after seeing the result?
            # if not replace the next by last
        }
        if (not looks_like_number($guess)) {
			print "Invalid input ($guess)\n";
			help();
			next;
        }
        if ($guess < 1 or $guess > $N) {
            warn "You shot ($guess) in the outer space.\n";
        }
        if ($guess < $hidden) {
            print "$guess is too small\n";
        }
        if ($guess > $hidden) {
            print "$guess is too big\n";
        }
        if ($guess == $hidden) {
            print "Heureka!\n";
            last;
        }
        if ($moving) {
            $hidden += int(rand 5)-2;
            # move target by -2 .. +2

            # don't wander off the space
            if ($hidden > $N) {
                $hidden = $N;
            }
            if ($hidden < 1) {
                $hidden = 1;
            }
        }
    }
    if (not defined $min) {
        $min = $count;
        $max = $count;
    }
    $min = $count < $min ? $count : $min;
    $max = $count > $max ? $count : $max;
}

if (defined $min) {
    open my $out, '>', $scores or die;
    print $out "$min\n";
    print $out "$max\n";
}

sub help {
    print q{
x - exit
q - quit
h - help
n - next game
s - show target
d - toggle debug mode
m - toggle - allow object to move or not
};
}
