import string

def alphafreq ( sample ):
    output = {}
    for item in sample:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1

    for key in output:
        print(key, output[key])


alphafreq("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan
 sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo.
  Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex,
   dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus.""")
#alphafreq('test')##
