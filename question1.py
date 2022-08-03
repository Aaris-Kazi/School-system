def give_remainder_dict(divided, divisor, number):
    remainder = divided/divisor
    n = str(number)
    a = "{:."+n+"f}"
    # print(a.format(remainder))
    x = a.format(remainder)
    x = str(x).split('.')
    # x = str(x[1])
    answers = []
    for i in range(0,10):
        answers.append(x[1].count(str(i)))
    print({1:  answers[1],2:  answers[2],3:  answers[3],4:  answers[4],5:  answers[5],6:  answers[6],7:  answers[7],8:  answers[8],9:  answers[9], 0: answers[0]})
    print('\n')
    


give_remainder_dict(22, 7, 10)
give_remainder_dict(22, 7, 100)
give_remainder_dict(27, 5, 25)
give_remainder_dict(1,3,33)
give_remainder_dict(100, 25, 4)

# {1: 2, 2: 2, 3: 0, 4: 2, 5: 1, 6: 0, 7: 1, 8: 1, 9: 1, 0: 0}
# {1:2, 2:2, 3:0, 4:2, 5:1, 6:0, 7:1, 8:2, 9:0, 0:0}