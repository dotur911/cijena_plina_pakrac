def calculate_pay_value():
    difference = float(input("Unesi potrošenu kubikažu plina: "))
    
    # Given data
    pay_value_for_156 = 73.38
    difference_for_156 = 156
    
    # Calculate the proportional increase
    proportional_increase = pay_value_for_156 / difference_for_156
    
    # Calculate pay value for the entered difference
    pay_value = proportional_increase * difference
    
    print(f"Navedeni iznos za platiti trebao bi bit:{pay_value:.2f} EUR")

if __name__ == "__main__":
    calculate_pay_value()
    input("Press Enter to close...")
