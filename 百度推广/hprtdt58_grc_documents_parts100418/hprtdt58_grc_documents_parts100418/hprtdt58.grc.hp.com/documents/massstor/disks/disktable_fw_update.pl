#! /usr/local/bin/perl
#
# (C) 09/2001 Stefan Stechemesser, HP, CRC Ratingen, Germany, MUHW
#
# reads current directory from firmware server cec825.atl.hp.com
# and automatically updates the disktable if new firmware is found on the server
#
$WORKDIR="/www/documents/massstor/disks";
$INFILE="disktable";
$LOGDIR="disktable.log";
$LOGFILE="$LOGDIR/disktable.fw.log";
$FIRMWAREFILE="$LOGDIR/firmware.new";
$OLDFWFILE="$LOGDIR/firmware.old";
$DATUM=`date "+%d.%m.%y %H:%M:%S"`;
chop $DATUM;
@FVzeile=("");
chdir($WORKDIR) || die "could not change to working dir $WORKDIR";
# create the input firmware file
if (-f $FIRMWAREFILE)
{
	system("cp $FIRMWAREFILE $OLDFWFILE");
}
else
{
	system("echo first entry > $OLDFWFILE");
}
print ` ( sleep 3;echo "dteam"; sleep 2; echo "disk"; sleep 5; echo "echo;find . -name \"*.frm\" -print | grep -v old"; sleep 3; echo "exit";) | telnet cec825.atl.hp.com | grep "./" > $FIRMWAREFILE`;
# Check if new Firmware File differs from old
system("cmp $FIRMWAREFILE $OLDFWFILE");
$ret=($?>>8);
# open the logfile
open(LOGFL,">>$LOGFILE") || die "Could not open logfile $LOGFILE";
if($ret == 0) # Files are identical
{
   print LOGFL "$DATUM: No changes on firmware server\n";
   print "$DATUM: No changes on firmware server\n";
}
else
{
   print LOGFL "*******************************************************************************\n";
   print LOGFL "Firmware Update Check on $DATUM\n";
   print "*******************************************************************************\n";
   print "Firmware Update Check on $DATUM\n";
# There has something changed on the cec825 server
#first, we make a copy of the old disktable
$OLDFN="$LOGDIR/$INFILE".substr($DATUM,0,8);
# Sicherheitskopie des alten Files anlegen
print `cp $INFILE  $OLDFN`; 
$changedjn=0; # wurde was geaendert ?
# read new firmware file into memory
open(FV,"<$FIRMWAREFILE") || die "File not found";
while(<FV>)
{
        crop  ;
	push(@FVzeile,$_);
}
close(FV);
# open current disk table
open(DB,"<$OLDFN") || die "could not open backup file $OLDFN for reading - Abort";
open(OUT,">$INFILE") || die "could not open output file $INFILE for reading - Abort";
# skip the first line, but save it for later use
	$firstline = $_ = <DB>;
	print OUT $firstline;
while ( <DB>) # loop over all entries in the disk table
{
   $line = $_;
   chop $line;
   @RECORD = split("::",$line);
   $inq=@RECORD[1]; # Inquiery String
   if($inq ne '') 
   {
      #search in  firmware file
      $currFV=0;
      $newestfv=""; # newest firmware in firmware input file
      for(@FVzeile)
      {
	  $i=index($_,$inq);
	  $l=length($inq)+1;
	  if($i>0)
	  {
	       $newfv=substr($_,$i+$l);
	       chop $newfv;
               $newfv =~ s/.frm//;
	       $newfv_value = $newfv;
	       $newfv_value =~ s/[a-z]|[A-Z]//g; # only numbers
	       if($newfv_value > $currFV) # higher Firmware version
	       {
		   $currFV=$newfv_value;
		   $newestfv=$newfv;
	       }
	  }
      }
      if($newestfv eq '') { $newestfv="N/A" ;}
      # Check if the firmware in table is older than the firmware on cec825
      $newfv = $newestfv;
      $newfv =~ s/[a-z]|[A-Z]//g; # only numbers
      $oldfv = @RECORD[6]; 
      $oldfv =~ s/[a-z]|[A-Z]//g; # only numbers
      if($newfv > $oldfv)    
      {
	print LOGFL "New Firmware: Record ",@RECORD[0],",",$inq," old:" ,@RECORD[6]," new:",$newestfv,"\n";
	print "New Firmware: Record ",@RECORD[0],",",$inq," old:" ,@RECORD[6]," new:",$newestfv,"\n";
	# Save changed Firmware
	@RECORD[6]=$newestfv;
	$changedjn=1;
      }
   }
   $content = join("::",@RECORD);
   print OUT $content,"\n";
}
close DB;
close OUT;
#remove backup file if no changes were made
if($changedjn==1)
{
   system("/usr/contrib/bin/gzip -9 $OLDFN");
   print LOGFL "backup file generated: ",$OLDFN,".gz";
   print "backup file generated: ",$OLDFN,".gz";
}
else
{
   system("rm $OLDFN");
   print LOGFL "No new firmware found. Temporary backupfile removed.\n"; 
   print "No new firmware found. Temporary backupfile removed.\n"; 
}
}
close LOGFL;
