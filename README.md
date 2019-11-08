Textronica 1 is a small project to rebuild a textgenerator that Theo Lutz and Rul Gunzenhäuser built in 1959 to produce their 'stochastic texts'. At the time, they only printed a couple of sentences and published even less than they produced. Textronica 1 should help to explore the logic and the esthetics of the generator and of the generated texts. 

The files can partly be used as standalone scripts to generate stochastic texts. the gen_webpage directory contains the necessary scripts to generate the active webpage currently hosted at <https://esthet1cs.net/botxpoet>

#. botxpoet.py: stochastic texts as a twitter bot (you will need a file called 'credentials' with the necessary credentials in order to use this)
#. botxpoet-complete_sorted.py: generate the full set of stochastic texts in a static fashion, without any randomized choices
#. botxpoet-continuous.py: generate stochastic texts continuously on your console
#. botxpoet-continuous_eng.py: an english translation of the script above
#. stochastische_texte_volltext_sortiert.txt: the full sorted (!) set of all possible stochastic texts as defined in the classic stochastic texts generator algorithm

For a more in-depth statement see http://esthet1cs.net/botxpoet/xplain.html
