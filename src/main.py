from rebase import ModelChain, node
import pandas as pd
import lightgbm as lgb


@node(inputs=['train_set', 'params'], outputs=['model', 'metrics'])
def train(train_set, params):
    print(train_set)
    df_X = train_set.drop(columns=['target'])
    df_y = train_set['target']
    lgb_trainset = lgb.Dataset(df_X, label=df_y)
    valid_sets = [lgb_trainset]
    valid_names = ['train']
    gbm = lgb.train(
        params, 
        lgb_trainset,
        valid_sets=valid_sets,
        valid_names=valid_names,
    )
    return [
        gbm,
        {'score': 1337}
    ]


@node(inputs=['model', 'val_x'], outputs='result')
def predict(model, val_x):
    val_x['target'] = model.predict(val_x)
    return val_x


def init():
    return dict(
        train=[train],
        infer=[predict]
    )

