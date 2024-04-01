[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/iczLm4Qi)
# I. Sárkány 

A bineáris keresés átismétlése a sárkányos feladaton keresztül. Mindenki talál a tasks mappában egy dragon
nevű fájlt, amiben ki kell javítani egy függvényt.

Ez a függvény picit eltér az órán felvázolt struktúrától. Itt már nem egy lista lesz a függvényetek paramétere, hanem egy is_dead függvény, amit nem nektek kell megírnotok. Ezt majd a tesztelő függvény adja meg. Nektek csak annyira kell használnotok, hogyha meghívjátok ezt a függvényt egy adott számmal, akkor az visszaadja, hogy az adott számú tehén halott e. **Figyeljetek, hogy itt fordul a logika az előzőhöz képest! Akkor kaptok igaz értéket visszatérési értékként, ha a tehén halott.** A másik paraméteretek pedig a tehenek száma. Nyugodtan keressetek minket, ha nem megy valami!

### parameters:

- is_dead: function

    it takes an integer parameter of the cows rank in the weight contest and returns a boolean value of whether a cow is dead or not

- number_of_cows: int

    the number of cows in the kingdom

### returns:

an integer, the rank of the largest (the one with the smallest rank) cow that is alive

and it checks the least amount of cows possible


# II. Tojás

Van két tojásunk és egy 100 emeletes épület. Meg kell mondanunk, hogy mi az a legmagasabb szint, ahonnan leejtve még nem törik össze egy tojás. Ha már az első emeletről leesve összetörik a tojás akkor 0-t ad vissza, ha a 100. emeletről ledobva sem törik össze akkor pedig 100-at. 

Ennél a feladatnál már találtok egy működő megoldást az eggs fájlban. Ennél egy jobb megoldást kellene írnotok. Annál jobb egy megoldás minél alacsonyabb a tesztnél kiírt **mean performance** értéke. Azaz átlagosan kevesebb dobás kell, hogy megtalálja a jó megoldást. Itt is van egy paraméter, ami egy függvény a breaks. Amikor ezt meghívjátok a függvényetekben az számít egy dobásnak. A teszt futásakor ez adja vissza, hogy eltörik e egy tojás egy adott emeleten vagy nem.

### parameters:

- breaks: function

    it takes an integer parameter of the floor number and returns a boolean value of whether the egg breaks or not

###  returns:

an integer, the number of the highest floor where the egg doesn’t break

# III. GitHub

Olvassátok át [ezt](./GitHub_summary.md) a rövid összefoglalót.

