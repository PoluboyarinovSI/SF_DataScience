import numpy as np
    
def random_preidct(number:int=1) -> int:
    """Randomly number predictor

    Args:
       number (int, optional): Number to predict. Defaults to 1.

    Returns:
        int: Attempts number
    """
    predict_number = np.random.randint(1, 100)
    count = 1
        
    while True:
        count += 1
        if number == predict_number:
            break
        elif number < predict_number:
            predict_number = np.random.randint(number, predict_number)
        elif number > predict_number:
            predict_number = np.random.randint(predict_number+1, number+1)
    return count
    
def score_game(random_preidct) -> int:
    """Mean attempts to predict

    Args:
        random_preidct ([type]): predict function

    Returns:
        int: Mean attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000)) # list of numbers
        
    for number in random_array:
        count_ls.append(random_preidct(number))
        
    score = int(np.mean(count_ls))
    print(f'Mean attempts to predict numeber: {score}')


if __name__ == '__main__':
    score_game(random_preidct)