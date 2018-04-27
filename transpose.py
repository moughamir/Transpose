W = 7
#msg = 'ABCDEF0123....'
msg = '.DC01.B.AF.2E3' # 100 time
method = "ENC"
perm = [4, 5, 6, 3, 2, 0, 1] # hard coding the key for test purpose

while len(msg) % (2*W):
    msg += "."
    

def encrypt(target):
  for i in xrange(100):
    target = target[1:] + target[:1]
    target = target[0::2] + target[1::2]
    target = target[1:] + target[:1]
    res = ""
    
    for j in xrange(0, len(target), W):
      for k in xrange(W):
        res += target[j:j+W][perm[k]]
    target = res
    
    print 'Transposed for '+str(i+1)+ '  time '+target
  
  print('--------------------------------------')
  print('Encrypted  : '+target)
  print('--------------------------------------')


'''
TODO: 
decrypt that
'''

def decrypt(target):
  lh = len(target)/2
  subT = ""
  target = target[-1]+target[:-1]
  
  for i in xrange(lh):
    subT += target[i::lh]
    
  target = subT[-1]+subT[:-1]
  
  print('Decrypted  : '+target)

if method == 'ENC':
  print('Input      : '+msg)
  encrypt(msg)
  
elif method == 'DEC':
  print('Input      : '+msg)
  decrypt(msg)
  
else:
  print('Undefined Method')