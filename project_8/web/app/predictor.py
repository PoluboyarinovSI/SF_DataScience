import numpy as np
import pickle

with open('./models/lfm_model.pkl', 'rb') as f:
    lfm_model = pickle.load(f)

with open('./models/item_id.pkl', 'rb') as f:
    item_sparse = pickle.load(f)
    
with open('./models/all_items.pkl', 'rb') as f:
    all_items = pickle.load(f)

with open('./models/all_users.pkl', 'rb') as f:
    all_users = pickle.load(f)

'''
def get_inner_model_visitorid(visitorid):
    return visitorid_mapping.get(visitorid)


def get_inner_model_itemid(itemid):
    return itemid_mapping.get(itemid)


def get_original_visitorid(inner_visitorid):
    return visitorid_labels.get(inner_visitorid)


def get_original_itemid(inner_itemid):
    return itemid_labels.get(inner_itemid)


def generate_top5_recommendations():
    pass
'''

def user_checker(visitorid):
    return visitorid in all_users


def get_predictions(visitorid):
    if not user_checker(visitorid):
        return []
    pred_scores = lfm_model.predict(visitorid, item_sparse)
    top_scores = np.argsort(-pred_scores)[:3]
    return all_items[top_scores]