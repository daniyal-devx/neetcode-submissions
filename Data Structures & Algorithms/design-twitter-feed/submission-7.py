
class Twitter:

    def __init__(self):
        self.time = 0

        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=self.following[userId] | {userId}
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index=len(self.tweets[user])-1
                time, tweetId= self.tweets[user][index]
                heapq.heappush(heap,(-time,user,index,tweetId))
        result=[]
        while heap and len(result)<10:
            neg_time, user, index, tweetId=heapq.heappop(heap)
            result.append(tweetId)
            index-=1
            if index>=0:
                time,tweetId=self.tweets[user][index]
                heapq.heappush(heap,(-time,user,index,tweetId))
        return result

        