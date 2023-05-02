/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let f1 = 0, f2 = 1, t;

    while (true) {
        yield f1;

        t = f2;
        f2 += f1;
        f1 = t;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
