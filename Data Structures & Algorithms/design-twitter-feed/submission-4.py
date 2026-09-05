class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=self.following[userId] | {userId}
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index=len(self.tweets[user])-1
                time,tweetid=self.tweets[user][index]
                heapq.heappush(heap,(-time,user,index,tweetid))
        result=[]
        while heap and len(result)<10:
            time,user,index,tweetid=heapq.heappop(heap)
            result.append(tweetid)
            index-=1
            if index>=0:
                time,tweetid=self.tweets[user][index]
                heapq.heappush(heap,(-time,user,index,tweetid))
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
