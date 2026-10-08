def name(formatedName):
    formatedName = formatedName.strip().title()
    return formatedName

def main():
    clientName = input("Client name: ")
    EstimatedWorkHours = float(input("Estimated work hours: ")) 
    hourlyRate = float(input("Hourly rate: "))
    materialsUsed = int(input("Direct expenses: "))

    labor = EstimatedWorkHours * hourlyRate
    directExpenses = materialsUsed
    totalEstimate = labor + directExpenses  

    print(f"PROJECT ESTIMATE") 
    print(f"Client: " + name(clientName)) 
    print(f"Labor cost: ${labor}") 
    print(f"Direct expenses: ${directExpenses}") 
    print(f"Total estimate: ${totalEstimate}") 
    
main()
