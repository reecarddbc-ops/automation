#A DFA has exactly ONE path for every input.
def run_dfa():
    # -------------------------------
    # STEP 1: INPUT STATES
    # -------------------------------
    
    # Number of states
    num_states = int(input("Enter the number of states: "))
    
    # Store state names in a list
    states = []
    for i in range(num_states):
        states.append(input(f"Enter the name of state {i+1}: "))

    # -------------------------------
    # STEP 2: INPUT ALPHABET
    # -------------------------------
    
    # Input symbols (like 0 1 or a b)
    alphabet = input("Enter the input symbols (separated by spaces): ").split()
    
    # -------------------------------
    # STEP 3: INPUT TRANSITIONS
    # -------------------------------
    
    print("\nEnter transitions:")
    print("Format: exactly one next state")
    print("Press Enter if no transition (acts as a dead state)")
    
    # Dictionary to store transitions
    # Key: (current_state, symbol)
    # Value: next_state (single state for DFA)
    transitions = {}

    for state in states:
        for symbol in alphabet:
            # Take next state input
            next_state = input(f"({state}, {symbol}) = ").strip()
            
            # If user presses Enter, empty string "" is stored
            # This represents NO transition (dead state)
            transitions[(state, symbol)] = next_state 

    # -------------------------------
    # STEP 4: INPUT START STATE
    # -------------------------------
    
    start_state = input("Enter start state: ").strip()

    # -------------------------------
    # STEP 5: INPUT FINAL STATES
    # -------------------------------
    
    final_states = input("Enter final accepting states (space separated): ").split()

    # -------------------------------
    # STEP 6: INPUT STRING
    # -------------------------------
    
    input_string = input("\nEnter the input string: ").strip()

    # -------------------------------
    # STEP 7: DFA SIMULATION
    # -------------------------------
    
    # DFA always has ONE current state
    current_state = start_state

    # Process each symbol one by one
    for symbol in input_string:
        
        # Check if transition exists AND is not empty
        if (current_state, symbol) in transitions and transitions[(current_state, symbol)] != "":
            
            # Move to next state
            current_state = transitions[(current_state, symbol)]
        
        else:
            # No valid transition → goes to dead state → reject
            print("\nString is Rejected")
            return

    # -------------------------------
    # STEP 8: FINAL CHECK
    # -------------------------------
    
    # If ending state is an accepting state → accept
    if current_state in final_states:
        print("\nString is Accepted")
    else:
        print("\nString is Rejected")


# -------------------------------
# RUN FUNCTION
# -------------------------------
run_dfa()
