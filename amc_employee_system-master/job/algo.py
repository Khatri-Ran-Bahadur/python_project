import pandas as pd
import numpy as np
import math

def euclidean_distance(person1,person2, ratings):
    df_first= ratings.loc[ratings['user__email']==person1]
    df_second= ratings.loc[ratings.user__email==person2]
    
    df= pd.merge(df_first,df_second,how='inner',on='job__title')
    
    if(len(df)==0): return 0
    
    sum_of_squares=sum(pow((df['rating_x']-df['rating_y']),2))
    r = 1/(1+sum_of_squares)
    #print("euc similarity", r)
    return r

def pearson_score(user1, user2, ratings):
    #Get detail for Person1 and Person2
    df_first= ratings.loc[ratings.user__email==user1]
    df_second= ratings.loc[ratings.user__email==user2]

    # Getting mutually rated items    
    df= pd.merge(df_first,df_second,how='inner',on='job__title')
    
    # If no rating in common
    n=len(df)
    if n==0: return 0

    #Adding up all the ratings
    sum1=sum(df['rating_x'])
    sum2=sum(df['rating_y'])
    
    ##Summing up squares of ratings
    sum1_square= sum(pow(df['rating_x'],2))
    sum2_square= sum(pow(df['rating_y'],2))
    # sum of products
    product_sum= sum(df['rating_x']*df['rating_y'])
    ## Calculating Pearson Score
    numerator= product_sum - (sum1*sum2/n)
    denominator=math.sqrt(
        (sum1_square- pow(sum1,2)/n) * 
        (sum2_square - pow(sum2,2)/n)
        )
    if denominator==0: return 0
    r=numerator/denominator
    #print("pearson similarity", r)
    return r

def topMatches(personId,n=5,similarity=pearson_score):
    scores=[(similarity(personId,other),other) for other in ratings.loc[ratings['user__email']!=personId]['user__email']]
    print(scores)
    # Sort the list so the highest scores appear at the top
    scores.sort( )
    scores.reverse( )
    return scores[0:n]

# user1 = "testuser_1@gmail.com"
# for i in range(2, 11):
#     user2 = f"testuser_{i}@gmail.com"

#     pearson_score(user1, user2)
#     euclidean_distance(user1, user2)

def getRecommendation(data, personId, similarity=euclidean_distance):

    totals,simSums= {},{}
    ratings = data["ratings"]
    jobs = data["jobs"]
    
    df_person= ratings.loc[ratings.user__email==personId]
    
    for otherUser in ratings.loc[ratings['user__email']!=personId]['user__email']: # all the UserID except personID
        
        # Getting Similarity with otherUser
        sim=similarity(personId,otherUser, ratings)
        
        # Ignores Score of Zero or Negatie correlation         
        if sim<=0: continue
            
        df_other=ratings.loc[ratings.user__email==otherUser]
        
        #job not seen by the personID
        job=df_other[~df_other.isin(df_person).all(1)]
        
        for jobtitle,rating in (np.array(job[['job__title','rating']])):
            #similarity* Score
            totals.setdefault(jobtitle,0)
            totals[jobtitle] += rating * sim
            
            #Sum of Similarities
            simSums.setdefault(jobtitle,0)
            simSums[jobtitle] += sim
            
    # Creating Normalized List
    ranking=[(t/simSums[item],item) for item,t in totals.items()]
    
    ranking.sort()
    ranking.reverse()
    recommendedId=np.array([x[1] for x in ranking])
    r_jobs = jobs[jobs['title'].isin(recommendedId)]['title']
    top_n = np.array(r_jobs)[:5]
    return top_n

