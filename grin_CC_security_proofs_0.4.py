###############################################################################
#### Signature validation
#### Author: Anynomous/ Grin Community Council
#### version: 0.1
#### date 18-08-2021
#### DEPENDENCIES
## https://github.com/mcdallas/cryptotools
## pip install git+https://github.com/mcdallas/cryptotools.git@master
###############################################################################
		
#import cryptotools
try:
	from cryptotools.BTC import Transaction
	from cryptotools import hex_to_bytes, Transaction
	import sys 
except:
	print("In order to verify the security proofs you need to install the Cryptotool library (requires python 3.X) using the following command: ")
	print("pip install git+https://github.com/mcdallas/cryptotools.git@master#egg=cryptotools")


	
if len(list(sys.argv)) <2:
	print('please run this script with either a file as input, or by piping information to it, Examples:')
	print('python grin_CC_security_proofs_0.4.py 2021-08-01_security_proof_CC_.txt')
	print('OR')
	print('cat 2021-08-01_security_proof_CC_.txt |grin_CC_security_proofs_0.4.py')
	exit
	
if len(list(sys.argv)) == 2:
	lines =[]
	file_name = sys.argv[1]
	f1 =  open(file_name,'r+')
	for line in f1:
		line = line.strip()
		lines.append(line)

else:
	lines =[]
	for line in sys.stdin:
		lines.append(line)
	
transaction = False
signatures = []
for line in lines:
	line = line.strip()
	## skip empty lines
	if len(line) == 0:
		continue
	## detect transaction id
	if len(line) == 65 and line[0] == '>':
		transaction = line.strip('>')
	## detect signature	
	if len(line) == 142:
		signatures.append(line)

print("Transaction:", transaction)	
#print(signatures)	

## Check transaction, get two version to try both replaement of first two and last two signatures
try:
	tx = Transaction.get(transaction)
	inp = tx.inputs[0]
	wit = list(inp.witness) 
	## The below two copies of witness data will be later used for replacing
	## and verifying replacements of both the first two signatures and 2 & 3 signature
	wit_v1 = list(inp.witness)
	wit_v2 = list(inp.witness)
except:
	print('Not a valid transaction ID, not present on the Bitcoin blockchain')
## Validate signatures
valid_signature_count = 0

## Try if signature already in witness data
## Check if signature is present in witness data, if so it is valid by default
signatures_not_in_witness = []
for signature in set(signatures):
	signature_bytes = hex_to_bytes(signature)
	in_witness = False 
	for stack_element_bytes in wit:
		if signature_bytes in stack_element_bytes:
			print("Signature in witness data:    ", signature)
			print("Signature valid: True")
			valid_signature_count+=1
			in_witness = True
	if in_witness == False: 
		signatures_not_in_witness.append(signature)
			
## Test validity of signatures not in witness data
## Test validity for both replacing signatures 1,2 and 2,3
## to be 100% certain there are no additional signatures from a single keyholder
		
for i, signature in enumerate(set(signatures_not_in_witness)):
	signature_bytes = hex_to_bytes(signature)
	## First set of witness data, to try replacing first two signatures
	wit_v1[i] = signature_bytes
	## Second set of witness data, 
	wit_v2[-i+1] = signature_bytes

	
	
## Test if both the first and second replacement confirm the signature is valid
inp.witness = tuple(wit_v1)
signature_valid_v1 = tx.verify()
inp.witness = tuple(wit_v2)
signature_valid_v2 = tx.verify()

if signature_valid_v1 and signature_valid_v2:
	valid_signature_count+=len(signatures_not_in_witness) ## Adds plus 2 if the two extra signatures are valid
	for signature in signatures_not_in_witness:
		print("Signature not in witness data:", signature)
		print("Signature valid:", True)
		
else:
		print("Signature not in witness data:", signatures_not_in_witness)
		print("One of the provided signatures is not valid")
	

## Print summary of results			
print('Done, {} out of {} signatures in security proof are proven to be valid'.format(valid_signature_count,len(signatures)))
##############################################################################
