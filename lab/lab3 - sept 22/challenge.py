from time import *

# mod_day = time() // (1 * 24 * 60 * 60) ---this means the amount of time in seconds that has passed since 1970, January 1

mod_day = (time() - (5 * 60 * 60)) % (1 * 24 * 60 * 60) # remaining time in seconds of a day

print(f"{mod_day} is the remaining amount of time in seconds for today")

hours = mod_day  // 60 // 60
minutes = mod_day // 60 % 60

print(f"current time in 24 hrs format is {hours:.0f}:{minutes:.0f}")


print(f"1 day = 24 hours = {24 * 60} minutes = {24 * 60 * 60} seconds")