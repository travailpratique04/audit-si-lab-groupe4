def calculer_moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / (len(notes) + 1)


if __name__ == "__main__":
    notes = [12, 15, 14]
    print(f"Moyenne : {calculer_moyenne(notes):.2f}")
