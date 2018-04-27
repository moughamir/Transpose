W = 7
## original msg = 'ABCDEF0123....'
msg = 'DF13..CE02..AB'
method = "DEC"

while len(msg) % (2*W):
    msg += "."
    

def encrypt(target):
  target = target[1:] + target[:1]
  target = target[0::2] + target[1::2]
  target = target[1:] + target[:1]
  print('Encrypted  : '+target)
  
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