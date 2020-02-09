packing_list = []
packing_list.append("shirt")
packing_list_2 = packing_list
packing_list_2.append("pants")
packing_list_3 = packing_list_2
packing_list.append("socks")
print (packing_list)
print (packing_list_2)
print (packing_list_3)

print (len({3, 2, 9, 5, 3, 6, 2}) + len([3, 2, 9, 5, 3, 6, 2]))

primes = [2, 3, 5]       # Line 1

for prime_number in primes: # Line 2
  print(prime_number)       # Line 3

print('Done!')

##
total = 0

for num in range(6):  # the easy way
  total += num

print(total)

your_name = input("Enter something")

print (your_name)

jobs = ['CEO', 'data scientist', 'instructor'] # Line 1

if jobs:                    # Line 2
    if 'Pilot' in jobs:     # Line 3
        print(jobs[0])      # Line 4
    else:                   # Line 5
        print(jobs[1])      # Line 6
else:                       # Line 7
    print(jobs[2])          # Line 8

####
print ("\n")

class Band(object):
    def __init__(self, band, genre):
        self.band = band
        self.genre = genre

    def give_stats(self):
        #print ("band: " + self.band + " genre: " + self.genre)
        self.stats = "band: " + self.band + " genre: " + self.genre
        return self.stats

Queen = Band("Queen", "Rock")
print(Queen.give_stats())
