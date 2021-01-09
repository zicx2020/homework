my_file = open("file.txt", "w+")  #создаём файл
read = open("1.txt.txt").read()
read_2 = open("2.txt.txt").read()
num_1 = len(open('1.txt.txt').readlines())  # считаем сколько строк
num_2 = len(open('2.txt.txt').readlines())
if num_1 > num_2 :
    my_file.write('2.txt \n' + str(num_2) + '\n' + read_2 + '\n' + '1.txt \n' + str(num_1) + '\n' + read)
elif num_2 >num_1 :
    my_file.write('1.txt \n' + str(num_1) + '\n' + read + '\n' + '2.txt \n' + str(num_2) + '\n' + read_2)
my_file.close()
with open('file.txt') as f :
 print(f.read())

