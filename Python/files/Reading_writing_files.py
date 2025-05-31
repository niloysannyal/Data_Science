# p = open("file2.txt","r")
# p_out = open("file2_out.txt","w")
#
# for line in p:
#     words = line.split()
#     p_out.write("word_count:"+str(len(words))+"   "+line)
#
# p.close()
# p_out.close()

with open('file1.txt', 'r') as f:
    print(f.read())

print(f.closed)

