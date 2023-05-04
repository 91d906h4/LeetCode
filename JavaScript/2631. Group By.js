/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    var result = new Object();

    this.forEach(element => {
      if (fn(element) in result) result[fn(element)].push(element);
      else result[fn(element)] = [element];
    });

    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
