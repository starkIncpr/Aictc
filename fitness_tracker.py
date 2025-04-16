class FitnessTracker:
    def __init__(self):
        self.parameters = {
            'age': 0,
            'bmi': 0,
            'duration': 0,
            'heart_rate': 0,
            'body_temp': 0,
            'gender_male': 1
        }
        
    def validate_input(self, value, min_val, max_val, param_name):
        try:
            value = float(value)
            if min_val <= value <= max_val:
                return True
            print(f"Error: {param_name} must be between {min_val} and {max_val}")
            return False
        except ValueError:
            print(f"Error: Please enter a valid number for {param_name}")
            return False

    def get_user_input(self):
        while True:
            try:
                print("\nEnter your fitness parameters:")
                age = input("Age (10-100): ")
                if not self.validate_input(age, 10, 100, "Age"): continue
                
                bmi = input("BMI (15-40): ")
                if not self.validate_input(bmi, 15, 40, "BMI"): continue
                
                duration = input("Duration in minutes (0-35): ")
                if not self.validate_input(duration, 0, 35, "Duration"): continue
                
                heart_rate = input("Heart Rate (60-130): ")
                if not self.validate_input(heart_rate, 60, 130, "Heart Rate"): continue
                
                body_temp = input("Body Temperature in Celsius (36-42): ")
                if not self.validate_input(body_temp, 36, 42, "Body Temperature"): continue
                
                gender = input("Gender (M/F): ").upper()
                if gender not in ['M', 'F']:
                    print("Error: Please enter M for Male or F for Female")
                    continue
                
                self.set_parameters(
                    float(age),
                    float(bmi),
                    float(duration),
                    float(heart_rate),
                    float(body_temp),
                    1 if gender == 'M' else 0
                )
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again.")

    def set_parameters(self, age, bmi, duration, heart_rate, body_temp, gender_male):
        self.parameters['age'] = age
        self.parameters['bmi'] = bmi
        self.parameters['duration'] = duration
        self.parameters['heart_rate'] = heart_rate
        self.parameters['body_temp'] = body_temp
        self.parameters['gender_male'] = gender_male

    def calculate_calories_burned(self):
        calories = (
            self.parameters['duration'] * 
            self.parameters['heart_rate'] * 
            0.1 * 
            (1 + (self.parameters['body_temp'] - 37) * 0.1)
        )
        return round(calories, 2)

    def display_results(self):
        print("\n" + "="*50)
        print("Personal Fitness Tracker Results".center(50))
        print("="*50)
        
        print("\nYour Parameters:")
        print("-"*20)
        for key, value in self.parameters.items():
            if key == 'gender_male':
                print(f"Gender: {'Male' if value == 1 else 'Female'}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nPrediction:")
        print("-"*20)
        print(f"Calories Burned: {self.calculate_calories_burned()} kcal")
        print("="*50)

if __name__ == "__main__":
    tracker = FitnessTracker()
    print("Welcome to Personal Fitness Tracker!")
    tracker.get_user_input()
    tracker.display_results()