var compactObject = function(obj) {

    function strip(obj) {
        if (Array.isArray(obj)) {
            var res = [];
        } else {
            var res = {};
        }

        for (let k in obj) {
            /* composed value */
            if (typeof obj[k] === 'object' && obj[k] !== null) {
                if (Array.isArray(obj)) {
                    res.push(strip(obj[k]));
                } else {
                    res[k] = strip(obj[k]);
                }
            } else if (Boolean(obj[k]) === true) {
                if (Array.isArray(obj)) {
                    res.push(obj[k]);
                } else {
                    res[k] = obj[k];
                }
            }
        }

        return res;
    }

    return strip(obj);
};
