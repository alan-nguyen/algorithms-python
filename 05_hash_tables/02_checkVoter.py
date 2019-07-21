voted = {}
def checkVoter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


# test case
checkVoter("Alex")  # Should be "let them vote!"
checkVoter("Emily")  # Should be "let them vote!"
checkVoter("Alex")  #  Should be "kick them out!"