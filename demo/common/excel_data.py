import xlrd, os

from demo.common.function import project_path


def read_excel(filename,index):
    #获取操作对象，打印单个表中的行数和列数
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    #利用双循环封装数据
    dic={}
    for j in  range(sheet.ncols):
        data=[]
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
            print(data)
        dic[j]=data
    return dic

if __name__ == '__main__':
    data = read_excel(project_path()+"data\\testdata.xlsx", 0)
    print(data)
    print(data.get(1))