def main():
    import pandas as pd
    import requests

    url = " http://demo7351102.mockable.io/march17"
    responce = requests.get(url)
    print(responce)
    prize = responce.json()
    value = pd.DataFrame(prize)
    print(value)

    value.to_csv("Fruits_Prize.csv")
main()
choose = int(input("Enter Number: "))
if choose == 0:
    print("Thanks for choosing the apple")
    Quantity = int(input("Enter the quantity: \n"))
    GST = "18%"
    total_bill_of_apple = Quantity*50
    GST_BILL = total_bill_of_apple*0.18
    Gross_total = total_bill_of_apple + (total_bill_of_apple*0.18)
    print(f"GST on apple {GST_BILL}")
    print(f"You selected {Quantity} apple your bill is {Gross_total}")
elif choose == 1:
    print("Thanks for choosing the kiwi")
    Quantity = int(input("Enter the quantity: \n"))
    GST = "18%"
    total_bill_of_kiwi = Quantity*60
    GST_BILL = total_bill_of_kiwi*0.18
    print(f"GST on kiwi {GST_BILL}")
    Gross_total = total_bill_of_kiwi + (total_bill_of_kiwi*0.18)
    print(f"You selected {Quantity} kiwi your bill is {Gross_total}")
elif choose == 2:
    print("Thanks for choosing the orange")
    Quantity = int(input("Enter the quantity: \n"))
    GST = "18%"
    total_bill_of_orange = Quantity*40
    GST_BILL = total_bill_of_orange*0.18
    print(f"GST on orange {GST_BILL}")
    Gross_total = total_bill_of_orange + (total_bill_of_orange*0.18)
    print(f"You selected {Quantity} orange your bill is {Gross_total}")
elif choose == 3:
    print("Thanks for choosing the banana")
    Quantity = int(input("Enter the quantity: \n"))
    GST = "18%"
    total_bill_of_banana = Quantity*20
    GST_BILL = total_bill_of_banana*0.18
    print(f"GST on banana {GST_BILL}")
    Gross_total = total_bill_of_banana + (total_bill_of_banana*0.18)
    print(f"You selected {Quantity} banana your bill is {Gross_total}")
elif choose == 4:
    print("Thanks for choosing the jackfruit")
    Quantity = int(input("Enter the quantity: \n"))
    GST = "18%"
    total_bill_of_jackfruit = Quantity*50
    GST_BILL = total_bill_of_jackfruit*0.18
    print(f"GST on jackfruit {GST_BILL}")
    Gross_total = total_bill_of_jackfruit + (total_bill_of_jackfruit*0.18)
    print(f"You selected {Quantity} jackfruit your bill is {Gross_total}")
else:
    print("Please enter appropriate number")
