import os
os.chdir('./main')
for i in os.walk('./'):
    for j in i[2:]:
	j.endswith('.py')
            
