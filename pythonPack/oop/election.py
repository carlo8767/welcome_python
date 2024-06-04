import uuid


class Election:
    __vote = ""
    __ballot_paper = ""

    def __init__(self, vote, ballot_paper=uuid.uuid4()):
        self.__vote = vote
        self.__ballot_paper = ballot_paper


if __name__ == '__main__':
    object_election = Election("Australia")
    # THIS IS CALLED NAME MANGLING
    print(object_election._Election__vote)
