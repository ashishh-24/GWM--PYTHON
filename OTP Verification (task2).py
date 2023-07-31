import random

def generate_otp():
  """Generates a 6-digit OTP."""
  otp = ""
  for i in range(6):
    otp += str(random.randint(0, 9))
  return otp

def verify_otp(otp, entered_otp):
  """Verifies the OTP entered by the user."""
  if otp == entered_otp:
    return True
  else:
    return False

def main():
  """Generates an OTP and verifies it."""
  otp = generate_otp()
  print("The OTP is:", otp)
  entered_otp = input("Enter the OTP: ")
  if verify_otp(otp, entered_otp):
    print("OTP verified successfully!")
  else:
    print("OTP verification failed.")

if __name__ == "__main__":
  main()
