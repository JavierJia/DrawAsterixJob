import json,sys,fileinput

stopword='[]:'

def validateChars(name):
    global stopword
    #return filter(lambda x : not (x in stopword), name)
    return ''.join(map(lambda x : '' if x in stopword else x , name))

def printOperators(node):
    for ops in node['operators']:
        opid =  validateChars(ops['id'])
        opname = validateChars(ops['display-name'])
        sys.stdout.write(opid + ' [ label = "' + opname + '" ];\n')

def printConnectors(node):
    for cn in node['connectors']:
        cname = validateChars(cn['connector']['display-name'])
        opfrom = validateChars(cn['in-operator-id'])
        opto = validateChars(cn['out-operator-id'])
        sys.stdout.write( opfrom + ' -> ' + opto + ' [ label = "' + cname + '"];\n')

jsonfile = ""
for line in fileinput.input():
    jsonfile += line

jobs = json.loads(jsonfile)


sys.stdout.write('digraph AsterixJob { node [shape = record,height=.1];\n')
printOperators(jobs)
printConnectors(jobs)
sys.stdout.write('}\n')

