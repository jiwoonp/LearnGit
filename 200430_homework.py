#########################################################################################
## playing with numpy

import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
print(a[::2])
print(a[-1])

aa = np.array(np.arange(12)).reshape((3,4))
bb = np.array(np.arange(12)).reshape((4,3))
print('\naa =')
print(aa)
print('\nbb =')
print(bb)

print('\nIndexing a 2-D array: aa[:3, :]')
print(aa[:3, :]) # the second : means "all items of that axis"

print('\nElement-by-element operation (like .* in MATLAB): ')

print('\n - exponentiation')
print(aa**2.7) # exponentiation is **

print('\n - square root')
print(np.sqrt(aa)) # square root

print('\n - Error from aa + bb')
try:
    print(aa + bb) # addition (throws an error because aa and bb are different shapes)
except ValueError as err:
    print(err)
print('\n - aa + bb.T works')
print(aa + bb.T) # need to take transpose of bb so it has the same shape as aa

print('\nMatrix multiplication using @: aa @ bb')
print(aa @ bb)

print('\nMatrix multiplication using @: bb @ aa')
print(bb @ aa)

print('\nConcatenate two arrays')
cc = np.concatenate((aa,aa), axis=1)
print(cc)

print('\nFlatten and array')
print(aa.flatten())

print('\n Make a Boolean mask of aa >= 5')
mask = aa >= 5
print(mask)

print('\n Use the mask to get just those elements of aa: aa[mask]')
print(aa[mask])
print('Note that this returns just a 1-D arrray (flattened)')

b = a
b[3] = 1
print(a)
print(b)

b = a.copy()
b[3] = 1
print(a)
print(b)

print('\nMean of array a is ', np.mean(1))

print('\nStandard deviation of array a is ', np.std(a))

print('\nMaximum element of array a is ', np.amax(a))

print('\nIndex of maximum element of array a is ', np.argmax(a))


af = a.astype(float)
af[5] = float('nan')
print(af)

print("Mean of array af with mean function is", np.mean(af))  
print("Mean of array af with nanmean function is ", np.nanmean(af))  


print("add elements at the end of an array: ", np.append(a, 7))
print("insert elements to array: ", np.insert(a, 3, 10))
print("delete nth element from array: ", np.delete(a, [4]))

b = np.array([1,-2,3,-4,5,-6])
print(np.abs(b))

c = np.concatenate((a,b))
print("concatenate multiple arrays: ", c)

d = np.hsplit(c,3)
print("split arrays: ", d)
print("transpose arrays: ", np.transpose(d))

print("3 random numbers from normal distribution: ", np.random.normal(size=3))
print("3 random intergers between 1 and 10: ", np.random.randint(high=10, low=1, size=3))

print("sign of each element in array: ", np.sign(b))


d = np.array([1.15, 3.62, 8.51])
print("round decimal values: ", np.around(d))
print("round decimal values with 1 decimal places: ", np.around(d, decimals=1))


#########################################################################################
## using pickle to have the code save outputs

import sys, os
import numpy as np
import pickle

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
out_dir = '../../' + this_dir + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

# save array as a pickle file
out_fn = out_dir + 'pickled_array.p'
pickle.dump(c, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
c = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary


#########################################################################################
## using argparse to add command line arguments to code

import argparse

def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--a_string', default='multiply numbers by changing b and c values: ', type=str)
parser.add_argument('-b', '--integer_b', default=10, type=int)
parser.add_argument('-c', '--integer_c', default=2, type=int)
parser.add_argument('-v', '--verbose', default=True, type=boolean_string)

args = parser.parse_args()

print(args.a_string)
print(args.integer_b * args.integer_c)
