import numpy as np
import pickle

with open('./models/lightfm_model.pickle', 'rb') as f:
    model = pickle.load(f)

with open('./models/sparse_user_item.pickle', 'rb') as f:
    user_item_sparse_data = pickle.load(f)

visitorid_mapping, _, itemid_mapping, _ = dataset_mapping
visitorid_labels = {v: k for k, v in visitorid_mapping.items()}
itemid_labels = {v: k for k, v in itemid_mapping.items()}


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


def predict(visitorid):
    inner_model_visitorid = get_inner_model_visitorid(visitorid)
    if not inner_model_visitorid:
        return []
    pred_scores = model.predict(inner_model_visitorid, np.arange(len(itemid_mapping)))
    top_scores = np.argsort(-pred_scores)[:3]
    return [itemid_labels[k] for k in top_scores]


def check_visitor(visitorid):
    return visitorid_mapping.get(visitorid, False) != False