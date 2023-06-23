var once = function(fn) {
    let called = false;
    return function(...args) {
        if (called === false) {
            called = true;
            return fn(...args);
        }

        return undefined;
    }
};
