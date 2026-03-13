import random
import time

# --- DATA STORAGE ---

# The first list stores the names of our infrastructure components.
# The second list stores the corresponding safety limits (thresholds) for each.
resource_names = ["web-server-01", "primary-db", "auth-service"]
error_thresholds = [75, 90, 85]

def run_monitoring_cycle():
    """
    This function performs a single check of all resources. 
    It loops through the lists and compares live data against safety limits.
    """
    
    print("\n--- New Monitoring Interval ---")
    
    # We use a 'for' loop to iterate through the resources.

    for i in range(len(resource_names)):
        
        # Pull the specific name and limit for the current item in the loop
        name = resource_names[i]
        limit = error_thresholds[i]
        
        # Use the random library to generate a fake 'load' percentage (10.0 to 100.0)
        # round(..., 2) keeps the number clean with only two decimal places.
        current_load = round(random.uniform(10.0, 100.0), 2)
        
        # Conditional Logic: Check if the current load is higher than the allowed limit.
        if current_load > limit:
            # If the load is too high, print a critical alert message
            print(f"!! CRITICAL !! {name} is at {current_load}% (Limit: {limit}%)")
        else:
            # If the load is within safe bounds, print an 'OK' status message
            print(f"OK - {name} is stable at {current_load}%")

# --- MAIN EXECUTION ---
# This block tells Python to start running the code from here.
if __name__ == "__main__":
    print("=== Sentinel Infrastructure Monitoring Initialized ===")
    
    # runs monitoring cycle 3 times to simulate continuous tracking.
    for _ in range(3):
        run_monitoring_cycle()
        
        # Pause the script for 1 second between cycles to simulate a real-world delay.
        time.sleep(1) 

    print("\nMonitoring session complete.")