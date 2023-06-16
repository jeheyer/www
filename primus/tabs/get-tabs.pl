#!/usr/bin/perl

$root = "http://www.ram.org/music/primus/tabs";
`fetch $root/primus_tabs.html`;

open(LIST, "primus_tabs.html"); 
while (defined($line = <LIST>)) {
	if ($line =~ "h3") {
		($a,$album,$b) = split(/ /,$line,3);
		`mkdir $album`;
	}
	if ($line =~ "<li>" && $line !~ "#") {
		($a,$song,$b) = split(/"/,$line);
		if (!(-e "$album/$song")) { 
			`lynx -source $root/$song > $album/$song`;
		}
	}
}
close(LIST);

`zip -r tabs *`;
