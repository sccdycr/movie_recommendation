import tkinter as tk



userid = 1
BigWindow = tk.Tk()
rootpath="G:/graduation_project/code/movie_recommendation/"
#rootpath1="d:/"
#data的位置
pathmovie = rootpath+"data/movies.csv"
pathlink = rootpath+"data/links.csv"
pathrating =rootpath+ "data/ratings.csv"
pathcosSim_svd = rootpath+"data/cosSim.csv"#pickle
pathmovie_similar_svd = rootpath+"data/movie_similar_svd.csv"
pathoffline_recommend_svd = rootpath+"data/offline_recommend_svd.csv"
pathoffline_recommend_als = rootpath+"ata/offline_recommend_als.csv"
pathmovie_similar_svd =rootpath+"data/movie_similar_svd.csv"
pathmovie_similar_als = rootpath+"datda/movie_similar_als.csv"
pathusers = rootpath+"data/users.csv"
pathonline_recommend = rootpath+"data/online_recommend.csv"
pathmovieidlist = rootpath+"data/movieidlist.pickle"
hotmovienum=100
# modelals=MoveRecommend(model_path='D://costom_model', user_path=pathrating,
#                   move_path=pathmovie)#感觉不需要保存moselals
