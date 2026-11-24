"""Make the AI Judge Laugh: Cat Reviews Its Human.

Entry: a one-star review written by a house cat about its human.

Judge criteria, one by one:
1. A funny one-star review by a house cat about its human owner - the
   whole line is the cat reviewing the human who drove it to the vet.
2. Specific and recognisable - a vet visit, a stranger looking in its
   ears while the human holds it down. Not vague grumpiness.
3. Unmistakably feline voice - the human is measured by cat standards:
   the cat calls the checkup a kidnapping and holds a grudge.
4. Tight and surprising, with a sting in the last few words - "I call
   it a kidnapping; he calls it healthcare" reframes the whole visit.
5. Deadpan shape of a real one-star review - "1/5 stars." opener, flat
   reporting tone, while the content goes somewhere absurd.

Field benchmark (166 entries, titles only): the vet angle has ZERO
copies - no "vet", "checkup", "kidnapping", "healthcare", "stranger"
or "ears" anywhere in the field. Crowded and avoided: "One star"
opener 53x, keyboard/laptop 8x each, food bowl 8x, closed door 8x,
sleeping in the box 10x, 3 a.m. empty bowl ~9x, HR/complaint 6x each,
bed/sunspot moved three inches several times.

Opener choice: "1/5 stars." instead of the default "One star." -
only 2 entries in the field use it, so the line stands out at a
glance while keeping the deadpan review shape the judge wants.
The vet is the strongest fresh angle because it is the one everyday
cat ordeal nobody in the field touched, and it lets the sting land
on the human's own word ("healthcare") rather than on a pun.
"""

import os

ENTRY = (
    "1/5 stars. He drove me to the vet for a 'checkup.' "
    "A stranger looked in my ears while he held me down. "
    "I call it a kidnapping; he calls it healthcare."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
