# Get args
my $Path = $ARGV[0];

# Check if the path exists
if (-d $Path) {
    print("The directory$Path does exist");
} else {
    die "The directory$Path does NOT exist";
}

# Open the file
open(my $file, '>', $Path) or die "Could not open file: $!";

# Loop over the lines in the file
while (my $line = <$file>) {
    chomp $line; # Remove the newline character at the end of each line

    # Iterate over the characters in the line
    # column 89 Is the start of the function names
    for (my $i = 89; $i < length($line); $i++) {
        my $char = substr($line, $i, 1);

        if ($char eq ' ') {
            last;
        }

        open(my $fh, '>', "parsed/pat_items_name.txt") or die "Can not open file: $!";
        print($fh $line);
        close(my $fh);        
    }
}

# Close the file
close(my $file) or die "Could not close: $!";