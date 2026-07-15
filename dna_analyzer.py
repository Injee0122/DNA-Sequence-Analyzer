def count_bases(dna):
    a = dna.count("A")
    t = dna.count("T")
    c = dna.count("C")
    g = dna.count("G")

    return {
        "A": a,
        "T": t,
        "C": c,
        "G": g
    }

def gc_content(dna):
    counts = count_bases(dna)
    gc_count = counts["G"] + counts["C"]
    gc_percentage = (gc_count / len(dna)) * 100
    return gc_percentage

def reverse_complement(dna):
    complement_sequence = ""

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    for base in dna:
        complement_sequence += complement[base]

    reverse_complement = complement_sequence[::-1]
    return reverse_complement

def main():
    dna = input("Enter DNA sequence: ")

    print("===== DNA Sequence Analyzer =====")
    print()

    print("Sequence: ")
    print(dna)
    print()

    print("Length: ")
    print(f"{len(dna)} bp")
    print()
    
    print("Base Counts:")
    print()
    counts = count_bases(dna)
    for base in counts:
        print(f"{base}: {counts[base]}")
    print()

    print("GC Content: ")
    print(f"{gc_content(dna):.2f}%")
    print()

    print("Reverse Complement: ")
    print(reverse_complement(dna))
    print()

main()