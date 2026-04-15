def run_finite_automation():
    # -------------------------------
    # STEP 1: INPUT STATES
    # -------------------------------
    
    # Ask user how many states the automaton has
    num_states = int(input("Enter number of states: "))
    
    # Take names of all states (like q0, q1, q2...)
    states = [input(f"Enter name of state {i+1}: ") for i in range(num_states)]

    # -------------------------------
    # STEP 2: INPUT ALPHABET
    # -------------------------------
    
    # Input symbols (like 0 1 or a b)
    alphabet = input("Enter input symbols (space separated): ").split()

    # -------------------------------
    # STEP 3: INPUT TRANSITIONS
    # -------------------------------
    
    print("\nEnter transitions:")
    print("Format: current_state symbol next_state")
    
    # Dictionary to store transitions
    # Key: (current_state, symbol)
    # Value: next_state
    transitions = {}

    # Loop through each state and each symbol
    for state in states:
        for symbol in alphabet:
            # Ask user where to go from (state, symbol)
            next_state = input(f"({state}, {symbol}) = ")
            
            # Store the transition in dictionary
            transitions[(state, symbol)] = next_state

    # -------------------------------
    # STEP 4: INPUT START STATE
    # -------------------------------
    
    start_state = input("Enter start state: ")
    
    # Check if start state is valid
    if start_state not in states:
        print("Invalid start state!")
        return   # Stop execution if invalid

    # -------------------------------
    # STEP 5: INPUT FINAL STATES
    # -------------------------------
    
    # Accepting states (can be multiple)
    final_states = input("Enter final accepting states (space separated): ").split()

    # Validate final states
    for f in final_states:
        if f not in states:
            print(f"Invalid final state: {f}")
            return   # Stop execution if invalid

    # -------------------------------
    # STEP 6: INPUT STRING
    # -------------------------------
    
    # Input string without spaces (example: 10101)
    input_string = input("Enter input string (symbols without spaces): ")

    # -------------------------------
    # STEP 7: SIMULATION (CORE LOGIC)
    # -------------------------------
    
    # Start from initial state
    current_state = start_state

    # Process each symbol in the input string
    for symbol in input_string:
        
        # Check if transition exists
        if (current_state, symbol) not in transitions:
            print(f"Invalid transition from state {current_state} with symbol '{symbol}'")
            return   # Stop if no valid transition
        
        # Move to the next state
        current_state = transitions[(current_state, symbol)]

    # -------------------------------
    # STEP 8: CHECK ACCEPTANCE
    # -------------------------------
    
    # If final state is one of the accepting states
    if current_state in final_states:
        print("String accepted ")
    else:
        print("String rejected ")

# -------------------------------
# RUN THE PROGRAM
# -------------------------------

run_finite_automation()
