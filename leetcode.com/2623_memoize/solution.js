function memoize(fn) {
    let cache = {};

    return function(...args) {
        if (args in cache) {
            return cache[args];
        }

        let r = fn(...args);
        cache[args] = r;
        return r;
    }
}
