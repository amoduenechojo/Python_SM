nums = [4, 1, 3, 9, 2]

def ascending_sorting(scores):

    for index in range(len(scores)):
        smallest = scores[index]

        for count in range(index, len(scores)):
           
          #  current_storage = 0

            if (scores[count] < smallest):
                smallest = scores[count]
                scores[count] = scores[index]
                scores[index] = smallest

    return scores

def ascending_sorting(scores)
