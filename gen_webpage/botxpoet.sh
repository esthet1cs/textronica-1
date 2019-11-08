#!/bin/bash


# bot-script für den 2theo-twitterbot (botXpoet)

# Konfiguration

WEBDIR=/home/user/dock/websites/esthet1cs.net/botxpoet/

# PROCDIR=~/textgen   # this is hardcoded in the following lines

TWEET=$(python ~/textgen/botxpoet.py)

echo $TWEET >> ~/textgen/tweets

# move to the textgen directory
cd ~/textgen

# build the index.html 
cat header.html > index.html
echo "<title>botxpoet's newest</title></head>" >> index.html
cat body.html >> index.html
echo '<p class="single">' >> index.html
echo $TWEET >> index.html
cat footer.html >> index.html

# build the stream.html

cat header.html > stream.html
echo "<title>botxpoet's stream</title></head>" >> stream.html
cat body.html >> stream.html
#echo '<p style="textalign:left;margin-left:20%;margin-top:-15%">' >> stream.html

# cat every line into the html-file and add a line break
while read line; do echo "$line <br>" >> stream.html; done < ~/textgen/tweets

cat footer.html >> stream.html

rsync index.html $WEBDIR
rsync stream.html $WEBDIR
