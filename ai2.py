count=0
keys=['engineer','engineering',"engineers"]
input_tree=['A','typical','student','of','engineering','is','called','an'
            ,'engineer','after','completion','of','engineering','in','the'
            ,'stipulated','time','frame','Engineers','should','have','the'
            ,'capability','to','create','think','and','administer',
            'novelty']
for i in input_tree:
    if i.lower() in keys:
        count+=1
print("The number of occurences of the search key is:",count)
