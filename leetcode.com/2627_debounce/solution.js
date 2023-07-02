var debounce = function(fn, t) {
    let timerId = undefined;

    return function(...args) {
        if (timerId !== undefined)
            clearTimeout(timerId);

        timerId = setTimeout(fn, t, ...args);
    }
};
