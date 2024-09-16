#Constants
INITIAL_REWARD = 50 #initial reward per block 
MAX_BTC = 21_000_000 #maximun supply BTC
BLOCKS_PER_HALVING = 210_000 #block per halving
MAX_HALVING=32 #number of halvings

#Calculate the total supply using the equation
def calculate_total_supply(halving):
    return BLOCKS_PER_HALVING*INITIAL_REWARD / (2**halving)

#Calculate the block reward in SATS
def calculate_block_reward_sats(halving):
    block_reward= INITIAL_REWARD / (2**halving)
    return block_reward * 100_000_000

#Calculate the percentage mined
def calculate_percentage_mined(total_supply):
    return (total_supply/MAX_BTC)*100

#Display the total BTC supply, block reward and percentage 
def show_results():
    total_supply=0  #Accumulated total supply
    i=0 #Counter for the number of halving
    while i <= MAX_HALVING:
        btc_mint = calculate_total_supply(i) #Call the function
        block_reward_sats = calculate_block_reward_sats(i) #Call the function

        total_supply += btc_mint

        percentage = calculate_percentage_mined(total_supply) #Call the function

        #print the results
        print(f"Halving {i}:")
        print(f"  Total supply: {total_supply:.8f} BTC")
        print(f"  Block reward: {block_reward_sats:.0f} SATS")
        print(f"  Percentage mined: {percentage:.2f}%\n")

        #halving counter
        i += 1


#call de function to display the results
show_results()