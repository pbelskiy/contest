var compose = function(functions) {
	return function(x) {
        let r = x;

        for (let i = functions.length - 1 ; i >= 0 ; i--)
            r = functions[i](r);

        return r;
    }
};
