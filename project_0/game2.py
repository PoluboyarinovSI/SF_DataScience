import numpy as np
    
def random_preidct(number:int=1) -> int:
    """Randomly number predictor

    Args:
       number (int, optional): Number ti predict. Defaults to 1.

    Returns:
        int: Attempts number
    """
    count = 0
        
    while True:
        count += 1
        predict_number = np.random.randint(1, 100)
        if number == predict_number:
            break
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
    print(f'Mean attempts to pretict numeber: {score}')


if __name__ == '__main__':
    score_game(random_preidct)