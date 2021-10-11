import subprocess
import sys
import binascii
import ast

REPOSITORY_NAME = 'MergeEventDetectiton'
FROM = 'develop01'
TO = 'develop03'

try:
  command = [
    "aws", "codecommit", "get-merge-conflicts",
    "--repository-name" , REPOSITORY_NAME,
    "--source-commit-specifier", FROM,
    "--destination-commit-specifier", TO,
    "--merge-option", "FAST_FORWARD_MERGE"
  ]
  res = subprocess.run(command, text=True, stdout=subprocess.PIPE)
  # print(type(res))
  res_toString = res.stdout.replace('false','False').replace('true','True')
  result_dict = ast.literal_eval(res_toString)
  
  # print(result_dict)
  
  if result_dict['mergeable'] == False:
    print("マージできないよ")
  else:
    print("マージできるよ")
except Exception as e:
  print(e)
