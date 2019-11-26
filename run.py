from fetch import get_data
from markov_python.cc_markov import MarkovChain
import textwrap


hms = int(input('How many songs do you want to mash up?'))

def get_songs():
    for i in range(hms):
        str = get_data()
        #mark.add_string(get_data())
        
mark = MarkovChain()
get_songs()
hmw = int(input('How many words do you want in this song?'))
output = mark.generate_text(hmw)
output = ' '.join(output)
print(output, 20)
