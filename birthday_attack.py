import hashlib
from fpdf import FPDF

BLOCK_SIZE = 65536

list_of_a = []
list_of_b = []

# Compare hashes of 2 files
def compare_hash(file1, file2):
    fhash = hashlib.md5()
    with open(file1, 'rb') as file:
        finfo = file.read(BLOCK_SIZE)
        while len(finfo) > 0:
            fhash.update(finfo)
            finfo = file.read(BLOCK_SIZE)
    
    fhash2 = hashlib.md5()
    with open(file2, 'rb') as f:
        finfo2 = f.read(BLOCK_SIZE)
        while len(finfo2) > 0:
            fhash2.update(finfo2)
            finfo2 = f.read(BLOCK_SIZE)

    str1 = fhash.hexdigest()
    str2 = fhash2.hexdigest()
    if(str1 == str2):
        print(str1)
        print(str2)
        return True

    return False

def birthday_attack():
    i = 0
    j = 0
    counter = 0
    str1 = 'a.pdf'
    str2 = 'b.pdf'
    list_of_a.append(str1)
    list_of_b.append(str2)
    while True:
        if(counter%2 == 1):
            if(i == 0):
                str1 = str1[:1] + str(i) + str1[1:]
            else:
                str1 = index_file(str1)

            with open('file.txt', 'a') as f:
                f.write(' ')
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 11)
            with open('file.txt', 'r') as f:
                for letter in f:
                    pdf.cell(200, 10, txt = letter)
            pdf.output(str1)

            for bfile in list_of_b:
                if(compare_hash(bfile, str1)):
                    print("We have found the two files with the same hash")
                    print(bfile)
                    print(str1)
                    exit()
            for afile in list_of_a:
                if(compare_hash(afile, str1)):
                    print("We have found the two files with the same hash")
                    print(afile)
                    print(str1)
                    exit()
            list_of_a.append(str1)
            i = i + 1
        else:
            if(j == 0):
                str2 = str2[:1] + str(j) + str2[1:]
            else:
                str2 = index_file(str2)

            with open('file.txt', 'a') as f:
                f.write(' ')
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 11)
            with open('file.txt', 'r') as f:
                for letter in f:
                    pdf.cell(200, 10, txt = letter)
            pdf.output(str2)

            for afile in list_of_a:
                if(compare_hash(afile, str2)):
                    print("We have found the two files with the same hash")
                    print(afile)
                    print(str2)
                    exit()
            for bfile in list_of_b:
                if(compare_hash(bfile, str2)):
                    print("We have found the two files with the same hash")
                    print(bfile)
                    print(str2)
                    exit()
            list_of_b.append(str2)
            j = j + 1

        counter = counter + 1

def index_file(file_name):
    final_str = ''
    x = file_name.split('.')
    fpart = x[0]
    fpart_number = fpart[1:]
    fpart_letter = fpart[0]
    fpart_number = int(fpart_number) + 1
    final_str = fpart_letter + str(fpart_number) + '.' + x[1]
    return final_str

birthday_attack()
