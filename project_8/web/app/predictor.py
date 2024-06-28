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


def user_checker(visitorid):
    return visitorid in all_users


def get_predictions(visitorid):
    if not user_checker(visitorid):
        return []
    pred_scores = lfm_model.predict(visitorid, item_sparse)
    top_scores = np.argsort(-pred_scores)[:3]
    return all_items[top_scores]

