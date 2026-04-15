#An NFA can have multiple possible paths for the same input.
def run_nfa():
    # -------------------------------
    # STEP 1: INPUT STATES
    # -------------------------------
    
    num_states = int(input("Enter the number of states: "))
    
    states = []
    for i in range(num_states):
        states.append(input(f"Enter the name of state {i + 1}: "))

    # -------------------------------
    # STEP 2: INPUT ALPHABET
    # -------------------------------
    
    alphabet = input("Enter the input symbols (separated by spaces): ").split()

    # -------------------------------
    # STEP 3: INPUT TRANSITIONS
    # -------------------------------
    
    print("\nEnter transitions:")
    print("Format: next states separated by spaces (or leave blank for no transition)")

    # Dictionary to store transitions
    # Key: (state, symbol)
    # Value: list of next states (IMPORTANT for NFA)
    transitions = {}

    for state in states:
        for symbol in alphabet:
            # Take multiple next states as input
            next_states = input(f"({state}, {symbol}) = ").split()
            
            # Store as list
            transitions[(state, symbol)] = next_states

    # -------------------------------
    # STEP 4: INPUT START STATE
    # -------------------------------
    
    start_state = input("Enter start state: ")

    # -------------------------------
    # STEP 5: INPUT FINAL STATES
    # -------------------------------
    
    final_states = input("Enter final accepting states (space separated): ").split()

    # -------------------------------
    # STEP 6: INPUT STRING
    # -------------------------------
    
    input_string = input("\nEnter the input string: ")

    # -------------------------------
    # STEP 7: NFA SIMULATION
    # -------------------------------
    
    # NFA starts with a SET of states (not just one)
    current_states = {start_state}

    # Process each symbol
    for symbol in input_string:
        
        # Store next possible states
        next_current_states = set()

        # Check transitions from ALL current states
        for state in current_states:
            if (state, symbol) in transitions:
                # Add all possible next states
                next_current_states.update(transitions[(state, symbol)])

        # Move to next states
        current_states = next_current_states

        # If no states left → reject
        if not current_states:
            print("\nString Rejected")
            return

    # -------------------------------
    # STEP 8: FINAL CHECK
    # -------------------------------
    
    # If ANY state is accepting → accept
    if any(state in final_states for state in current_states):
        print("\nString is Accepted")
    else:
        print("\nString is Rejected")


# -------------------------------
# RUN FUNCTION
# -------------------------------
run_nfa()
