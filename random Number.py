import random

def guessing_game():
    print("مرحبًا بك في لعبة التخمين! سيقوم الكمبيوتر باختيار رقم بين 1 و100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("أدخل تخمينك: "))
            attempts += 1
            if guess < secret_number:
                print("الرقم أعلى من ذلك! حاول مرة أخرى.")
            elif guess > secret_number:
                print("الرقم أقل من ذلك! حاول مرة أخرى.")
            else:
                print(f"تهانينا! لقد خمنت الرقم الصحيح وهو {secret_number} بعد {attempts} محاولة.")
                break
        except ValueError:
            print("يرجى إدخال رقم صالح.")
            
guessing_game()
