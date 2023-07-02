var promiseAll = async function(functions) {
    let results = new Array(functions.length);
    let resolved = 0;

    return await new Promise(function(resolve, reject) {
        for (let i = 0 ; i < functions.length ; i++) {
            functions[i]().then(function(value) {
                results[i] = value;
                resolved++;

                if (resolved == results.length) {
                    resolve(results);
                }
            }).catch(function(error) {
                reject(error);
            });
        }
    });
};
