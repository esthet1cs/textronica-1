#!/bin/bash


# bot-script für den 2theo-twitterbot (botXpoet)


TWEET=$(python ~/python/programs/textgen/botxpoet.py)

twidge -c ~/.twidgerc_botxpoet update "$TWEET"


