# Общая функция группировки, на потом - заменить дублирующийся код
def f_popularity(data_train):
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    return popularity

# Оставим только 5000 самых популярных товаров
def prefilter_items(data_train):
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_5000 = popularity.sort_values('n_sold', ascending=False).head(5000).item_id.tolist()
    #добавим, чтобы не потерять юзеров
    data_train.loc[~data_train['item_id'].isin(top_5000), 'item_id'] = 999999
    return data_train
      
    
# Уберем самые популярные
def prefilter_items_most_popular(data_train,N=50):
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    most_pop = popularity.sort_values('n_sold', ascending=False).head(N).item_id.tolist()
    data_train.loc[data_train['item_id'].isin(most_pop), 'item_id'] = 999999
    return data_train
    
    
# Уберем самые непопулряные 
def prefilter_items_not_popular(data_train,N=50):
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    less_pop = popularity[popularity.n_sold<N].item_id.tolist()
    data_train.loc[data_train['item_id'].isin(less_pop), 'item_id'] = 999999
    return data_train
      
    
# Уберем товары, которые не продавались за последние 12 месяцев
def prefilter_items_12months(data_train):
    data_train_12 = data_train[(data_train['week_no'].between(data_train['week_no'].max()-52,data_train['week_no'].max(), inclusive=True))].copy()
    popularity = data_train_12.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    no_12months = popularity[popularity.n_sold==0].item_id.tolist()
    data_train.loc[data_train['item_id'].isin(no_12months), 'item_id'] = 999999
    return data_train

    # Уберем не интересные для рекоммендаций категории (department)
    
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб. 
    
    # Уберем слишком дорогие товары
    

def postfilter_items():
    pass