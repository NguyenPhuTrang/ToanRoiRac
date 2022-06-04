from math import fabs
from msilib import sequence
from pickle import TRUE
from tracemalloc import stop
from xml.etree.ElementInclude import include

class GenerationAlgorithm(object):
    def __init__(self):
        '''
        Contructor
        '''

    '''
    Phương thức generateBinarySequences() được đặc tả để sinh một dãy nhị phân độ dài n.

    Một dãy nhị phân độ dài n là một dãy x[1…n] trong đó x[i] ∈ {0, 1} (∀i : 1 ≤ i ≤ n).
    '''
    def generateBinarySequences(n, sequences):
        '''
        Bước 1 định nghĩa mảng bao gồm các phần tử của một dãy nhị phân
        Mảng này bao gồm n phần tử 
        Xác định dãy ban đầu là 0...0
        '''
        x = [0] * n

        '''
        Bước 2 thực hiện thuật toán sinh
        '''
        stop = False
        while(not stop):
            '''
            Bước 2.1:
                Thêm dãy nhị phân hiện tại vào sequences
            '''
            biSe = ""
            for element in x:
                biSe += str(element)
            sequences.append(biSe)

            '''
                Bước 2.2:
                    x[i] là phần từ cuối dãy
                    Lùi dần i cho tới khi gặp số 0 hoặc khi i = 0
            '''
            i = n - 1
            while ((i >= 0) and (x[i] == 1)):
                i -= 1
            
            '''
            Chưa gặp dãy 11...1
            '''
            if(i >= 0):
                '''
                Thay x[i] bằng số 1
                '''
                x[i] = 1

                '''
                Gán x[i + 1] = x[i + 2] = ... = x[n - 1] = 0
                '''
                for j in range (i + 1, n):
                    x[j] = 0

            '''
            Dừng lại khi gặp dãy 11...1
            '''
            if(i < 0):
                stop = True
    '''
    Sinh dãy nhị phân độ dài n
    '''
    n = 3
    sequences = []
    genAl = generateBinarySequences(n, sequences)
    for seg in sequences:
        print(seg)

    '''
    Phương thức generateSubSets() được đặc tả để liệt kê các tập con k phần tử của tập {1, 2, …, n} theo thứ tự từ điển.
    '''
    def generateSubSets(n, k, sequences):
        '''
        Định nghĩa mảng bao gồm các phần tử của một tập con
        Mảng này bao gồm k phần tử
        '''
        x = [0] * k

        '''
        Xác định tập con ban đầu là 1 2 ...k
        '''
        for i in range(k):
            x[i] = i + 1
        
        '''
        Thực hiện thuật toán sinh
        '''
        countsubSet = 1
        stop = False
        while (not stop):
            '''
            Thêm tập con hiện tại vào sequences
            '''
            curSubSets = []
            for element in x:
                curSubSets.append(element)
            sequences[countsubSet] = curSubSets

            countsubSet += 1

            '''
            x[i] là phần tử cuối chuỗi
            Lùi dần i cho tới khi gặp x[i] chưa đạt giới hạn trên n - k + i
            '''
            i = k - 1
            while ((i >= 0) and (x[i] == n - k + i + 1)):
                i -= 1
            
            '''
            Nếu chưa lùi đến 0 có nghĩa là chưa phải cấu hình kết thúc 
            '''
            if(i >= 0):
                '''
                Tăng x[i] lên 1
                '''
                x[i] += 1

                '''
                Gán các phần tử đứng sau x[i] bằng các giới hạn dưới của nó
                '''
                for j in range(i + 1, k):
                    x[j] = x[j - 1] + 1
            
            '''
            Lùi đến tận 0
            Tất cả các phần tử đã đạt giới hạn trên
            '''
            if(i < 0):
                stop = True

    '''
    Sinh tập con k phàn tử của tập{1, 2, ..., n}
    '''
    n = 5
    k = 3
    sequences = {}
    genAl = generateSubSets(n, k, sequences)

    for countSubSet, subSet in sequences.items():
        print(str(countSubSet) + ": \t {", end= "")

        for element in subSet:
            print(str(element) + ", ", end= " ")
        
        print("}")
    

    '''
    Phương thức generatePermutation() được đặc tả để liệt kê các hoán vị của tập {1, 2, …, n} theo thứ tự từ điển.
    '''
    def generatePermutation(n, sequences):
        '''
        Định nghĩa mảng bao gồm các phần tử của 1 hoán vị
        Mảng này bao gồm n phần tử 
        '''
        x = [0] * n

        '''
        Xác định hoán vị ban đầu là 1 2... n
        '''
        for i in range(n):
            x[i] = i + 1

        '''
        Thực hiện thuật toán sinh
        '''
        countPermutation = 1
        stop = False
        while (not stop):
            '''
            Thêm hoán vị hiện tại vào sequences
            '''
            curPermutation = []
            for element in x:
                curPermutation.append(element)
            sequences[countPermutation] = curPermutation

            countPermutation += 1

            '''
            Bắt đầu điều chỉnh từ x[n - 1]
            '''
            i = n - 2
            while((i >= 0) and (x[i] > x[i + 1])):
                i -= 1
            
            '''
            Chưa gặp phải hoán vị cuối (n, n - 1, ..., 1)
            '''
            if(i >= 0):
                '''
                x[k] là phần tử cuối dãy
                '''
                k = n - 1

                '''
                Lùi dần k cho tới khi gặp x[k] sao cho x[i] > x[k]
                '''
                while (x[k] < x[i]):
                    k -= 1

                '''
                Đổi chỗ x[k] và x[i]
                '''
                tmp = x[k]
                x[k] = x[i]
                x[i] = tmp
            
            '''
            Lật ngược đoạn cuối giảm dần - a: đầu đoạn - b: cuối đoạn
            '''
            a = i + 1
            b = n - 1

            while (a < b):
                '''
                Đảo giá trị x[a] và x[b]
                '''
                tmp = x[a]
                x[a] = x[b]
                x[b] = tmp

                '''
                Tiến a và lùi b cho tới khi a, b gặp nhau
                '''
                a += 1
                b -= 1

            '''
            Toàn dãy là dãy giảm dần
            '''
            if(i < 0):
                stop = True

    '''
    Liệt kê các hoán vị của {1, 2, ..., n}
    '''
    n = 4
    sequences = {}
    genAl = generatePermutation(n, sequences)

    for countSubSet, subSet in sequences.items():
        print(str(countSubSet) + ": \t {", end= "")

        for element in subSet:
            print(str(element) + ", ", end= " ")
        
        print("}")
        
if __name__ == 'main':
    genAl = GenerationAlgorithm()

