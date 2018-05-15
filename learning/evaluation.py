from sklearn import metrics


def count_accuracy(prediction, target):
    f = count_accuracy_metrics(prediction.food_matrix, target.food_matrix)
    p = count_accuracy_metrics(prediction.price_matrix, target.price_matrix)
    s = count_accuracy_metrics(prediction.service_matrix, target.service_matrix)
    a = count_accuracy_metrics(prediction.ambience_matrix, target.ambience_matrix)
    return (f,p,s,a)

def count_accuracy_metrics(pred, target):
    return metrics.confusion_matrix(target, pred, labels=[-1, 0, 1])

def count_accuracy_score_metrics(pred, target):
    return metrics.accuracy_score(target, pred)

def count_accuracy_score(prediction, target):
    f = count_accuracy_score_metrics(prediction.food_matrix, target.food_matrix)
    p = count_accuracy_score_metrics(prediction.price_matrix, target.price_matrix)
    s = count_accuracy_score_metrics(prediction.service_matrix, target.service_matrix)
    a = count_accuracy_score_metrics(prediction.ambience_matrix, target.ambience_matrix)
    return (f,p,s,a)