/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    var morse = {"a" : ".-",
                 "b" : "-...",
                 "c" : "-.-.",
                 "d" : "-..",
                 "e" : ".",
                 "f" : "..-.",
                 "g" : "--.",
                 "h" : "....",
                 "i" : "..",
                 "j" : ".---",
                 "k" : "-.-",
                 "l" : ".-..",
                 "m" : "--",
                 "n" : "-.",
                 "o" : "---",
                 "p" : ".--.",
                 "q" : "--.-",
                 "r" : ".-.",
                 "s" : "...",
                 "t" : "-",
                 "u" : "..-",
                 "v" : "...-",
                 "w" : ".--",
                 "x" : "-..-",
                 "y" : "-.--",
                 "z" : "--.."};
    var a = [];
    var c = 0;
    words.forEach(elementa => {
        var b = "";
        elementa.split("").forEach(elementb => {
            b += morse[elementb];
        });
        console.log(b);
        if(!a.includes(b)){
            a.push(b);
            c++;
        }
    });
    return c;
};
