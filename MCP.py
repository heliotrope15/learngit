#encoding: utf-8
from __future__ import print_function
class mcp():
    def __init__(self,n,matrix):
        self.matrix=matrix   #无向图G的邻接矩阵
        self.v=n        #无向图G的顶点
        self.e=0          #无向图G的边
        self.x=[0]*(n+1)           #顶点与当前团的连接，x[i]=1 表示有连接
        self.bestx=[0]*(n+1)   #当前最优解
        self.bestn = 0  # 当前团的顶点数目
        self.cnum = 0  # 最大团的顶点数目
    def new(self,n):
        self.x = [0] * (n + 1)  # 顶点与当前团的连接，x[i]=1 表示有连接
        self.bestx = [0] * (n + 1)
        self.bestn = 0
        self.cnum = 0
# test=mcp(2)
class getmcp():
    def judge(self,matrix):
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix)):
                if (matrix[i][j] == 1):
                    return True
        return False
    def backTrack(self,mcp,i):
        if i>mcp.v:
            for j in range(1,mcp.v+1):
                mcp.bestx[j]=mcp.x[j]
            mcp.bestn=mcp.cnum
            return
        OK=1
        for j in range(1,i+1):
            if (mcp.x[j]==1 and mcp.matrix[i][j]==0):#i不与J相连
                 OK=0
                 break
        if OK==1:
            mcp.x[i]=1  #把i加入团
            mcp.cnum+=1
            self.backTrack(mcp,i+1)
            mcp.x[i]=0
            mcp.cnum-=1
        if (mcp.cnum+mcp.v-i>mcp.bestn):
            mcp.x[i]=0
            self.backTrack(mcp,i+1)
    def checklist(self,list,carrry):
        for i in range(1,len(carrry)):
            if carrry[i]==0:
                l=[]
                l.append(i)
                list.append(l)
        return list
    def clearE(self,mcp,line):
        matrix=mcp.matrix
        for i in range(1,mcp.v+1):
            matrix[line][i]=0
        for i in range(1, mcp.v+1):
            matrix[i][line] = 0
        mcp.matrix=matrix

class runmain():
     if __name__ == '__main__':
        n = 6
        matrix = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0]]
        print ("初始化中...")
        getmcp = getmcp()
        mcp = mcp(n, matrix)
        print ("初始化完成，邻接矩阵为：")
        carray = [0] * (n + 1)
        list = []
        while getmcp.judge(mcp.matrix):
            # print (getmcp.judge(mcp.matrix))
            for i in range(1,n):
                l = []
                for j in range(1,n+1):
                    l.append(mcp.matrix[i][j])
                print (l)
            mcp.new(n)
            getmcp.backTrack(mcp,1)
            print ("最大团顶点数为："+str(mcp.bestn))
            print("最大团方案为：")
            l = []

            for i in range(1,mcp.v+1):
                if mcp.bestx[i]==1:
                    print (i,end=" ")
                    l.append(i)
                    carray[i]=1
                    getmcp.clearE(mcp,i)
            list.append(l)
            print (' ')
        list = getmcp.checklist(list, carray)
        print (list)