Array.prototype.groupBy = function(fn) {
    let group = {};

    for (let i = 0 ; i < this.length ; i++) {
        let key = fn(this[i]);

        if (key in group) {
            group[key].push(this[i]);
        } else {
            group[key] = [this[i]];
        }
    }

    return group;
};
