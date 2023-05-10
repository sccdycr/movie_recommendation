"""
热门推荐
"""
import GlobalFun
import GlobalVar

#设置热门电影
def sethotlist(num):
    hotlist = []
    sql='SELECT * FROM dbmovierecommender.movie_score_info where times>50 order by score desc limit {}'.format(num)#获取点击次数大于50次的电影，降序排序
    conn, cur = GlobalFun.ConnectSql() #链接数据库
    cur.execute(sql)
    data=cur.fetchall() #fetchall函数返回多个元组
    for d in data:
        hotlist.append(d[0])#将热门电影加入热门推荐列表
    return hotlist

class hotRecommendation:
    hotlist = sethotlist(GlobalVar.hotmovienum)

    def gethotmovie(self, num,haveseelist=None):#不需要这个
        """根据电影热度选出前num个热门电影，最多选出hotmovienum个"""

        if GlobalVar.hotmovienum < num:
            num = GlobalVar.hotmovienum
        #hotmovie=set(self.hotlist)-set(haveseelist)#减去失去了顺序
        hotmovie=[]
        n=0
        if haveseelist is not None:
            for h in self.hotlist :
                if h not in haveseelist:
                    n=n+1
                    hotmovie.append(h)
                    if n>=num:
                        break
        else:hotmovie=self.hotlist
        return hotmovie[:num]

    def train(self):#离线计算
        """训练，为电影热度打分并保存"""

        #删除热门电影表


        #重新获得热门电影表

"""测试======"""
# hotrec=hotRecommendation()
# l=hotrec.gethotmovie(10,[318,858])
# print(l)


