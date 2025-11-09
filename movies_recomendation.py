import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer # creates a matrix of 0s and 1s
from sklearn.metrics.pairwise import cosine_similarity # does the job of checking similarity
movies=pd.read_csv(r'C:\Users\Avina\Downloads\IMDBdata_MainData.csv')
#creates some empty spaces so that crashes can be prevented
movies['Genre']=movies['Genre'].fillna('')
movies['Director']=movies['Director'].fillna('')
movies['Writer']=movies['Writer'].fillna('')
movies['Actors']=movies['Actors'].fillna('')
movies['info']=movies['Genre'] + ' ' + movies['Director'] + ' ' + movies['Writer'] + ' ' + movies['Actors']
#converts the text into nos(0s nd 1s)
cv=CountVectorizer(stop_words='english')
vectors=cv.fit_transform(movies['info'])
similarity=cosine_similarity(vectors)
def find_idx(movie_name):
    movie_name=movie_name.lower()
    for i in range(len(movies)):
        if movies.loc[i,'Title'].lower()==movie_name:
            return i
    return -1
def recomender(movie_name):
    idx=find_idx(movie_name)
    if idx==-1:
        print("movie not found in the database try again:")
        return
    scores=list(enumerate(similarity[idx]))
    for i in range(len(scores)):
        for j in range(i+1,len(scores)):
            if scores[i][1]<scores[j][1]:
                temp=scores[i]
                scores[i]=scores[j]
                scores[j]=temp
    print("\nMovies Similar to:",movies.loc[idx,'Title'])
    print("-----------------------------------------------")
    for i in range(5):
        movie_idx=scores[i][0]
        print(movies.loc[movie_idx,'Title'])
inp=input("enter the preferred movie of ur choice:")
recomender(inp)
