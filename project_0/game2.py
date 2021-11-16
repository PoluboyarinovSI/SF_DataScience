import numpy as np
    
def random_predict(number:int=1) -> int:
    """Randomly number predictor

    Args:
       number (int, optional): Number to predict. Defaults to 1.

    Returns:
        int: Attempts number
    """

    first_attempt = 50
    count = 1
    
    if number==first_attempt:
        return count
    predict_number = first_attempt
      
    if number<predict_number:  
        left_border = 0
        right_border = 50
    else:
        left_border = 50
        right_border = 100

    while True:
        if number==predict_number:
            break
        if number<predict_number:
            right_border = predict_number
            predict_number = left_border + (right_border-left_border)//2
            count += 1
        else:
            left_border = predict_number
            predict_number = left_border + (right_border-left_border)//2
            count += 1
    return count
    
def score_game(random_predict) -> int:
    """Mean attempts to predict

    Args:
        random_predict ([type]): predict function

    Returns:
        int: Mean attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(10)) # list of numbers
        
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Mean attempts to predict number: {score}')


if __name__ == '__main__':
    score_game(random_predict)