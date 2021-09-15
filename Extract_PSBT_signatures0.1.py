# -*- coding: utf-8 -*-
"""
Created Aug  2021
Extract signatures from Partially Signed Bitcoin Transaction PSBT (Electrum)
Run either with a text file or by piping PSBT output into the script
Only works with Python 3.X, 2.7 gives padding errors
Signatures directly printed out in hex format, examples:
	
python Extract_PSBT_signatures0.1.py psbt_example_input.txt > list_of_signatures.txt
cat psbt_example_input.txt |python Extract_PSBT_signatures0.1.py > list_of_signatures.txt

In order to use the signatures with a security proof, add of the beginning of 
the output file ">" followed by the transaction id.

-https://github.com/petertodd/python-bitcoinlib
-https://pypi.org/project/python-bitcointx/
-https://bitcointechweekly.com/front/bip-174-psbt-partially-signed-bitcoin-transactions/
-https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki
DEPENDENCIES:
	base64
	re
@author: Anynomous

"""
import sys
import base64 #  PSBT's are base64 encrypted when exported as plain text
import re
import binascii


if len(list(sys.argv)) <2:
	print('please run this script with either a file as input, or by piping information to it, Examples:')
	print('python Extract_PSBT_signatures0.1.py psbt_example_input.txt')
	print('OR')
	print('cat psbt_example_input.txt |python Extract_PSBT_signatures0.1.py')


if len(list(sys.argv)) == 2:
	## Assume a text file with PSBT's is fed as input, open and parse file
	file_name = sys.argv[1]
	f1 =  open(file_name,'r+')
	lines = []
	for i,line in enumerate(f1):
		line = line.strip()
		lines.append(line)
else:
	lines =[]
	for line in sys.stdin:
		lines.append(line)

## looop over input, add to the raw psbt_base64, test if right length
psbt_base64_binary_string_list = []	
psbt_decoded = []
for i,line in enumerate(lines):
	line = line.strip()
	psbt=line
	## skip empty lines
	if line == '':
		continue
	try:
		psbt_decoded.append(base64.b64decode(psbt).hex())
	except:
		print(line)
		print('PSBT: ',i,' malformed, incorrect padding')
		print('Length: ',len(psbt))
		## convert piped bytes seedn as string back to bytes
		line = base64.b64decode(psbt).hex()
		psbt_base64_binary_string_list.append(line)
		psbt_decoded.append(bytes(base64.b64decode(psbt)).hex())

## Loop over decoded PSB's, extract signatures, print to standard output	
signatures = []
for i,psbt in enumerate(psbt_decoded):
	p1_list = [m.start() for m in re.finditer('30440220', psbt)]
	## Loop over the begin position of the signaures, slice them out
	for p1 in p1_list:
		p2 = int(str(46),16)*2+2 +p1 #Hex -> decimal-> +2 since 2 bits of length, bits #Now hard coded, but in case I need to parse the stack
		after = psbt[p2:p2+2]
		if after not in ['47', '48']:  ## ugly hack to avoid interpreting PSBTs, valid signatures are not followed by these numbers, ugly but it works
			signature = psbt[p1:p2]
			signatures.append(signature)
			print(signature) ## print signature to standard output
