var timeLimit = function(fn, t) {
	return async function(...args) {
        return await new Promise(function(resolve, reject) {

            setTimeout(function() {
                reject("Time Limit Exceeded");
            }, t);

            return fn(...args).catch(reject).then(resolve);
        })
    }
};
