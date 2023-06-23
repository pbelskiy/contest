var createCounter = function(init) {
    let val = init;

    return {
        increment: function() {
            return ++val;
        },
        decrement: function() {
            return --val;
        },
        reset: function() {
            val = init;
            return init;
        },
    }
};
