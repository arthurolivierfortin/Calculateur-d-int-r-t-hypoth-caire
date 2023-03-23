

def calculateurIntérêt():
    PrixLogement = input("Entré le prix du logement (sans le signe de dollars)\n")
    MiseDeFond = input("Entré la mise de fond (sans le signe de dollars)\n")
    Hypothèque=(PrixLogement-MiseDeFond)
    print(f"Hypothèque = {Hypothèque}\n")
    intérêts = input("Entré le pourcentage d'intérêts (sans le signe de %)\n")
    ammortissement = input("Entrez le nombre d'années d'ammortissement\n")
    hydro = input("Entrez les frais annuels d'hydro (sans le signee de dollars)\n")
    taxes = input("Entrez les frais annuels de taxes (sans le signe de dollars)")
    autres = input('''Entrez les frais annuels "autres" (sans le signee de dollars)\n''')
    
    sommeTotale = 0
    fraisMensuel = (((Hypothèque/ammortissement)+hydro+taxes+autres)/12)
    intérêtsTotale = 0

    
    for i in range(ammortissement-1):
        print(f"====== Année {i+1} ======\n")
        intérêtsAnnuels = (Hypothèque*intérêts)
        sommeTotale+=((fraisMensuel*12)+intérêtsAnnuels)
        Hypothèque-=(Hypothèque-(fraisMensuel*12))
        intérêtsTotale += intérêtsAnnuels
        print(f"Les intérêts payés lors de la {i+1} années = {intérêtsAnnuels}")
        print(f"Les frais totaux lors de la {i+1} années = {(fraisMensuel*12)+intérêtsAnnuels}")

    print(f"somme totale à rembourser (intérêt + Hypothèque) = {sommeTotale}\n")
    print("===========")
    print(f"somme totale des intérêts sur {ammortissement} d'ammortissement à rembourser = {intérêtsTotale}\n")
    print("===========")

