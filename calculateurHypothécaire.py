

def calculateurIntérêt():
    
    PrixLogement = float(214000)#float(input("Entré le prix du logement (sans le signe de dollars)\n"))
    MiseDeFond = float(75000)#float(input("Entré la mise de fond (sans le signe de dollars)\n"))
    Hypothèque=(PrixLogement)-MiseDeFond
    HypothèqueDébut = Hypothèque
    intérêts = float(5.89)#float(input("Entré le pourcentage d'intérêts (sans le signe de %)\n"))
    intérêts /= 10
    ammortissement = int(25)#int(input("Entrez le nombre d'années d'ammortissement\n"))
    hydro = float(804)#float(input("Entrez les frais annuels d'hydro (sans le signee de dollars)\n"))
    taxes = float(2012)#float(input("Entrez les frais annuels de taxes (sans le signe de dollars)\n"))
    autres = float(1545)#float(input('''Entrez les frais annuels "autres" (sans le signee de dollars)\n'''))
    fraisAnnuelsHypothèque = (Hypothèque/25)
    FraisTotaux = (Hypothèque+(+hydro+taxes+autres)*ammortissement)

    print(f"............\n")
    print(f"Hypothèque = || {Hypothèque}$ ||\n")
    print(f"intérêt = || {intérêts}$ ||\n")
    print(f"ammortissement = || {ammortissement}$ ||\n")
    print(f"hydro = || {hydro}$ ||\n")
    print(f"taxes = || {taxes}$ ||\n")
    print(f"autres = || {autres}$ ||\n")
    

    
    sommeTotale = 0
    fraisAnnuels = (((Hypothèque/ammortissement)+hydro+taxes+autres))
    intérêtsTotale = 0

    print(f"Frais Annuels (sans les intérêts)  = || {fraisAnnuels}$ ||\n")
    print(f"Frais Mensuels (sans les intérêts)  = || {fraisAnnuels/12}$ ||\n")
    print(f".............\n")

    
    for i in range(ammortissement):
        print(f"====== Année {i+1} ======")
        intérêtsAnnuels = (Hypothèque*intérêts)/(ammortissement)
        print(f" IntérêtsAnnuels = || {intérêtsAnnuels}% ||\n")
        sommeTotale+=((fraisAnnuels)+intérêtsAnnuels)
        print(f" sommeTotale déboursé à date = || {sommeTotale}$ ||\n")
        FraisTotaux-=(fraisAnnuels)
        intérêtsTotale += intérêtsAnnuels
        Hypothèque-=(fraisAnnuelsHypothèque)
        print(f"Somme des intérêts payé à date = || {intérêtsTotale}$ ||")
        print(f"Les intérêts payés lors de l'année {i+1} = || {intérêtsAnnuels}$ ||")
        print(f"Les frais totaux lors de l'année {i+1} = || {(fraisAnnuels)+intérêtsAnnuels}$ ||")
        print(f"Frais restant à payer ((Hypothèque+intérêts Totaux) - montant payé) = || {FraisTotaux}$ ||")

    print(" ======== Résultats : ")
    print(f"Pour un immeuble de || {PrixLogement}$ || avec une mise de fond de || {MiseDeFond}$ ||:")
    print(f"L'hypothèque sera de || {HypothèqueDébut}$ ||")
    print(f"Les payements mensuels sans intérêts seraient d'une somme de ||{fraisAnnuels/12}$||")
    print(f"somme totale à rembourser (intérêt + Hypothèque) = || {sommeTotale}$ ||")
    print(f"somme totale des intérêts sur {ammortissement} ans d'ammortissement à rembourser = || {intérêtsTotale}$ ||")
    print("===========")

calculateurIntérêt()

