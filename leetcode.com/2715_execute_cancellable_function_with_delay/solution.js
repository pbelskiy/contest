var cancellable = function(fn, args, t) {
    let timerId = setTimeout(fn, t, ...args);
    let cancelFn = () => clearTimeout(timerId);

    return cancelFn;
};
