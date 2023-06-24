var cancellable = function(fn, args, t) {
    fn(...args);

    let timerId = setInterval(fn, t, ...args);

    let cancelFn = function() {
        clearInterval(timerId);
    };

    return cancelFn;
};
