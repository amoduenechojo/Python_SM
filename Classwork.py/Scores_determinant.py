no_of_passes = 0
no_of_fails = 0

for number in range(1,16):
    Scores_determinant = int(input("Enter a score: "))

    if Scores_determinant > 45:
            no_of_passes += 1
        print("passed", no_of_passes)

    else: 
            no_of_fails += 1

print("passed",  no_of_passes)
print("failed", no_of_fails)



