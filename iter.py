
import pandas as pd

def combos(a,b,c):
    totalcombos = []
    for i in a:
        for j in b:
            for k in c:
                #print(i,j,k)
                totalcombos.append((i,j,k))
    print(len(totalcombos))
    num = []
    for i in range(len(totalcombos)):
        num.append(i)
    excel_csv = {'Number': num,'Combos': totalcombos}
    excel_xls = {'Combos': totalcombos} 
    df = pd.DataFrame(data=excel_csv)
    df = pd.DataFrame(data=excel_xls)
   # print(excel)
    df.to_csv('combos.csv',index=False)
    df.to_excel('combos.xlsx', engine='xlsxwriter')  



    return

def main():
 #   a = ['ea_1','ea_2','ea_3']
    a_1 = input('How many electron acceptors? ')
    a = []
    for i in range(int(a_1)):
        if i == ' ':
            i
        else:
            a.append(str(i+1)+'ea')
    print((a,'You have '+str(len(a))+' electron acceptors.'))

 #   a = ['a','b']
   # b = ['b_1','b_2','b_3']
    b_1 = input('How many backbones? ')
    b= []
    for i in range(int(b_1)):
        if i == ' ':
            i
        else:
            b.append(str(i+1)+'b')
    print(b)
    print((b,'You have '+str(len(b))+' backbones.'))

   # b = ['b','c']
   # c = ['ed_1','ed_2','ed_3']
    c_1 = input('How many electron donors? ')
    c = []
    for i in range(int(c_1)):
        if i == ' ':
            i
        else:
            c.append(str(i+1)+'ed')
    print(c)
    print((c,'You have '+str(len(c))+' electron donors.'))
   # c =['c','b']
    combos(a,b,c)





    return 
main()