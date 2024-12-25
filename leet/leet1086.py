from collections import defaultdict
import heapq

def findTop5Averages(items): # O(n) due to default dict append
    """
    :param items:
    :return:
    """
    mapper = defaultdict(list)
    top_averages = defaultdict(list)

    for j in items:
        id = j[0]
        score = j[1]
        mapper[id].append(score)

    for key in mapper.keys():
            values = mapper.get(key)
            average = 0
            for value in values:
                average += value
            average = average/5
            top_averages[key].append(average)

    return top_averages

def findTop5Better(items): # O (n log (n)) due to sorted algo and default dict append
    """
    :param items:
    :return:
    """
    mapper = defaultdict(list)
    # Group scores by ID
    for id, score in items:
        mapper[id].append(score)

    # Calculate the average of the top 5 scores for each ID
    top_averages = {}
    for key, scores in mapper.items():
        # Sort scores in descending order and take the top 5
        top_5_scores = sorted(scores, reverse=True)[:5]
        # Calculate the average of the top 5 scores
        average = sum(top_5_scores) / len(top_5_scores)
        top_averages[key] = average

    return top_averages


# because of heap O (n log (k))
def findTop5Best(items):
    """
    Calculate the average of the top 5 scores for each ID in a faster way.
    :param items: List of [ID, score] pairs.
    :return: Dictionary mapping ID to the average of its top 5 scores.
    """
    mapper = defaultdict(list)

    # Group scores by ID
    for id, score in items:
        mapper[id].append(score)

    # Calculate the average of the top 5 scores for each ID
    top_averages = {}
    for key, scores in mapper.items():
        # Use heapq.nlargest to get the top 5 scores in O(n log k)
        top_5_scores = heapq.nlargest(5, scores)
        # Calculate the average of the top 5 scores
        average = sum(top_5_scores) / len(top_5_scores)
        top_averages[key] = average

    return sorted(top_averages.items())

items = [[1,92],[1,93],[1,94],[1,95],[1,100],[2,93],[2,94],[2,99],[2,100],[2,100]]

print(findTop5Averages(items)) # dont need default dict
print(findTop5Better(items)) # n lon(n) which is good
print(findTop5Best(items)) # n lon(k) due to heap