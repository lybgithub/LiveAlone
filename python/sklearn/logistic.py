from gen_feat import make_train_set
from gen_feat import make_test_set
from gen_feat import get_labels_8
from sklearn.cross_validation import train_test_split
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier as gbdt
from sklearn.linear_model import LogisticRegression as lg
from gen_feat import report



def logistic_make_submission():
    train_start_date = '2016-03-10'
    train_end_date = '2016-04-11'
    test_start_date = '2016-04-11'
    test_end_date = '2016-04-16'

    sub_start_date = '2016-03-15'
    sub_end_date = '2016-04-16'

    user_index, training_data, label = make_train_set(train_start_date, train_end_date, test_start_date, test_end_date)
    X_train, X_test, y_train, y_test = train_test_split(training_data.values, label.values, test_size=0.2, random_state=0)


    clf = lg()  # 使用类，参数全是默认的  
    clf.fit(X_train,y_train)
    

    sub_user_index, sub_trainning_data = make_test_set(sub_start_date, sub_end_date)

    y_hat = clf.predict(sub_trainning_data)
    sub_user_index['label'] = y_hat
    pred = sub_user_index[sub_user_index['label'] == 1]
    pred = pred[['user_id', 'sku_id']]
    pred = pred.groupby('user_id').first().reset_index()
    pred['user_id'] = pred['user_id'].astype(int)
    pred.to_csv('../sub/submissionLOG508.csv', index=False, index_label=False)

def logistic_cv():
    train_start_date = '2016-03-05'
    train_end_date = '2016-04-06'
    test_start_date = '2016-04-06'
    test_end_date = '2016-04-11'

    sub_start_date = '2016-03-10'
    sub_end_date = '2016-04-11'
    sub_test_start_date = '2016-04-11'
    sub_test_end_date = '2016-04-16'

    user_index, training_data, label = make_train_set(train_start_date, train_end_date, test_start_date, test_end_date)
    X_train, X_test, y_train, y_test = train_test_split(training_data, label, test_size=0.2, random_state=0)

    clf = lg()
    clf.fit(X_train,y_train)
    
    sub_user_index, sub_trainning_date, sub_label = make_train_set(sub_start_date, sub_end_date,
                                                                   sub_test_start_date, sub_test_end_date)   # use this data to see the offline score
    
    test = sub_trainning_date.values    
    y = clf.predict(test)

    pred = sub_user_index.copy()
    y_true = get_labels_8(sub_test_start_date, sub_test_end_date)   # during the test date, real label for cate 8
    # y_true = sub_user_index.copy()
    pred['label'] = y    # add the new column which is the predict label for the test date

    ans = []
    for i in range(0,30):
        pred = sub_user_index.copy()
        pred['label'] = y
        pred = pred[pred.label >= i / 100]
        # print(pred)
        rep = report(pred, y_true)
        print('%s : score:%s' %(i/100,rep))
        ans.append([i / 100, rep])

    print('ans:%s' %ans)

    threshold = sorted(ans, key=getKey, reverse=True)[0][0]
    bestscore = sorted(ans, key=getKey, reverse=True)[0][1]
    print('best threshold:%s' % threshold)
    print('best score:%s' % bestscore)