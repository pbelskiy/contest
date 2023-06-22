var expect = function(val) {
    return {
        toBe: function(n) {
            if (val === n)
                return true;
            throw "Not Equal";
        },
        notToBe: function(n) {
            if (val !== n)
                return true;
            throw "Equal";
        },
    }
};
