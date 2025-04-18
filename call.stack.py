

def call_stack(value):

        if value > 0:
            call_stack(value - 1)  # CALLING THE STACK
            print(value)





if __name__ == "__main__":
    call_stack(10)