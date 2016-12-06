import string

def alphafreq ( sample ):
    output = {}
    #alphabet = string.ascii_lowercase
    for item in sample:
        output[item] = 0
    #output = dict.fromkeys(alphabet, 0)
    for item in sample:
        output[item] += 1

    for key in output:
        print(key, output[key])


alphafreq(input('Please enter a sentence:') )
#alphafreq('test')#
