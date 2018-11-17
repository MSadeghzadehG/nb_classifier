import pandas as pd
import numpy as np


def cal_p(data,labels):
    # print(data)
    labels = list(labels)
    n = labels.count(-1)
    p = labels.count(1)
    md = max(data)
    subset = [0] * (2*(md+1))

    for i in range(0,len(data)):
        if labels[i]==-1:
            # print(data[i])
            subset[data[i]] += 1
        else :
            subset[data[i]+md+1] += 1
    for i in range(0,md+1):
        subset[i] /= n
    for i in range(md+1,len(subset)):
        subset[i] /= p
    return subset


def multiply_p(data,p):
    # print(len(data))
    noutput = 0
    poutput = 0
    for i in range(0,len(data)):
        m = int(len(p[i])/2)
        # print(data[i])
        # print(m)
        # print((p[i]))
        if m-1<data[i]:
            # pass
            poutput += np.log(0.00000001)
            noutput += np.log(0.00000001)
        else:
            if p[i][int(data[i])] != 0.0:
                noutput += np.log(p[i][int(data[i])])
            else :
                noutput += np.log(0.00000001)
            if p[i][m+int(data[i])] != 0:
                # print(m+data[i])
                poutput += np.log(p[i][m+int(data[i])])
            else :
                poutput += np.log(0.00000001)
        output = [noutput,poutput]
        # print(output)
        # input()
    return output


def main():
    df = pd.read_csv('train.csv')
    # print(df.head())
    dfarray = df.values
    # print(dfarray)

    p = []
    for c in df:
        if c != '-1':
            p.append(cal_p(df[c].values,df['-1'].values))
        # print(cal_p(df[c].values,df['-1'].values))
        # input()
        # print(c)
    # print(result)
    # print(len(p))
    result = []
    trues = []
    dftest = pd.read_csv('test.csv')
    # print(dftest.head())
    for index, row in dftest.iterrows():
            c = multiply_p(list(row[:len(row)-1]),p)
            trues.append(row[len(row)-1])
            result.append(c.index(max(c)))
    # print(len(result))
    # print(len(trues))
    r=[]
    for (x1, x2) in zip(trues, result):
        if (x1 == -1 and x2==0) or (x1==x2):
            r.append(1)
        else:
            r.append(0)
    print(r.count(1)/len(r))


if __name__ == '__main__':
    main()