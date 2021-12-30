
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
    df.to_csv('combos.csv',index=False)
    df.to_excel('combos.xlsx', engine='xlsxwriter')  



    return

def main():
    a_1 = input('How many electron acceptors? ')
    a = []
    for i in range(int(a_1)):
        if i == ' ':
            i
        else:
            a.append(str(i+1)+'ea')
    print((a,'You have '+str(len(a))+' electron acceptors.'))

    b_1 = input('How many backbones? ')
    b= []
    for i in range(int(b_1)):
        if i == ' ':
            i
        else:
            b.append(str(i+1)+'b')
    print((b,'You have '+str(len(b))+' backbones.'))

    c_1 = input('How many electron donors? ')
    c = []
    for i in range(int(c_1)):
        if i == ' ':
            i
        else:
            c.append(str(i+1)+'ed')
    print((c,'You have '+str(len(c))+' electron donors.'))
    combos(a,b,c)





    return 
main()
