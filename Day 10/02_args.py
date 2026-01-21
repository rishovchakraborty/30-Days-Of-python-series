# Arbitrary Number of Arguments

# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.


def sum(*args):
    total=0
    for arg in args:
        total += arg
    return total

print(sum(2,4,6))
print(sum(2,4,4,6,6))
print(sum(2,4,6,0,2,6,8))

# default and arbitary
def group(team,*team_mates):
    print(f"the team members of group : {team} are")
    for i in team_mates:
        print(i)

group('india','virat','rohit','rahul')