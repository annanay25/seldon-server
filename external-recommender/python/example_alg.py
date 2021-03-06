import random
import operator

def init(mc,config):
    global mc_pool
    mc_pool = mc


def get_recommendations(
        user_id,
        client,
        recent_interactions_list,
        data_set,
        limit
        ):

    scores = {}
    for i in data_set:
        scores[i]=random.uniform(0,1)

    sorted_scores=sorted(scores.items(), key=operator.itemgetter(1))
    sorted_scores = sorted_scores[::-1]
    top_scores = sorted_scores[0:limit]
    recs = dict(top_scores)

    return recs

