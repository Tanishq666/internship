import random as r
import smtplib


def generate_otp():
    return str(r.randint(100000, 999999))


def send_email(receiver_mail, otp):
    my_email = "dropamessage941@gmail.com"
    password = "arqvbxsoietnqnuw"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_mail,
            msg=f"{otp}"
        )


def main():
    otp = generate_otp()

    receiver_mail = input("Enter your email address: ")
    send_email(receiver_mail, otp)
    print("OTP sent to your email address")

    user_otp = input("Enter the OTP received in your email: ")

    if user_otp == otp:
        print("OTP verification Successful")
    else:
        print("Incorrect OTP")


if __name__ == "__main__":
    main()
