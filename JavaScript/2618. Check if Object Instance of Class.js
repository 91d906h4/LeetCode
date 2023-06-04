/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj == null || obj == undefined || typeof classFunction !== "function") return false;

    if (typeof obj !== "Object") obj = Object(obj);

    return obj instanceof classFunction;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
