def name(formatedname):
    formatedname = formatedname.strip().title()
    return formatedname

def main():
    # input sends a prompt to the user and then waits for input, input goes into variable
    clientname = input("client name: ")

    # 
    estimateworkhours = float(input("estimated work hours: "))
    hourlyrate = float(input("hourly rate: "))
    material = int(input("direct expenses: "))

    labor = estimateworkhours * hourlyrate
    directexpenses = material
    totalestimate = labor + directexpenses

    print("project estimate")
    print("client:" + name(clientname))
    print(f"laborcost: ${labor}")
    print(f"direct expenses: ${directexpenses}")
    print(f"total estimate: ${totalestimate}")

main()
