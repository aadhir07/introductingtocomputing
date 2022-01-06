#program to compute income tax

#assigning constants first


inc=float(input("Enter your gross income in dollars: "))
dep=int(input("Enter total dependents: "))

inc_tax=(inc-10000-(dep*3000))


final_tax=inc_tax*0.2
final_tax=round(final_tax,2)

if final_tax<0:
    final_tax=0

else:
    final_tax=final_tax


print("Your income tax is: ", final_tax)   


