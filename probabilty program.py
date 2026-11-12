outcomes = ["H","T"]
total = len(outcomes)

def start_attributes():
    outcomes = "NA"
    if outcomes != "NA":
        total = len(outcomes)
    else:
        total = "Na"

    #keep get_ride_of
    rules = "NA"
    
    #[event1,event2,...]
    probablity_to_caculate = []

    return outcomes,total,rules,probablity_to_caculate,(outcomes == "NA" or rules == "NA" or probablity_to_caculate == [])

outcomes,total,rules,probablity_to_caculate,applicable = start_attributes()

    

def unique_out_comes(outcomes):
    unique = []
    for d in range(len(outcomes)):
        if outcomes[d] not in unique:
            unique.append(outcomes[d])
    return unique

def count_amount_outcomes(unique,outcomes):
    amounts = []
    for d in range(len(unique)):
        amounts.append(0)
        for dd in range(len(outcomes)):
            if unique[d] == outcomes[dd]:
                amounts[d] = amounts[d]+1
    return amounts

def probability_cacultor_outcomes(amounts,total):
    probablity = []
    for d in range(len(amounts)):
        probablity.append(amounts[d]/total)
    return probablity
def probability_of_each_outcome_alone(outcomes,total):
    unique = unique_out_comes(outcomes)
    print(unique)
    amounts = count_amount_outcomes(unique,outcomes)
    print(amounts)

    #caculates actuall proablity 
    return probability_cacultor_outcomes(amounts,total),unique,amounts

def linear_search(list,find):
    for d in range(len(list)):
        if list[d] == find:
            return d
    return d
def condisional_probablity_caculator(unique,probability,amounts,total):
    #keep get_ride_of
    rules = ""
    
    #[event1,event2,...]
    probablity_to_caculate = ["H"]
    probablity_currently = 1
    for d in range(len(probablity_to_caculate)):
        search = linear_search(unique,probablity_to_caculate[d])
        if search < len(unique):
            probablity_currently = probablity_currently*probability[search]
        else:
            probability = 0
            break

        if rules != "keep":
            amounts[search] = amounts[search]-1
            total = total - 1
            if total != 0:
                probability[search] = amounts[search]/total
            else:
                probability[search] = 0
    return probablity_currently

if (applicable == True):
    probablity,unique,amounts = probability_of_each_outcome_alone(outcomes,total)
    probability_of_event = condisional_probablity_caculator(unique,probablity,amounts,total)
    print(probability_of_event)
else:
    print("put somthing in start_attributes() line 4 of program")
    #search for this function in IDE
    #def start_attributes():