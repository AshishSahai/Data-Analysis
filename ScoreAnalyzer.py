scores=[]
while True:
    user_input=input("Enter score (or type 'done'): ")
    if user_input.lower()=="done":
        break
    try:
        score= int(user_input)
        if score <0:
            print("scores cannot be negative. try again")
            continue
        scores.append(score)

    except ValueError:
        print("Enter valid input")

if not scores:
    print("No valid inputs from the user. Exiting program")
    exit()

maximum_score:int=max(scores)
minimum_score:int=min(scores)
sum_of_scores= sum(scores)


average_score=sum_of_scores/len(scores)
filename ="score_results.txt"
with open(filename, "w") as file:

    file.write("=== Results===\n")
    file.write("==Score Summary==\n")
    file.write(f"\n Highest Score : {maximum_score}")
    file.write(f"\n Lowest Score : {minimum_score}")
    file.write(f"\n Sum of Scores : {sum_of_scores}")
    file.write(f"\n Average Score : {average_score:.2f}")

    above_average_count=sum(1 for score in scores if score>average_score)

    file.write(f"\n Above Average Count : {above_average_count}")


print(f"\n Result saved to : {filename}")



