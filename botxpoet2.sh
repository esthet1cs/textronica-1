#!/bin/bash


# bot-script für den 2theo-twitterbot (botXpoet)


TWEET=$(python ~/python/programs/textgen/botxpoet.py)

ttytter -keyf=botxpoet -status="$TWEET" -silent

